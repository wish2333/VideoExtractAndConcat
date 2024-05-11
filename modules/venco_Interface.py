import logging
import os

from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from modules.config import ffpath
from modules.ffmpegApi import FFmpeg
from modules.Ui_vencoInterface import Ui_Form



# 打印初始化ffmpeg路径为：
logging.info(f"初始化ffmpeg路径为：{ffpath.ffmpeg_path}")
logging.info(f"初始化ffprobe路径为：{ffpath.ffprobe_path}")

# 继承自QObject的子类，用于执行后台任务的子类
class Worker(QObject):
    finished = Signal()  # 任务完成时发出的信号
    def __init__(self, task_type, ffmpeg_path, ffprobe_path, *task_args):
        super().__init__()
        self.task_type = task_type
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path
        self.task_args = task_args
    def run_ffmpeg_task(self):
        if self.task_type == 'extract_video':
            self.extract_video(*self.task_args)
        elif self.task_type == 'audio_encode':
            self.audio_encode(*self.task_args)
        elif self.task_type == 'video_encode':
            self.video_encode(*self.task_args)
        self.finished.emit()  # 任务完成，发出信号

    # 在这里可以添加更多任务类型的判断和调用
    def extract_video(self, input_folder, output_folder, start_time, end_time, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.extract_video_single(input_folder, output_folder, start_time, end_time, encoder, overwrite)
    def audio_encode(self, input_file, output_file, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.audio_encode(input_file, output_file, encoder, overwrite)
    def video_encode(self, input_file, output_file, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.video_encode(input_file, output_file, encoder, overwrite)
        
# 继承自QThread的子类，用于后台执行任务的线程类
class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    def run(self):
        self.worker.run_ffmpeg_task()

class VencoInterface(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_variables()
        self.init_action()
        self.init_print()
        self.bind()

    # Custom_encoder
    def change_custom_encoder(self, vcodec, vpreset, resolution, fps, acodec, apreset,):
        custom_encoder = f'{vcodec}{vpreset}{resolution}{fps}{acodec}{apreset}'
        return custom_encoder
    


    # Init_variables
    def init_variables(self):
        # file
        self.input_file_path = ''
        self.output_file_path = ''
        self.audio_file_path = ''
        self.subtitle_file_path = ''
        # encoding
        self.custom_encoder = ''
        self.vcodec = '-vcodec libx264 '
        self.vpreset ='-preset medium -crf 23 '
        self.resolution = ''
        self.fps = ''
        self.acodec = '-acodec aac '
        self.apreset ='-b:a 128k '
        self.bitrate = '800000'
        self.quality = '23'
    # Init_action
    def init_action(self):
        self.lineEdit.setReadOnly(True)  # 禁止修改分辨率
        self.lineEdit_2.setReadOnly(True)  # 禁止修改帧率
        self.comboBox_5.setEnabled(False)  # 禁止修改profile
    # Init_print
    def init_print(self):
        # Welcome message
        self.console.appendPlainText("欢迎使用FFmpeg-python视频处理工具！")
        # encoder
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.plainTextEdit.setPlainText(self.custom_encoder)
        # 判断ffmpeg文件是否存在
        if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
            self.console.appendPlainText("ffmpeg路径或ffprobe路径错误，请检查！")
            logging.error("ffmpeg or ffprobe error, please check the path!")
        else:
            self.console.appendPlainText(f"ffmpeg初始化：{ffpath.ffmpeg_path}")
            self.console.appendPlainText(f"ffprobe初始化：{ffpath.ffprobe_path}")
            logging.info(f"ffmpeg and ffprobe initialized successfully!")
    # Bind Event
    def bind(self):
        # Bind Button Event 
        self.fileBtn_1.clicked.connect(self.open_file_1)  # inout
        self.fileBtn_2.clicked.connect(self.open_file_2)  # output
        self.fileBtn_3.clicked.connect(self.open_file_3)  # audio
        self.fileBtn_4.clicked.connect(self.open_file_4)  # subtitle
        self.pushBtn.clicked.connect(self.encoding)  # encoding
        
        # Checkbox Event
        self.checkBox_2.stateChanged.connect(self.enable_resolution)  # resolution
        self.checkBox_3.stateChanged.connect(self.enable_fps)  # fps
        self.checkBox.stateChanged.connect(self.enable_profile)  # profile

        # Combobox Event
        self.comboBox.currentTextChanged.connect(self.change_vcodec)  # vcodec
        self.comboBox_2.currentTextChanged.connect(self.change_vpreset)  # vpreset
        self.comboBox_4.currentTextChanged.connect(self.change_acodec)  # acodec
        self.comboBox_3.currentTextChanged.connect(self.change_apreset)  # apreset
        self.comboBox_5.currentTextChanged.connect(self.change_profile)  # profile
        self.spinBox.valueChanged.connect(self.change_bitrate)  # bitrate
        self.spinBox_2.valueChanged.connect(self.change_quality)  # quality

        # lineEdit Event
        self.lineEdit.textChanged.connect(self.change_resolution)  # resolution
        self.lineEdit_2.textChanged.connect(self.change_fps)  # fps



    # open_file_1:input
    def open_file_1(self):
        self.input_file_path, _ = QFileDialog.getOpenFileName(self, "选择输入文件", "", "视频文件 (*)")
        if self.input_file_path:
            self.lineEdit1.setText(self.input_file_path)

    # open_file_2:output
    def open_file_2(self):
        if self.lineEdit1.text() != '':
            output_file_path, _ = QFileDialog.getSaveFileName(self, "选择输出文件", f"{self.input_file_path}", "视频文件 (*)")
            if output_file_path:
                self.lineEdit2.setText(output_file_path)
        else:
            QMessageBox.information(self, "警告", "请先选择输入文件！", QMessageBox.Yes)

    # open_file_3:audio
    def open_file_3(self):
        self.audio_file_path, _ = QFileDialog.getOpenFileName(self, "选择音频文件", "", "音频文件 (*.aac *.flac *.mp3 *.m4a *.wav *.wma *.ogg *.opus *.alac)")
        if self.audio_file_path:
            self.lineEdit3.setText(self.audio_file_path)

    # open_file_4:subtitle
    def open_file_4(self):
        if self.lineEdit1.text() != '':
            self.subtitle_file_path, _ = QFileDialog.getOpenFileName(self, "选择字幕文件", "", "字幕文件 (*.srt *.ass)")
            if self.subtitle_file_path:
                self.lineEdit4.setText(self.subtitle_file_path)
        else:
            QMessageBox.information(self, "警告", "请先选择输入文件！", QMessageBox.Yes)



    # Custom encoding Config
    def enable_resolution(self):
        if self.checkBox_2.isChecked():
            self.lineEdit.setReadOnly(False)  # 允许修改分辨率
            self.resolution = f'-s {self.lineEdit.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)
        else:
            self.lineEdit.setReadOnly(True)  # 禁止修改分辨率
            self.resolution = ''
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_resolution(self):
        if self.checkBox_2.isChecked():
            self.resolution = f'-s {self.lineEdit.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)


    def enable_fps(self):
        if self.checkBox_3.isChecked():
            self.lineEdit_2.setReadOnly(False)  # 允许修改帧率
            self.fps = f'-r {self.lineEdit_2.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)
        else:
            self.lineEdit_2.setReadOnly(True)  # 禁止修改帧率
            self.fps = ''
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_fps(self):
        if self.checkBox_3.isChecked():
            self.fps = f'-r {self.lineEdit_2.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_vcodec(self):
        if not self.comboBox.currentText() == 'copy':
            self.vcodec = f'-vcodec {self.comboBox.currentText()} '  # 结尾要有空格
        else:
            self.vcodec = '-vcodec copy '
            self.vpreset = ''
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_vpreset(self):
        self.quality = self.spinBox_2.value()
        self.bitrate = self.spinBox.value() * 1000 
        if self.comboBox_2.currentText() == 'CRF品质-medium' or self.comboBox_2.currentText() == 'CRF品质-fast' or self.comboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.change_vpreset_sub(self.quality)
        else:
            self.change_vpreset_sub(self.bitrate)

    def change_vpreset_sub(self, rate):
        if self.comboBox_2.currentText() == 'CRF品质-medium':
            self.vpreset = f'-preset medium -crf {rate} '
        elif self.comboBox_2.currentText() == 'CRF品质-fast':
            self.vpreset = f'-preset fast -crf {rate} '
        elif self.comboBox_2.currentText() == 'CBR平均码率-medium':
            self.vpreset = f'-preset medium -b:v {rate} '
        elif self.comboBox_2.currentText() == 'CBR平均码率-fast':
            self.vpreset = f'-preset fast -b:v {rate} '
        elif self.comboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.vpreset = f'-preset medium -qp {rate} '
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_bitrate(self):
        if self.comboBox_2.currentText() == 'CBR平均码率-medium' or self.comboBox_2.currentText() == 'CBR平均码率-fast':
            self.bitrate = self.spinBox.value() * 1000
            self.change_vpreset_sub(self.bitrate)

    def change_quality(self):
        if self.comboBox_2.currentText() == 'CRF品质-medium' or self.comboBox_2.currentText() == 'CRF品质-fast' or self.comboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.quality = self.spinBox_2.value()
            self.change_vpreset_sub(self.quality)

    def change_acodec(self):
        if not self.comboBox_4.currentText() == 'copy':
            self.acodec = f'-acodec {self.comboBox_4.currentText()} '  # 结尾要有空格
        else:
            self.acodec = '-acodec copy '
            self.apreset = ''
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.plainTextEdit.setPlainText(self.custom_encoder)

    def change_apreset(self):
        self.apreset = f'-b:a {self.comboBox_3.currentText()} '  # 结尾要有空格
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.plainTextEdit.setPlainText(self.custom_encoder)

    def enable_profile(self):
        if self.checkBox.isChecked():
            self.comboBox_5.setEnabled(True)
            if self.comboBox_5.currentText() == '默认':
                self.custom_encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k '
                self.plainTextEdit.setPlainText(self.custom_encoder)
        else:
            self.comboBox_5.setEnabled(False)

    def change_profile(self):
        if self.checkBox.isChecked() and self.comboBox_5.currentTextChanged():
            if self.comboBox_5.currentText() == '默认':
                self.custom_encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k '
                self.plainTextEdit.setPlainText(self.custom_encoder)
    


    # Encoding
    def encoding(self):
        # 是否传入文件
        # 如果输入文件和输出文件都存在，则执行转码任务
        if not self.lineEdit1.text() == '' and not self.lineEdit2.text() == '':
            # 检查输入文件是否合法
            if os.path.isfile(self.lineEdit1.text()):
                if self.lineEdit3.text() == '' and self.lineEdit4.text() == '':
                    # 无音频无字幕
                    if self.timeEdit.text() == '0:00:00:000' and self.timeEdit_2.text() == '0:00:00:000':
                        self.console.appendPlainText("执行简单转码任务，请稍等...")
                        # 简单转码任务
                        self.worker = Worker('video_encode', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.lineEdit1.text(), self.lineEdit2.text(), self.plainTextEdit.toPlainText())  # 开启子进程
                        self.thread = WorkerThread(self.worker)
                        self.thread.started.connect(lambda: self.console.appendPlainText("开始视频转码"))  # 线程开始时显示提示信息
                        self.thread.finished.connect(lambda: self.console.appendPlainText("完成视频转码"))  # 线程结束时显示提示信息
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.start()  # 开始线程
                    elif not self.timeEdit.text() == '0:00:00:000' or not self.timeEdit_2.text() == '0:00:00:000':
                        self.console.appendPlainText("执行切割任务，请稍等...")
                        # 切割任务
                        self.worker = Worker('extract_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.lineEdit1.text(), self.lineEdit2.text(), self.timeEdit.text(), self.timeEdit_2.text(), self.plainTextEdit.toPlainText())  # 开启子进程
                        self.thread = WorkerThread(self.worker)
                        self.thread.started.connect(lambda: self.console.appendPlainText("开始视频转码"))  # 线程开始时显示提示信息
                        self.thread.finished.connect(lambda: self.console.appendPlainText("完成视频转码"))  # 线程结束时显示提示信息
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.start()  # 开始线程
                else:
                    # 有音频或字幕，功能省缺
                    ########
                    QMessageBox.information(self, "提示", "音频或字幕功能暂未实现，请等待更新！", QMessageBox.Yes)
                    self.lineEdit3.setText('')
                    self.lineEdit4.setText('')
                    ########
            else:
                QMessageBox.warning(self, "警告", "输入文件不存在！", QMessageBox.Yes)
        # 如果输入输出不存在，音频存在，执行音频转码
        elif self.lineEdit1.text() == '' and self.lineEdit2.text() == '' and not self.lineEdit3.text() == '':
            self.custom_encoder = f'{self.acodec} {self.apreset} '  # 结尾要有空格
            QMessageBox.information(self, "提示", f"进行音频转码，请选择输出文件，转码格式为{self.acodec} {self.apreset}", QMessageBox.Yes)
            audio_output_file_path, _ = QFileDialog.getSaveFileName(self, "选择输出文件", self.lineEdit3.text(), "音频文件 (*.aac *.flac *.mp3 *.m4a *.wav *.wma *.ogg *.opus *.alac)")
            # 开始音频转码
            self.worker = Worker('audio_encode', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.lineEdit3.text(), audio_output_file_path, self.custom_encoder)  # 开启子进程
            self.thread = WorkerThread(self.worker)
            self.thread.started.connect(lambda: self.console.appendPlainText("开始音频转码"))  # 线程开始时显示提示信息
            self.thread.finished.connect(lambda: self.console.appendPlainText("完成音频转码"))  # 线程结束时显示提示信息
            self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
            self.thread.start()  # 开始线程
            ######## 显示进度条 ########
            # 打开输出文件夹
            # 判断是否成功
                # os.startfile(os.path.dirname(audio_output_file_path))
        # 如果输出都不存在，则提示选择文件
        elif not self.lineEdit1.text() == '' and self.lineEdit2.text() == '':
            QMessageBox.warning(self, "警告", "请选择输出文件！", QMessageBox.Yes)
        




            







# if not self.timeEdit.text() == '0:00:00:000' and not self.timeEdit_2.text() == '0:00:00:000':
#     self.console.appendPlainText("执行切割任务，请稍等...")