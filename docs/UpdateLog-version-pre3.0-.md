# Update20240519-1921

## version-pre4.1

视频批处理面板完成了中断按钮及逻辑实现（通过中断标志和回调函数向api模块的传输与接受），api模块通过守卫线程实现中断操作并调用回调函数传输中断完成标志。

### main.py

防止日志文件夹未建立

```python
if os.path.exists(r'log') == False:

    os.mkdir(r'log')

file_handler = logging.FileHandler(r'log/log.txt', mode='w', encoding='utf-8')
```

### vcodecp_Interface.py

Worker子类中，向FFmpeg模块传入中断标志和回调函数，调整部分变量为继承Worker子类的变量以便于中断函数调用，调用FFmpeg模块中的update_interrupt_flag函数，以更新其中的中断标志。建立interrupted_callback函数以获取回调信号并发出中断完成标志。

```python
# 继承自QObject的子类，用于执行后台任务的子类
class Worker(QObject):
    started = Signal()  # 任务开始时发出的信号
    finished = Signal()  # 任务完成时发出的信号
    interrupted = Signal()  # 任务被中断时发出的信号
    callback = Signal()  # 任务执行过程中输出的信号

    def __init__(self, task_type, ffmpeg_path, ffprobe_path, *task_args, callback=None):
        super().__init__()
        ......
        self._started_flag = False  # 任务是否开始的标志
        self._interrupted_flag = False  # 任务是否被中断的标志
        self.callback = callback  # 任务执行过程中输出的回调函数
        self.is_interrupted = False  # 任务被中断时的回调函数

    def interrupt(self):
        self._interrupted_flag = True  # 设置任务被中断的标志
        self.ffmpeg_instance.update_interrupt_flag(self._interrupted_flag)  # 更新全局中断标志
        logging.info('中止信号已发出')
    def interrupted_callback(self):
        logging.info('中止信号回调，worker任务被中断')
        self.is_interrupted = True  # 设置任务被中断的标志
        if callable(self.callback):
            self.callback()
        self.interrupted.emit()  # 发出中断信号

    def run_ffmpeg_task(self):
        self._started_flag = True  # 任务开始的标志
        self.started.emit()  # 任务开始，发出信号
        if self.task_type == 'extract_video':
            self.extract_video(*self.task_args)
        ......
        self.finished.emit()  # 任务完成，发出信号


    # 在这里可以添加更多任务类型的判断和调用
    def extract_video(self, input_folder, output_folder, start_time, end_time, encoder, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.extract_video_single(input_folder, output_folder, start_time, end_time, encoder, overwrite)
```

添加中断函数绑定到中断按钮上，经过中断完成标志确认后等待线程终止并删除线程。

```python
def stop(self):
    if self.worker._started_flag:
        self.is_paused = True  # 开启暂停标志
        logging.info(f'暂停循环，i={self.i}')
        self.i = 2600000000  # 设定一个很大的数值，使线程结束
        self.worker.interrupt()  # 停止worker
        if self.worker.is_interrupted:  # 停止worker
            self.thread.wait()  # 等待线程结束
            self.worker.deleteLater()  # 删除worker对象
            self.thread.deleteLater()  # 删除线程对象
            self._started_flag = False
            self.is_paused = False  # 重置暂停标志
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("警告", "转码任务已暂停！软件即将退出，请重新启动！", parent=self).exec()
```

### ffmpegApi.py

初始化函数中，获取中断标志和回调信号。建立update_interrupt_flag函数以获得中断标志的更新。建立check_interrupt_flag函数以始终检查中断标志的更新。建立interrupt_run()函数以中断FFmpeg进程的运行，并在中断完成后调用Interface的回调函数发出中断完成标志。

```python
def __init__(self, 
    ffmpeg_path=ffpath.ffmpeg_path,
    ffprobe_path=ffpath.ffprobe_path,
    interrupt_flag=False,  # 中断标志
    callback=None,  # 回调函数
):
    self.ffmpeg_path = ffmpeg_path
    self.ffprobe_path = ffprobe_path
    self.interrupt_flag = interrupt_flag
    self.callback = callback

def update_interrupt_flag(self, flag=True):
    self.interrupt_flag = flag
def check_interrupt_flag(self):
    while not self.interrupt_flag:  # 循环直至收到中断信号
        # logging.info("ffmpegapi守卫线程运行中")
        time.sleep(1)
    logging.info("ffmpegapi检测到中断请求")
    self.interrupt_run()
def interrupt_run(self):
    if self.interrupt_flag:
        # 如果收到中断信号，则终止FFmpeg进程
        logging.info("尝试终止FFmpeg进程")
        self.p.terminate()
        self.p.wait(timeout=5)
        if self.p.poll() is None:
            self.p.kill()
        if callable(self.callback):
            self.callback()
        self.interrupt_flag = False
        logging.info("FFmpeg进程强制终止")
    logging.info("ffmpegapi中断请求已处理")
```

run函数在建立FFmpeg-subprocess运行进程以外，创建t守卫进程（靶向check_interrupt_flag函数）接受中断信号并执行中断。try-expect语句结束确认进程顺利退出。

```python
# 定义run方法来执行FFmpeg命令
def run(self, 
    cmd
):
    t = None  # t建立在try之外让finally可以检测
    try:
        cmd = [self.ffmpeg_path] + cmd
        cmd_str = ' '.join(cmd)
        logging.info(f"尝试执行：{cmd_str}")
        # 创建线程运行FFmpeg命令
        self.p = subprocess.Popen(
            cmd_str, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT
        )
        # 创建线程检测中断信号
        t = threading.Thread(target=self.check_interrupt_flag)
        t.daemon = True
        t.start()
        if t.is_alive():
            logging.info('启动守卫线程成功')
        else:
            logging.error('启动守卫线程失败')
        # 实时输出FFmpeg命令的执行信息
        while True:
            line = self.p.stdout.readline().decode('utf-8')
            if not line:
                # 如果没有更多输出，检查进程是否已经结束
                if self.p.poll() is not None:
                    break
                else:
                    continue
            logging.info(line.strip())  # 打印输出信息
        # 如果出错，获取错误信息
        out, err = self.p.communicate()
        if self.p.returncode != 0:
            logging.info(f"命令执行失败，错误信息：{err.decode('utf-8')}")
            raise Exception(err.decode('utf-8'))
    except FileNotFoundError as fnf_error:
        logging.error(f"找不到ffmpeg或ffprobe命令，请检查ffmpeg_path和ffprobe_path是否正确配置。")
        raise fnf_error
    except PermissionError as p_error:
        logging.error(f"ffmpeg或ffprobe命令没有执行权限，请检查ffmpeg_path和ffprobe_path是否正确配置。")
        raise p_error
    except Exception as e:
        logging.error(f"执行FFmpeg命令失败：{e}")
        raise e
    finally:
        logging.info("FFmpeg命令执行完成")
        if t and t.is_alive():
            self.interrupt_flag = True  # 设置中断标志
            t.join()
            self.interrupt_flag = False  # 重置中断标志
            logging.info("守卫线程退出")
```

## version-pre4.2

完成了视频面板（单文件）的音视频及字幕混流合成。

修复了中断后守卫线程t没有被正确关闭的错误。

### vcodec_Interface.py

subtitle非常容易错误检测路径为选项，必须注意转义的问题

```python
if self.timeEdit.text() == '0:00:00:000' and self.timeEdit_2.text() == '0:00:00:000':
    self.console.appendPlainText("执行音视频合成任务，请稍等...")
    # 音视频合成任务
    if self.lineEdit3.text() != '':
        audio_input_file_path = self.lineEdit3.text()
        audio = f'-i "{audio_input_file_path}"'
    else:
        audio = ''
    if self.lineEdit4.text() != '':
        subtitle_input_file_path = self.lineEdit4.text().replace(':', r'\:')  # 注意转义
        if os.path.splitext(subtitle_input_file_path)[1] == '.srt':
            subtitle_format = 'subtitles'
        elif os.path.splitext(subtitle_input_file_path)[1] == '.ass':
            subtitle_format = 'ass'
        else:
            logging.error("字幕格式错误，请检查！")
        subtitle = f'-vf "{subtitle_format}=\'{subtitle_input_file_path}\'"'  
    else:
        subtitle = ''
    self.worker = Worker('avsmix_encode', ffpath.ffmpeg_path, ffpath.ffprobe_path,self.lineEdit1.text(), self.lineEdit2.text(), audio, subtitle, self.plainTextEdit.toPlainText())  # 开启子进程
    self.thread = WorkerThread(self.worker)
    self.thread.started.connect(lambda: self.console.appendPlainText("开始音视频合成"))  # 线程开始时显示提示信息
    self.thread.finished.connect(lambda: self.console.appendPlainText("完成音视频合成"))  # 线程结束时显示提示信息
    self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
    self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
    self.thread.start()  # 开始线程
```

### ffmpeg.py

```python
# 音视频字幕混合
def avsmix_encode(self, 
    input_file, 
    output_file, 
    audio,
    subtitle,
    encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k', 
    overwrite='-y'):
    cmd = [
        '-hide_banner',
        overwrite, 
        '-i', 
        f'"{input_file}"', 
        audio,
        subtitle, 
        encoder,
        f'"{output_file}"'
    ]
    self.run(cmd)
    file = os.path.basename(input_file)
    logging.info(file + '视频字幕混合完成')
```

# Update20240513-version-pre3.0

实现批处理界面，添加了加速、切割时间段和合并片头片尾功能，部分逻辑以及API接口函数有所修改，后续调用需要注意

![verison-pre3.0](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre3.0.jpg)

## 整体逻辑

### 文件操作

导入文件：判断是否重复导入

导出文件夹：判断是否导入文件

清除导入导出

```python
def select_input_file(self):
        self.append_input_file_args, _ = QFileDialog.getOpenFileNames(self, "选择输入文件", "", "All Files (*)")
        for file_path in self.append_input_file_args:
            if file_path not in self.input_file_args:
                self.input_file_args.append(file_path)
                item = QListWidgetItem(file_path)
                self.VcodecpIFinputlist.addItem(item)
def select_output_folder(self):
        if self.input_file_args != []:
            output_folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "")  # 选择输出文件夹
            self.output_file_args = [os.path.join(output_folder, os.path.basename(file_path)) for file_path in self.input_file_args]  # 获得输出文件，输出文件名与输入文件名相同
            self.VcodecpIFoutputfolder.setText(output_folder)
        else:
            MessageBox("警告", "请先选择输入文件！", parent=self).exec()

def clear_input_file(self):
    self.input_file_args = []
    self.output_file_args = []
    self.VcodecpIFoutputfolder.setText('选择输出文件夹')
    self.VcodecpIFinputlist.clear()
```

### 编码设置

设置好默认状态，还有复选框打钩的动作（enable对应框），所以设置直接反映到自定义PlainTextEdit，以便自定义和后续函数获取

### 滤镜设置

#### debug_of_filter_config

确认未实现的多重滤镜功能的关闭，传回状态布尔值，以决定是否开始处理，否则弹框提示

#### simple_encoding（未选择滤镜设置）

```python
if os.path.isfile(input_file) and not self.VcodecpIFcheckBox_4.isChecked() and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_merge.isChecked()
```

#### accelerated_encoding

```python
if os.path.isfile(input_file) and self.VcodecpIFcheckBox_4.isChecked() and self.VcodecpIFdoubleSpinBox.value() != 1 and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_merge.isChecked():

def accelerated_encode(self, 
    input_file, 
    output_file, 
    rate=1,
    encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k', 
    overwrite='-y'):
    cmd = [
    overwrite, 
    '-i', 
    f'"{input_file}"', 
    f'-filter_complex "[0:v]setpts=PTS/{rate}[v];[0:a]atempo={rate}[a]" -map "[v]" -map "[a]"',
    encoder, 
    f'"{output_file}"'
    ]
    self.run(cmd)
    file = os.path.basename(input_file)
    logging.info(file + '视频加速完成')
```

#### clear_filter_config

```
def clear_filter_config(self):
    self.VcodecpIFcheckBox_4.setChecked(False)
    self.VcodecpIFdoubleSpinBox.setEnabled(False)
    self.VcodecpIFcheckBox_merge.setChecked(False)
    self.VcodecpIFtimeEdit_3.setTime(QTime(0, 0, 0, 0))  # 注意需要使用QCore.QTime设置TimeEdit
    self.VcodecpIFtimeEdit_2.setTime(QTime(0, 0, 0, 0))  # 注意需要使用QCore.QTime设置TimeEdit
    self.op_file = ''
    self.ed_file = ''
    self.VcodecpIFpushButton_3.setText('选择片头')
    self.VcodecpIFpushButton_4.setText('选择片尾')
```

#### extract_or_cut_video

```
if os.path.isfile(input_file) and not self.VcodecpIFcheckBox_4.isChecked() and not self.VcodecpIFcheckBox_merge.isChecked():
    if self.VcodecpIFtimeEdit_3.text() != '0:00:00:000' or self.VcodecpIFtimeEdit_2.text() != '0:00:00:000':
        if self.VcodecpIFradioButton.isChecked():  # 如果选择了片尾时长
            self.worker = Worker('extract_video',...  # 执行切割片尾模式
        elif self.VcodecpIFradioButton_2.isChecked():  # 如果选择了结束时间
            self.worker = Worker('cut_video',...  # 执行时间段切割模式
```

#### merge_or_concat_video

```
if  self.VcodecpIFcheckBox_merge.isChecked() and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_4.isChecked():
    if self.VcodecpIFpushButton_3.text() != '选择片头' and self.VcodecpIFpushButton_4.text() != '选择片尾':
        self.merge_3_videos()  # 片头片尾合并
    elif self.VcodecpIFpushButton_3.text() != '选择片头' and self.VcodecpIFpushButton_4.text() == '选择片尾':
        self.merge_2_videos(True)  # 片头合并
    elif self.VcodecpIFpushButton_3.text() == '选择片头' and self.VcodecpIFpushButton_4.text() != '选择片尾':
        self.merge_2_videos(False)  # 片尾合并
    else:
        MessageBox("错误", "请选择合并方式！即选择片头或片尾！", parent=self).exec()
        self.debugflag_of_filter_config = False
        self.i = 0  # 循环计数器清零

def merge_3_videos(self):
    if os.path.isfile(self.merge_input_file) and os.path.isfile(self.op_file) and os.path.isfile(self.ed_file):
        self.VcodecpIFconsole.appendPlainText("执行合并任务，请稍等...")
        # 判断传入的分辨率、帧率信息
        if self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
        elif self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
        elif not self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
        elif not self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():

def merge_2_videos(self, is_op):
    if is_op:
        if self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
            self.worker = Worker('merge_video_two',...
        elif ...
    elif not is_op:
        ...
```

#### 处理视频-多线程与循环暂停的处理

```
def encoding(self):
    self.debugflag_of_filter_config = False  # 调试模式
    self.debug_of_filter_config()
    if self.debugflag_of_filter_config:
        # 是否传入文件
        # 如果输入文件和输出文件都存在，则执行转码任务
        self.freeze_config('正在执行转码任务，请稍等...')  # 冻结操作
        if self.input_file_args != [] and self.output_file_args != []:
            while self.i < (len(self.input_file_args)):
                if self.is_paused:  # 若暂停，则不进行循环
                    break
                self.simple_encoding()
                self.accelerated_encoding()
                self.extract_or_cut_video()
                self.merge_or_concat_video()
            else:
                self.i = 0  # 循环计数器清零
                self.VcodecpIFconsole.appendPlainText("全部转码任务完成！")
                self.clear_input_file()
                self.unfreeze_config()  # 解冻操作

        # 如果输入文件存在，但输出文件不存在，则弹出提示框，ok进入选择，cancel退出
        elif self.input_file_args != [] and self.output_file_args == []:
            warn = MessageBox("警告", "请先选择输出文件夹！", parent=self)
            if warn.exec():
                self.select_output_folder()
                if_continue = MessageBox("提示", "是否继续执行？", parent=self)
                if if_continue.exec():
                    self.simple_encoding()
                    self.accelerated_encoding()
                    self.extract_or_cut_video()
                    self.merge_or_concat_video()
             else:
                 self.i = 0  # 循环计数器清零
                 self.unfreeze_config()

        # 如果输入文件不存在，则弹出提示框，ok退出，cancel进入选择
        elif self.input_file_args == []:
            MessageBox("警告", "请先选择输入文件！", parent=self).exec()
            self.clear_input_file()
            self.unfreeze_config()

def freeze_config(self, text=''):
    self.VcodecpIFlineEditVE.setEnabled(False)  # 禁止修改视频编码器
    self.VcodecpIFlineEditAE.setEnabled(False)  # 禁止修改音频编码器
    ...

# 使用self.i参数传入while循环，同时传入暂停标志使得每一条视频的处理过程中循环不继续下去
def on_thread_started(self):
    self.is_paused = True  # 开启暂停标志
    logging.info(f'线程创建，暂停循环，i={self.i}')
def on_thread_finished(self):
    self.is_paused = False  # 重置暂停标志
    self.i = self.i + 1  # 开启下一个文件
    logging.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
    self.encoding()  # 开启下一个线程


# 示例任务，看on_thread_started()和on_thread_finished的调用
def simple_encoding(self):
    input_file = self.input_file_args[self.i]
    output_file = self.output_file_args[self.i]
    if os.path.isfile(input_file) and not self.VcodecpIFcheckBox_4.isChecked() and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_merge.isChecked():
        self.VcodecpIFconsole.appendPlainText("执行简单转码任务，请稍等...")
        self.worker = Worker('video_encode', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, self.VcodecpIFplainTextEdit.toPlainText())  # 开启子进程
        self.thread = WorkerThread(self.worker)
        self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}开始视频转码"))  # 线程开始时显示提示信息
        logging.info(f"Simple encoding task started, input file: {input_file}, output file: {output_file}")
        self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
        self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}完成视频转码"))  # 线程结束时显示提示信息
        logging.info(f"Simple encoding task finished, input file: {input_file}, output file: {output_file}")
        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
        self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
        self.thread.start()  # 开始线程
    elif not os.path.isfile(input_file):
        MessageBox("错误", f"{input_file}不存在！", parent=self).exec()
        self.on_thread_finished()  #  进行下一个文件
```

#### 安全退出QThread

https://geek-docs.com/pyqt/pyqt-questions/110_pyqt_how_to_stop_a_qthread_from_the_gui.html

该功能暂未实现

## FluentUI的特殊

fluentcombobox是从linetext继承来的，需要在Designer提升的时候注意，且列表需要再Interface.py中设置一下
