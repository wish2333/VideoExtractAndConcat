
import os

from PySide6.QtCore import Qt, QThread, Signal, QObject, QTime
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QListWidgetItem
from qfluentwidgets import MessageBox

from modules.config import ffpath
from modules.ffmpegApi import FFmpeg
from modules.ffmpegApi_filter import FFmpegFilter
from modules.Ui_VfilterInterface import Ui_VfilterInterface

from modules.logger_config import logger

# 继承自QObject的子类，用于执行后台任务的子类
class Worker(QObject):
    started = Signal()  # 任务开始时发出的信号
    finished = Signal()  # 任务完成时发出的信号
    interrupted = Signal()  # 任务被中断时发出的信号
    callback = Signal()  # 任务执行过程中输出的信号

    def __init__(self, task_type, ffmpeg_path, ffprobe_path, *task_args, callback=None):
        super().__init__()
        self.task_type = task_type
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path
        self.task_args = task_args
        logger.info(f"Simple {task_type} task started")
        self._started_flag = False  # 任务是否开始的标志
        self._interrupted_flag = False  # 任务是否被中断的标志
        self.callback = callback  # 任务执行过程中输出的回调函数
        self.is_interrupted = False  # 任务被中断时的回调函数
    def interrupt(self):
        self._interrupted_flag = True  # 设置任务被中断的标志
        self.ffmpeg_instance.update_interrupt_flag(self._interrupted_flag)  # 更新全局中断标志
        logger.info('中止信号已发出')
    def interrupted_callback(self):
        logger.info('中止信号回调，worker任务被中断')
        self.is_interrupted = True  # 设置任务被中断的标志
        if callable(self.callback):
            self.callback()
        self.interrupted.emit()  # 发出中断信号

    def run_ffmpeg_task(self):
        self._started_flag = True  # 任务开始的标志
        self.started.emit()  # 任务开始，发出信号
        if self.task_type == 'run':
            self.run_video(*self.task_args)
        elif self.task_type == 'norEx_video':
            self.norEx_video(*self.task_args)
        elif self.task_type == 'mulEx_video':
            self.mulEx_video(*self.task_args)
        else:
            logger.error(f"Unknown task type: {self.task_type}")
        
        self.finished.emit()  # 任务完成，发出信号
        

    # 在这里可以添加更多任务类型的判断和调用
    def run_video(self, cmd):
        self.ffmpeg_instance = FFmpegFilter(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.run(cmd)
    def norEx_video(self, input, output, action, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.norEx_video(input, output, action, overwrite)
    def mulEx_video(self, input, output, action, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.mulEx_video(input, output, action, overwrite)



# 继承自QThread的子类，用于后台执行任务的线程类
class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
        self.worker.interrupted.connect(self.handle_interrupt)  # 任务被中断时停止线程
    def run(self):
        try:
            self.worker.run_ffmpeg_task()
        except Exception as e:
            logger.error(f"Error occurred while running {self.worker.task_type} task: {e}")

    def handle_interrupt(self):
        self.quit()  # 停止线程

class VfilterInterface(QWidget, Ui_VfilterInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_variables()
        self.init_action()
        self.init_print()
        self.bind()
        # 必须给子界面设置全局唯一的对象名
    
    # Init_variables
    def init_variables(self):
        # file
        self.input_file_args = []
        self.output_file_args = []
        # 循环
        self.i = 0
        self.is_paused = False
        # rotate
        self.image_ = ['', '']

    # Init_action
    def init_action(self):

        self.rotate_dict = {'横竖屏转换':'','横屏转竖屏-背景图片': 'H2V-I', '横屏转竖屏-背景原片': 'H2V-T', '横屏转竖屏-背景黑色': 'H2V-B', '竖屏转横屏-背景图片': 'V2H-I', '竖屏转横屏-背景原片': 'V2H-T', '竖屏转横屏-背景黑色': 'V2H-B'}
        # 将字典的值添加到选项中
        self.VcodecpIFcutsomFilter.addItems(list(self.rotate_dict.keys()))
        


    # Init_print
    def init_print(self):
        logger.debug("VfilterInterface is initialized")  # 直接使用导入的全局日志记录器
        

    # Bind Event
    def bind(self):

        # file operation
        self.Vfilterinputfile.clicked.connect(self.select_input_file)
        self.Vfilteroutputfolder.clicked.connect(self.select_output_folder)
        self.Vfilterinputclear.clicked.connect(self.clear_input_file)
        # self.remuxpushButton_2.clicked.connect(lambda: self.norEx('V'))
        # self.remuxpushButton_3.clicked.connect(lambda: self.norEx('A'))
        # self.remuxpushButton_5.clicked.connect(lambda: self.mulEx('V'))
        # self.remuxpushButton_6.clicked.connect(lambda: self.mulEx('A1'))
        # self.remuxpushButton_4.clicked.connect(lambda: self.mulEx('A2'))
        # self.remuxpushButton_7.clicked.connect(lambda: self.mulEx('A3'))
        # self.remuxpushButton_10.clicked.connect(lambda: self.mulEx('A4'))
        # self.remuxpushButton_8.clicked.connect(lambda: self.mulEx('S1'))
        # self.remuxpushButton_9.clicked.connect(lambda: self.mulEx('S2'))

        # filter operation
        self.VcodecpIFcutsomFilter.currentIndexChanged.connect(self.change_rotate_filter)
        self.Vfilterbgimg.clicked.connect(self.select_bg_img)
        self.VcodecpIFClearFil.clicked.connect(self.clear_filter)
        self.VcodecpIFcheckBox_4.stateChanged.connect(self.change_audio_filter)
        self.VfilterlineEdit_3.textChanged.connect(self.change_resolution)

        # start
        self.VfilterpushBtn.clicked.connect(self.filter_video)
        self.VfilterSTBtn.clicked.connect(self.stop)
        self.VfilterpushBtn_2.clicked.connect(self.unfreeze_config)


    
    #  File_operation
    def select_input_file(self):
        self.append_input_file_args, _ = QFileDialog.getOpenFileNames(self, "选择输入文件", "", "All Files (*)")
        for file_path in self.append_input_file_args:
            if file_path not in self.input_file_args:
                self.input_file_args.append(file_path)
                item = QListWidgetItem(file_path)
                self.Vfilterinputlist.addItem(item)

    def select_output_folder(self):
        if self.input_file_args != []:
            output_folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "")  # 选择输出文件夹
            if output_folder != '':  # 输出文件夹不为空且输出文件夹与输入文件夹不同
                self.output_file_args = [os.path.join(output_folder, os.path.basename(file_path)) for file_path in self.input_file_args]  # 获得输出文件，输出文件名与输入文件名相同
                self.Vfilteroutputfolder.setText(output_folder)
            else:
                self.Vfilteroutputfolder.setText('选择输出文件夹')
        else:
            MessageBox("警告", "请先选择输入文件！", parent=self).exec()

    def clear_input_file(self):
        self.input_file_args = []
        self.output_file_args = []
        self.Vfilteroutputfolder.setText('选择输出文件夹')
        self.Vfilterinputlist.clear()
    
    def clear_filter(self):
        self.VcodecpIFcutsomFilter.setText('横竖屏转换')
        self.VfilterlineEdit_3.setText('x')
        self.image_ = ['', '']
        self.VcodecpIFcheckBox_4.setChecked(False)
        self.Vfilterbgimg.setText('选择背景图片')
        self.VfilterplainTextEdit_2.setPlainText('滤镜参数：')

    def change_rotate_filter(self):
        index = self.VcodecpIFcutsomFilter.currentText()
        # 根据index从self.rotate_dict获取对应的旋转参数
        self.image_[0] = self.rotate_dict[index]
        if self.image_[0] in ['V2H-I', 'V2H-T', 'V2H-B']:
            self.VfilterlineEdit_3.setText('1920x1080')
        elif self.image_[0] in ['H2V-I', 'H2V-T', 'H2V-B']:
            self.VfilterlineEdit_3.setText('1080x1920')
        else:
            self.VfilterlineEdit_3.setText('x')
            filter = ''
        resolution = self.VfilterlineEdit_3.text()
        x = resolution.split('x')[0]
        y = resolution.split('x')[1]
        if self.image_[0] in ['V2H-T', 'V2H-B', 'H2V-T', 'H2V-B']:
            fs = FFmpegFilter()
            filter = fs.rotate_filter(self.image_, x, y)
        if self.image_[0] in ['V2H-I', 'H2V-I']:
            fs = FFmpegFilter()
            filter = fs.rotate_filter(self.image_, x, y, 'flag')
        if self.VcodecpIFcheckBox_4.isChecked():
            af = ' -af loudnorm=i=-16.0:lra=5.0:tp=-0.3'
            filter = filter + af
        self.VfilterplainTextEdit_2.setPlainText(filter)

    def select_bg_img(self):
        self.image_[1] = QFileDialog.getOpenFileName(self, "选择背景图片", "", "All Files (*)")[0]
        if self.image_[1] != '':
            name = os.path.basename(self.image_[1])
            self.Vfilterbgimg.setText(name)
        else:
            self.image_[1] = ''
            self.Vfilterbgimg.setText('选择背景图片')

    def change_audio_filter(self):
        if self.VcodecpIFcheckBox_4.isChecked() and self.VfilterplainTextEdit_2.toPlainText() != '滤镜参数：':
            self.VfilterplainTextEdit_2.setPlainText(self.VfilterplainTextEdit_2.toPlainText() + ' -af loudnorm=i=-16.0:lra=5.0:tp=-0.3')
        elif self.VcodecpIFcheckBox_4.isChecked() and self.VfilterplainTextEdit_2.toPlainText() == '滤镜参数：':
            self.VfilterplainTextEdit_2.setPlainText(' -af loudnorm=i=-16.0:lra=5.0:tp=-0.3')
        else:
            self.VfilterplainTextEdit_2.setPlainText(self.VfilterplainTextEdit_2.toPlainText().replace(' -af loudnorm=i=-16.0:lra=5.0:tp=-0.3', ''))

    def change_resolution(self):
        if self.VcodecpIFcutsomFilter.text() != '横竖屏转换':
            resolution = self.VfilterlineEdit_3.text()
            x = resolution.split('x')[0]
            y = resolution.split('x')[1]
            fs = FFmpegFilter()
            if self.image_[0] in ['V2H-T', 'V2H-B', 'H2V-T', 'H2V-B']:
                filter = fs.rotate_filter(self.image_, x, y)
            if self.image_[0] in ['V2H-I', 'H2V-I']:
                filter = fs.rotate_filter(self.image_, x, y, 'flag')
            if self.VcodecpIFcheckBox_4.isChecked():
                af = ' -af loudnorm=i=-16.0:lra=5.0:tp=-0.3'
                filter = filter + af
            self.VfilterplainTextEdit_2.setPlainText(filter)

    def filter_video(self):
        cmd = []
        
        if self.VfilterplainTextEdit_2.toPlainText() in ['', '滤镜参数：']:
            MessageBox("警告", "请先选择滤镜！", parent=self).exec()
            return
            
        if self.input_file_args != [] and self.output_file_args != []:
            while self.i < len(self.input_file_args):  # 循环处理多个文件
                if self.is_paused:  # 循环暂停
                    break
                input_file = self.input_file_args[self.i]
                output_file = self.output_file_args[self.i] + 'rotate' +os.path.splitext(input_file)[-1]
                if os.path.isfile(input_file):
                    rotate_filter = self.VfilterplainTextEdit_2.toPlainText()
                    if self.image_[0] in ['V2H-I', 'H2V-I']:
                        fs = FFmpegFilter()
                        duration = fs.get_duration(input_file)
                        rotate_filter = rotate_filter.replace('@duration', str(duration))
                        cmd += ['-i', f'"{self.image_[1]}"']
                    cmd += [rotate_filter]
                    encoder = self.VfilterplainTextEdit.toPlainText()
                    cmd += [encoder]
                    try:
                        self.freeze_config()
                        cmd = ['-hide_banner', '-y', '-i', f'"{input_file}"'] + cmd
                        cmd += [f'"{output_file}"']
                        self.worker = Worker('run', ffpath.ffmpeg_path, ffpath.ffprobe_path, cmd)  # 创建worker对象
                        self.thread = WorkerThread(self.worker)  # 创建线程对象
                        self.thread.started.connect(self.on_thread_started())  # 线程开始信号连接到槽函数
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.finished.connect(self.filter_thread_finished)  # 线程结束信号连接到槽函数
                        self.thread.start()  # 启动线程
                    except Exception as e:
                        logger.error(f"Error occurred while creating worker object: {e}")
                else:
                    m = MessageBox("错误", f"{input_file}不存在！", parent=self)
                    if not m.exec():
                        self.clear_input_file()  # 清空输入文件列表
                        self.i = 2666666666  # 设定一个很大的数值，使线程结束
                        self.filter_thread_finished()  #  进行下一个文件
                        break


    def on_thread_started(self):
        self.is_paused = True  # 开启暂停标志
        logger.info(f'线程创建，暂停循环，i={self.i}')
    def filter_thread_finished(self):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        if self.i < len(self.input_file_args):  # 还有文件未处理
            logger.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
            self.filter_video()  # 开启下一个线程
        else:
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("提示", "转码任务已完成！", parent=self).exec()

    def freeze_config(self, text=''):
        self.VfilterplainTextEdit.setEnabled(False)  # 禁止修改视频格式
        self.VcodecpIFClearFil.setEnabled(False)  # 禁止清空滤镜
        self.VcodecpIFcutsomFilter.setEnabled(False)  # 禁止修改滤镜
        self.VfilterlineEdit_3.setEnabled(False)  # 禁止修改分辨率
        self.Vfilterbgimg.setEnabled(False)  # 禁止修改背景图片
        self.VcodecpIFcheckBox_4.setEnabled(False)  # 禁止修改音频增益
        self.VfilterplainTextEdit_2.setEnabled(False)  # 禁止修改滤镜参数
        logger.info(f"Freeze config. {text}")
        # self.VcodecpIFconsole.appendPlainText("冻结配置")
    def unfreeze_config(self):
        self.VfilterplainTextEdit.setEnabled(True)  # 解除视频格式冻结
        self.VcodecpIFClearFil.setEnabled(True)  # 解除滤镜清空冻结
        self.VcodecpIFcutsomFilter.setEnabled(True)  # 解除滤镜修改冻结
        self.VfilterlineEdit_3.setEnabled(True)  # 解除分辨率修改冻结
        self.Vfilterbgimg.setEnabled(True)  # 解除背景图片修改冻结
        self.VcodecpIFcheckBox_4.setEnabled(True)  # 解除音频增益修改冻结
        self.VfilterplainTextEdit_2.setEnabled(True)  # 解除滤镜参数修改冻结
        logger.info("Unfreeze config.")
        # self.VcodecpIFconsole.appendPlainText("解除冻结配置")

    def stop(self):
        if self.worker._started_flag:
            self.is_paused = True  # 开启暂停标志
            logger.info(f'暂停循环，i={self.i}')
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