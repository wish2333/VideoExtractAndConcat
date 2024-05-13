import logging
import os

from PySide6.QtCore import Qt, QThread, Signal, QObject, QTime
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QListWidgetItem
from qfluentwidgets import MessageBox

from modules.config import ffpath
from modules.ffmpegApi import FFmpeg
from modules.Ui_vcodecpInterface import Ui_VcodecpInterface

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
        logging.info(f"Simple {task_type} task started")
    def run_ffmpeg_task(self):
        if self.task_type == 'extract_video':
            self.extract_video(*self.task_args)
        elif self.task_type == 'cut_video':
            self.cut_video(*self.task_args)
        elif self.task_type == 'audio_encode':
            self.audio_encode(*self.task_args)
        elif self.task_type == 'video_encode':
            self.video_encode(*self.task_args)
        elif self.task_type == 'accelerated_encode':
            self.accelerated_encode(*self.task_args)
        elif self.task_type == 'merge_video':
            self.merge_video(*self.task_args)
        elif self.task_type == 'concat_video':
            self.concat_video(*self.task_args)
        elif self.task_type =='merge_video_two':
            self.merge_video_two(*self.task_args)
        self.finished.emit()  # 任务完成，发出信号
        

    # 在这里可以添加更多任务类型的判断和调用
    def extract_video(self, input_folder, output_folder, start_time, end_time, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.extract_video_single(input_folder, output_folder, start_time, end_time, encoder, overwrite)
    def cut_video(self, input_folder, output_folder, start_time, end_time, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.cut_video(input_folder, output_folder, start_time, end_time, encoder, overwrite)
    def audio_encode(self, input_file, output_file, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.audio_encode(input_file, output_file, encoder, overwrite)
    def video_encode(self, input_file, output_file, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.video_encode(input_file, output_file, encoder, overwrite)
    def accelerated_encode(self, input_file, output_file, rate, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.accelerated_encode(input_file, output_file, rate, encoder, overwrite)
    def merge_video(self, input_files, output_file, op_file, ed_file, encoder, resolution='1920:1080', fps='30', overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.merge_video(input_files, output_file, op_file, ed_file, encoder, resolution, fps, overwrite)
    def merge_video_two(self, op_files, output_file, ed_file, encoder, resolution='1920:1080', fps='30', overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.merge_video_two(op_files, output_file, ed_file, encoder, resolution, fps, overwrite)
    def concat_video(self, input_files, output_file, op_file, ed_file, encoder, overwrite='-y'):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.concat_video(input_files, output_file, op_file, ed_file, encoder, overwrite)

        
# 继承自QThread的子类，用于后台执行任务的线程类
class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
    def run(self):
        self.worker.run_ffmpeg_task()

class VcodecpInterface(QWidget, Ui_VcodecpInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_variables()
        self.init_action()
        self.init_print()
        self.bind()
        # 必须给子界面设置全局唯一的对象名

    # Custom_encoder
    def change_custom_encoder(self, vcodec, vpreset, resolution, fps, acodec, apreset,):
        custom_encoder = f'{vcodec}{vpreset}{resolution}{fps}{acodec}{apreset}'
        return custom_encoder
    
    # Init_variables
    def init_variables(self):
        # file
        self.input_file_args = []
        self.output_file_args = []
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

        # 循环
        self.i = 0
        self.is_paused = False

    # Init_action
    def init_action(self):

        self.VcodecpIFlineEdit.setEnabled(False)  # 禁止修改分辨率
        resolution_list = ['1280x720', '1920x1080', '2560x1440', '3840x2160', '720x1280', '1080x1920']
        self.VcodecpIFlineEdit.addItems(resolution_list)  # 添加分辨率选项

        self.VcodecpIFlineEdit_2.setEnabled(False)  # 禁止修改帧率
        fps_list = ['30', '60', '24', '25', '50']
        self.VcodecpIFlineEdit_2.addItems(fps_list)  # 添加帧率选项

        self.VcodecpIFcomboBox_5.setEnabled(False)  # 禁止修改profile
        self.VcodecpIFdoubleSpinBox.setEnabled(False)  # 禁止修改加速倍率
        self.VcodecpIFradioButton.setChecked(True)  # 默认选择片尾时长

        VideoCodecs = ['libx264', 'copy', 'h264_nvenc', 'hevc_nvenc', 'vp9_nvenc', 'av1_nvenc', 'h264_amf', 'hevc_amf', 'vp9_amf', 'av1_amf', 'h264_qsv', 'hevc_qsv', 'vp9_qsv', 'av1_qsv', 'libx265']  # 视频编码器，包括显卡编码
        self.VcodecpIFlineEditVE.addItems(VideoCodecs)  # 添加视频编码器选项

        AudioCodecs = ['aac', 'copy', 'alac', 'flac', 'MP3', 'vorbis','opus']  # 音频编码器
        self.VcodecpIFlineEditAE.addItems(AudioCodecs)  # 添加音频编码器选项


    # Init_print
    def init_print(self):
        # Welcome message
        self.VcodecpIFconsole.appendPlainText("欢迎使用FFmpeg-python视频处理工具！")
        # encoder
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
        # 判断ffmpeg文件是否存在
        if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
            self.VcodecpIFconsole.appendPlainText("ffmpeg路径或ffprobe路径错误，请检查！")
            logging.error("ffmpeg or ffprobe error, please check the path!")
        else:
            self.VcodecpIFconsole.appendPlainText(f"ffmpeg初始化：{ffpath.ffmpeg_path}")
            self.VcodecpIFconsole.appendPlainText(f"ffprobe初始化：{ffpath.ffprobe_path}")
            logging.info(f"ffmpeg and ffprobe initialized successfully!")

    # Bind Event
    def bind(self):

        # Bind Button Event
        self.VcodecpIFinputfile.clicked.connect(self.select_input_file)
        self.VcodecpIFinputclear.clicked.connect(self.clear_input_file)
        self.VcodecpIFoutputfolder.clicked.connect(self.select_output_folder)
        self.VcodecpIFpushBtn.clicked.connect(self.encoding)
        self.VcodecpIFClearFil.clicked.connect(self.clear_filter_config)
        self.VcodecpIFpushButton_3.clicked.connect(self.select_op_file)
        self.VcodecpIFpushButton_4.clicked.connect(self.select_ed_file)
        self.VcodecpIFpushBtn_2.clicked.connect(self.unfreeze_config)

        # Check Event
        self.VcodecpIFcheckBox_2.clicked.connect(self.enable_resolution)
        self.VcodecpIFcheckBox_3.clicked.connect(self.enable_fps)
        self.VcodecpIFcheckBox.clicked.connect(self.enable_profile)
        self.VcodecpIFcheckBox_4.clicked.connect(self.enable_accelerated)

        # LineEdit/ComboBox/SpinBox Event
        self.VcodecpIFlineEdit.textChanged.connect(self.change_resolution)
        self.VcodecpIFlineEdit_2.textChanged.connect(self.change_fps)
        self.VcodecpIFlineEditVE.textChanged.connect(self.change_vcodec)
        self.VcodecpIFlineEditAE.textChanged.connect(self.change_acodec)
        self.VcodecpIFcomboBox_2.currentTextChanged.connect(self.change_vpreset)
        self.VcodecpIFcomboBox_3.currentTextChanged.connect(self.change_apreset)
        self.VcodecpIFspinBox.valueChanged.connect(self.change_bitrate)
        self.VcodecpIFspinBox_2.valueChanged.connect(self.change_quality)
        # self.VcodecpIFdoubleSpinBox.valueChanged.connect(self.change_accelerated)
        self.VcodecpIFcomboBox_5.currentTextChanged.connect(self.change_profile)



    
    #  File_operation
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

    

    # Custom encoding Config

    # resolution
    def enable_resolution(self):
        if self.VcodecpIFcheckBox_2.isChecked():
            self.VcodecpIFlineEdit.setEnabled(True)  # 允许修改分辨率
            self.resolution = f'-s {self.VcodecpIFlineEdit.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
        else:
            self.VcodecpIFlineEdit.setEnabled(False)  # 禁止修改分辨率
            self.resolution = ''
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    def change_resolution(self):
        if self.VcodecpIFcheckBox_2.isChecked():
            self.resolution = f'-s {self.VcodecpIFlineEdit.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)


    # fps
    def enable_fps(self):
        if self.VcodecpIFcheckBox_3.isChecked():
            self.VcodecpIFlineEdit_2.setEnabled(True)  # 允许修改帧率
            self.fps = f'-r {self.VcodecpIFlineEdit_2.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
        else:
            self.VcodecpIFlineEdit_2.setEnabled(False)  # 禁止修改帧率
            self.fps = ''
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    def change_fps(self):
        if self.VcodecpIFcheckBox_3.isChecked():
            self.fps = f'-r {self.VcodecpIFlineEdit_2.text()} '  # 结尾要有空格
            self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)


    # Video encoding Config
    def change_vpreset(self):
        self.quality = self.VcodecpIFspinBox_2.value()
        self.bitrate = self.VcodecpIFspinBox.value() * 1000
        if self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-medium' or self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-fast' or self.VcodecpIFcomboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.change_vpreset_sub(self.quality)
        else:
            self.change_vpreset_sub(self.bitrate)
    def change_vpreset_sub(self, rate):
        if self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-medium':
            self.vpreset = f'-preset medium -crf {rate} '
        elif self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-fast':
            self.vpreset = f'-preset fast -crf {rate} '
        elif self.VcodecpIFcomboBox_2.currentText() == 'CBR平均码率-medium':
            self.vpreset = f'-preset medium -b:v {rate} '
        elif self.VcodecpIFcomboBox_2.currentText() == 'CBR平均码率-fast':
            self.vpreset = f'-preset fast -b:v {rate} '
        elif self.VcodecpIFcomboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.vpreset = f'-preset medium -qp {rate} '
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    def change_vcodec(self):
        if self.VcodecpIFlineEditVE.text() != 'copy':
            self.vcodec = f'-vcodec {self.VcodecpIFlineEditVE.text()} '  # 结尾要有空格
            self.change_vpreset()
        else:
            self.vcodec = '-vcodec copy '
            self.vpreset = ''
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    def change_bitrate(self):
        if self.VcodecpIFcomboBox_2.currentText() == 'CBR平均码率-medium' or self.VcodecpIFcomboBox_2.currentText() == 'CBR平均码率-fast':
            self.bitrate = self.VcodecpIFspinBox.value() * 1000
            self.change_vpreset_sub(self.bitrate)
    def change_quality(self):
        if self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-medium' or self.VcodecpIFcomboBox_2.currentText() == 'CRF品质-fast' or self.VcodecpIFcomboBox_2.currentText() == 'CQP硬编品质(*qsv)':
            self.quality = self.VcodecpIFspinBox_2.value()
            self.change_vpreset_sub(self.quality)


    # Audio encoding Config
    def change_acodec(self):
        if self.VcodecpIFlineEditAE.text() != 'copy':
            self.acodec = f'-acodec {self.VcodecpIFlineEditAE.text()} '  # 结尾要有空格
            self.change_apreset()
        else:
            self.acodec = '-acodec copy '
            self.apreset = ''
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    def change_apreset(self):
        self.apreset = f'-b:a {self.VcodecpIFcomboBox_3.currentText()} '  # 结尾要有空格
        self.custom_encoder = self.change_custom_encoder(self.vcodec, self.vpreset, self.resolution, self.fps, self.acodec, self.apreset)
        self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    

    # Profile Config
    def enable_profile(self):
        if self.VcodecpIFcheckBox.isChecked():
            self.VcodecpIFcomboBox_5.setEnabled(True)  # 允许修改profile
            self.profile_changing()
        else:
            self.VcodecpIFcomboBox_5.setEnabled(False)  # 禁止修改profile
    def change_profile(self):
        if self.VcodecpIFcheckBox.isChecked() and self.VcodecpIFcomboBox_5.currentTextChanged():
            self.profile_changing()
    def profile_changing(self):
        if self.VcodecpIFcomboBox_5.currentText() == '默认':
            self.custom_encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k '
            self.VcodecpIFplainTextEdit.setPlainText(self.custom_encoder)
    
    # Accelerated Config
    def enable_accelerated(self):
        if self.VcodecpIFcheckBox_4.isChecked():
            self.VcodecpIFdoubleSpinBox.setEnabled(True)  # 允许修改加速倍率
        else:
            self.VcodecpIFdoubleSpinBox.setEnabled(False)  # 禁止修改加速倍率
    # def change_accelerated(self):
            



    # 简单转码任务
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

    # 加速转码任务
    def accelerated_encoding(self):
        input_file = self.input_file_args[self.i]
        output_file = self.output_file_args[self.i]
        if os.path.isfile(input_file) and self.VcodecpIFcheckBox_4.isChecked() and self.VcodecpIFdoubleSpinBox.value() != 1 and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_merge.isChecked():
            self.VcodecpIFconsole.appendPlainText("执行加速转码任务，请稍等...")
            self.worker = Worker('accelerated_encode', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, '%.2f'%self.VcodecpIFdoubleSpinBox.value(), self.VcodecpIFplainTextEdit.toPlainText())  # 开启子进程
            self.thread = WorkerThread(self.worker)
            self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}开始视频加速转码"))  # 线程开始时显示提示信息
            logging.info(f"Accelerated encoding task started, input file: {input_file}, output file: {output_file}")
            self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
            self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}完成视频加速转码"))  # 线程结束时显示提示信息
            logging.info(f"Accelerated encoding task finished, input file: {input_file}, output file: {output_file}")
            self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
            self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
            self.thread.start()  # 开始线程
        elif not os.path.isfile(input_file):
            MessageBox("错误", f"{input_file}不存在！", parent=self).exec()
            self.on_thread_finished()  #  进行下一个文件

    # 切割任务
    def extract_or_cut_video(self):
        input_file = self.input_file_args[self.i]
        output_file = self.output_file_args[self.i]
        if os.path.isfile(input_file) and not self.VcodecpIFcheckBox_4.isChecked() and not self.VcodecpIFcheckBox_merge.isChecked():
            if self.VcodecpIFtimeEdit_3.text() != '0:00:00:000' or self.VcodecpIFtimeEdit_2.text() != '0:00:00:000':
                # 如果选择了片尾时长，执行切割片尾模式
                if self.VcodecpIFradioButton.isChecked():
                    self.VcodecpIFconsole.appendPlainText("执行切割任务，请稍等...")
                    self.worker = Worker('extract_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, self.VcodecpIFtimeEdit_3.text(), self.VcodecpIFtimeEdit_2.text(), self.VcodecpIFplainTextEdit.toPlainText())  # 开启子进程
                    self.thread = WorkerThread(self.worker)
                    self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}开始视频切割"))  # 线程开始时显示提示信息
                    logging.info(f"Extract video task started, input file: {input_file}, output file: {output_file}")
                    self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
                    self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}完成视频切割"))  # 线程结束时显示提示信息
                    logging.info(f"Extract video task finished, input file: {input_file}, output file: {output_file}")
                    self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                    self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                    self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
                    self.thread.start()  # 开始线程
                # 如果选择了结束时间，执行时间段切割模式
                elif self.VcodecpIFradioButton_2.isChecked():
                    self.VcodecpIFconsole.appendPlainText("执行切割任务，请稍等...")
                    self.worker = Worker('cut_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, self.VcodecpIFtimeEdit_3.text(), self.VcodecpIFtimeEdit_2.text(), self.VcodecpIFplainTextEdit.toPlainText())  # 开启子进程
                    self.thread = WorkerThread(self.worker)
                    self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}开始视频切割"))  # 线程开始时显示提示信息
                    logging.info(f"Cut video task started, input file: {input_file}, output file: {output_file}")
                    self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
                    self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}完成视频切割"))  # 线程结束时显示提示信息
                    logging.info(f"Cut video task finished, input file: {input_file}, output file: {output_file}")
                    self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                    self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                    self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
                    self.thread.start()  # 开始线程
        elif not os.path.isfile(input_file):
            MessageBox("错误", f"{input_file}不存在！", parent=self).exec()
            self.on_thread_finished()  #  进行下一个文件


    # 合并任务
    def merge_or_concat_video(self):
        self.merge_input_file = self.input_file_args[self.i]
        self.merge_output_file = self.output_file_args[self.i]
        if  self.VcodecpIFcheckBox_merge.isChecked() and self.VcodecpIFtimeEdit_3.text() == '0:00:00:000' and self.VcodecpIFtimeEdit_2.text() == '0:00:00:000' and not self.VcodecpIFcheckBox_4.isChecked():
            if self.VcodecpIFpushButton_3.text() != '选择片头' and self.VcodecpIFpushButton_4.text() != '选择片尾':
                self.merge_3_videos()
            elif self.VcodecpIFpushButton_3.text() != '选择片头' and self.VcodecpIFpushButton_4.text() == '选择片尾':
                self.merge_2_videos(True)
            elif self.VcodecpIFpushButton_3.text() == '选择片头' and self.VcodecpIFpushButton_4.text() != '选择片尾':
                self.merge_2_videos(False)
            else:
                MessageBox("错误", "请选择合并方式！即选择片头或片尾！", parent=self).exec()
                self.debugflag_of_filter_config = False
                self.i = 0  # 循环计数器清零
            # else:
            #     self.VcodecpIFconsole.appendPlainText("执行合并任务，请稍等...")
            #     self.worker = Worker('concat_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, self.op_file, self.ed_file, r'vcodec=copy acodec=copy')  # 开启子进程
            #     self.thread = WorkerThread(self.worker)
            #     self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}开始视频合并"))  # 线程开始时显示提示信息
            #     logging.info(f"Merge video task started, input file: {input_file}, output file: {output_file}")
            #     self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
            #     self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{input_file}完成视频合并"))  # 线程结束时显示提示信息
            #     logging.info(f"Merge video task finished, input file: {input_file}, output file: {output_file}")
            #     self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            #     self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象                
            #     self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
            #     self.thread.start()  # 开始线程

    def select_op_file(self):
        self.op_file = QFileDialog.getOpenFileName(self, "选择片头文件", "", "媒体文件 (*.mp4 *.avi *.flv *.mkv *.wmv)")[0]
        self.VcodecpIFpushButton_3.setText(f'{os.path.basename(self.op_file)}')
    def select_ed_file(self):
        self.ed_file = QFileDialog.getOpenFileName(self, "选择片尾文件", "", "媒体文件 (*.mp4 *.avi *.flv *.mkv *.wmv)")[0]
        self.VcodecpIFpushButton_4.setText(f'{os.path.basename(self.ed_file)}')
    def merge_3_videos(self):
        if os.path.isfile(self.merge_input_file) and os.path.isfile(self.op_file) and os.path.isfile(self.ed_file):
            self.VcodecpIFconsole.appendPlainText("执行合并任务，请稍等...")
            if self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                self.worker = Worker('merge_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.op_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
            elif self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                self.worker = Worker('merge_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.op_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution)  # 开启子进程
            elif not self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                resolution = '1920:1080'  # 默认值
                self.worker = Worker('merge_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.op_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
            elif not self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                resolution = '1920:1080'  # 默认值
                fps = 30  # 默认值
                self.worker = Worker('merge_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.op_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, fps)  # 开启子进程
            self.thread = WorkerThread(self.worker)
            self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}开始视频合并"))  # 线程开始时显示提示信息
            logging.info(f"Merge video task started, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
            self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
            self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}完成视频合并"))  # 线程结束时显示提示信息
            logging.info(f"Merge video task finished, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
            self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
            self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
            self.thread.start()  # 开始线程
        elif not os.path.isfile(self.merge_input_file):
            MessageBox("input错误", f"{self.merge_input_file}不存在！", parent=self).exec()
            self.on_thread_finished()  #  进行下一个文件
        elif not os.path.isfile(self.op_file):
            MessageBox("op错误", f"{self.op_file}不存在！", parent=self).exec()
            self.debugflag_of_filter_config = False
            self.i = 0  # 循环计数器清零
        elif not os.path.isfile(self.ed_file):
            MessageBox("ed错误", f"{self.ed_file}不存在！", parent=self).exec()
            self.debugflag_of_filter_config = False
            self.i = 0  # 循环计数器清零
    def merge_2_videos(self, is_op):
        if is_op:
            if os.path.isfile(self.merge_input_file) and os.path.isfile(self.op_file):
                self.VcodecpIFconsole.appendPlainText("执行合并任务，请稍等...")
                if self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                    resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.op_file, self.merge_output_file, self.merge_input_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
                elif self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                    resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.op_file, self.merge_output_file, self.merge_input_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution)  # 开启子进程
                elif not self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                    resolution = '1920:1080'  # 默认值
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.op_file, self.merge_output_file, self.merge_input_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
                elif not self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                    resolution = '1920:1080'  # 默认值
                    fps = 30  # 默认值
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.op_file, self.merge_output_file, self.merge_input_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, fps)  # 开启子进程
                self.thread = WorkerThread(self.worker)
                self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}开始视频合并"))  # 线程开始时显示提示信息
                logging.info(f"Merge video task started, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
                self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
                self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}完成视频合并"))  # 线程结束时显示提示信息
                logging.info(f"Merge video task finished, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
                self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
                self.thread.start()  # 开始线程
            elif not os.path.isfile(self.merge_input_file):
                MessageBox("input错误", f"{self.merge_input_file}不存在！", parent=self).exec()
                self.on_thread_finished()  #  进行下一个文件
            elif not os.path.isfile(self.op_file):
                MessageBox("op错误", f"{self.op_file}不存在！", parent=self).exec()
                self.debugflag_of_filter_config = False
                self.i = 0  # 循环计数器清零
        elif not is_op:
            if os.path.isfile(self.merge_input_file) and os.path.isfile(self.ed_file):
                self.VcodecpIFconsole.appendPlainText("执行合并任务，请稍等...")
                if self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                    resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
                elif self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                    resolution = self.VcodecpIFlineEdit.text().replace('x', ':')  # 将resolution的x改为：
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution)  # 开启子进程
                elif not self.VcodecpIFcheckBox_2.isChecked() and self.VcodecpIFcheckBox_3.isChecked():
                    resolution = '1920:1080'  # 默认值
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, self.VcodecpIFlineEdit_2.text())  # 开启子进程
                elif not self.VcodecpIFcheckBox_2.isChecked() and not self.VcodecpIFcheckBox_3.isChecked():
                    resolution = '1920:1080'  # 默认值
                    fps = 30  # 默认值
                    self.worker = Worker('merge_video_two', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.merge_input_file, self.merge_output_file, self.ed_file, self.VcodecpIFplainTextEdit.toPlainText(), resolution, fps)  # 开启子进程
                self.thread = WorkerThread(self.worker)
                self.thread.started.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}开始视频合并"))  # 线程开始时显示提示信息
                logging.info(f"Merge video task started, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
                self.thread.started.connect(self.on_thread_started())  # 线程开始时启动子进程
                self.thread.finished.connect(lambda: self.VcodecpIFconsole.appendPlainText(f"{self.merge_input_file}完成视频合并"))  # 线程结束时显示提示信息
                logging.info(f"Merge video task finished, input file: {self.merge_input_file}, output file: {self.merge_output_file}")
                self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                self.thread.finished.connect(self.on_thread_finished)  # 线程结束时开启下一个线程
                self.thread.start()  # 开始线程
            elif not os.path.isfile(self.merge_input_file):
                MessageBox("input错误", f"{self.merge_input_file}不存在！", parent=self).exec()
                self.on_thread_finished()  #  进行下一个文件
            elif not os.path.isfile(self.ed_file):
                MessageBox("ed错误", f"{self.ed_file}不存在！", parent=self).exec()
                self.debugflag_of_filter_config = False
                self.i = 0  # 循环计数器清零




    def debug_of_filter_config(self):
        if self.VcodecpIFcheckBox_4.isChecked() and self.VcodecpIFcheckBox_merge.isChecked():
            if self.VcodecpIFtimeEdit_3.text() != '0:00:00:000' or self.VcodecpIFtimeEdit_2.text() != '0:00:00:000':
                MessageBox("警告", "请勿同时选择加速、切割选项和合并选项！", parent=self).exec()
                self.clear_filter_config()
            else:
                MessageBox("警告", "请勿同时选择加速和合并选项！", parent=self).exec()
                self.clear_filter_config()
        elif self.VcodecpIFcheckBox_4.isChecked():
            if self.VcodecpIFtimeEdit_3.text() != '0:00:00:000' or self.VcodecpIFtimeEdit_2.text() != '0:00:00:000':
                MessageBox("警告", "请勿同时选择滤镜选项！", parent=self).exec()
                self.clear_filter_config()
            else:
                self.debugflag_of_filter_config = True
        elif self.VcodecpIFcheckBox_merge.isChecked():
            if self.VcodecpIFtimeEdit_3.text() != '0:00:00:000' or self.VcodecpIFtimeEdit_2.text() != '0:00:00:000':
                MessageBox("警告", "请勿同时选择滤镜选项！", parent=self).exec()
                self.clear_filter_config()
            else:
                self.debugflag_of_filter_config = True
        else:
            self.debugflag_of_filter_config = True


    def clear_filter_config(self):
        self.VcodecpIFcheckBox_4.setChecked(False)
        self.VcodecpIFdoubleSpinBox.setEnabled(False)
        self.VcodecpIFcheckBox_merge.setChecked(False)
        self.VcodecpIFtimeEdit_3.setTime(QTime(0, 0, 0, 0))
        self.VcodecpIFtimeEdit_2.setTime(QTime(0, 0, 0, 0))
        self.op_file = ''
        self.ed_file = ''
        self.VcodecpIFpushButton_3.setText('选择片头')
        self.VcodecpIFpushButton_4.setText('选择片尾')
    

        # Encoding Config
    def encoding(self):
        self.debugflag_of_filter_config = False  # 调试模式
        self.debug_of_filter_config()
        if self.debugflag_of_filter_config:
            # 是否传入文件
            # 如果输入文件和输出文件都存在，则执行转码任务
            self.freeze_config('正在执行转码任务，请稍等...')
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
                    self.unfreeze_config()

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
    
    def on_thread_started(self):
        self.is_paused = True  # 开启暂停标志
        logging.info(f'线程创建，暂停循环，i={self.i}')
    def on_thread_finished(self):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        logging.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
        self.encoding()  # 开启下一个线程

    def freeze_config(self, text=''):
        self.VcodecpIFlineEditVE.setEnabled(False)  # 禁止修改视频编码器
        self.VcodecpIFlineEditAE.setEnabled(False)  # 禁止修改音频编码器
        self.VcodecpIFcomboBox_2.setEnabled(False)  # 禁止修改视频预设
        self.VcodecpIFcomboBox_3.setEnabled(False)  # 禁止修改音频预设
        self.VcodecpIFspinBox.setEnabled(False)  # 禁止修改视频码率
        self.VcodecpIFspinBox_2.setEnabled(False)  # 禁止修改视频品质
        self.VcodecpIFcomboBox_5.setEnabled(False)  # 禁止修改profile
        self.VcodecpIFdoubleSpinBox.setEnabled(False)  # 禁止修改加速倍率
        self.VcodecpIFpushBtn.setEnabled(False)  # 禁止开始转码
        self.VcodecpIFpushButton_3.setEnabled(False)  # 禁止选择切割起始时间
        self.VcodecpIFtimeEdit_3.setEnabled(False)  # 禁止选择切割结束时间
        self.VcodecpIFtimeEdit_2.setEnabled(False)  # 禁止enable修改分辨率
        self.VcodecpIFlineEdit.setEnabled(False)  # 禁止修改分辨率
        self.VcodecpIFlineEdit_2.setEnabled(False)  # 禁止修改帧率
        self.VcodecpIFcheckBox_3.setEnabled(False)  # 禁止enable修改帧率
        self.VcodecpIFcheckBox.setEnabled(False)  # 禁止enable修改profile
        self.VcodecpIFcheckBox_4.setEnabled(False)  # 禁止enable加速转码
        self.VcodecpIFcheckBox_merge.setEnabled(False)  # 禁止enable合并转码
        self.VcodecpIFradioButton.setEnabled(False)  # 禁止enable切割模式
        self.VcodecpIFradioButton_2.setEnabled(False)  # 禁止enable合并模式
        self.VcodecpIFClearFil.setEnabled(False)  # 禁止清除输入文件
        self.VcodecpIFpushButton_3.setEnabled(False)  # 禁止选择开头文件
        self.VcodecpIFpushButton_4.setEnabled(False)  # 禁止选择结尾文件
        self.VcodecpIFplainTextEdit.setEnabled(False)  # 禁止自定义编码参数
        logging.info(f"Freeze config. {text}")
        # self.VcodecpIFconsole.appendPlainText("冻结配置")
    def unfreeze_config(self):
        self.VcodecpIFlineEditVE.setEnabled(True)  # 解除禁止修改视频编码器
        self.VcodecpIFlineEditAE.setEnabled(True)  # 解除禁止修改音频编码器
        self.VcodecpIFcomboBox_2.setEnabled(True)  # 解除禁止修改视频预设
        self.VcodecpIFcomboBox_3.setEnabled(True)  # 解除禁止修改音频预设
        self.VcodecpIFspinBox.setEnabled(True)  # 解除禁止修改视频码率        
        self.VcodecpIFspinBox_2.setEnabled(True)  # 解除禁止修改视频品质
        self.VcodecpIFcomboBox_5.setEnabled(True)  # 解除禁止修改profile
        self.VcodecpIFdoubleSpinBox.setEnabled(True)  # 解除禁止修改加速倍率
        self.VcodecpIFpushBtn.setEnabled(True)  # 解除禁止开始转码
        self.VcodecpIFpushButton_3.setEnabled(True)  # 解除禁止选择切割起始时间
        self.VcodecpIFtimeEdit_3.setEnabled(True)  # 解除禁止选择切割结束时间
        self.VcodecpIFtimeEdit_2.setEnabled(True)  # 解除禁止enable修改分辨率
        self.VcodecpIFlineEdit.setEnabled(True)  # 解除禁止修改分辨率
        self.VcodecpIFlineEdit_2.setEnabled(True)  # 解除禁止修改帧率
        self.VcodecpIFcheckBox_3.setEnabled(True)  # 解除禁止enable修改帧率
        self.VcodecpIFcheckBox.setEnabled(True)  # 解除禁止enable修改profile
        self.VcodecpIFcheckBox_4.setEnabled(True)  # 解除禁止enable加速转码
        self.VcodecpIFcheckBox_merge.setEnabled(True)  # 解除禁止enable合并转码
        self.VcodecpIFradioButton.setEnabled(True)  # 解除禁止enable切割模式
        self.VcodecpIFradioButton_2.setEnabled(True)  # 解除禁止enable合并模式
        self.VcodecpIFClearFil.setEnabled(True)  # 解除禁止清除输入文件
        self.VcodecpIFpushButton_3.setEnabled(True)  # 解除禁止选择开头文件
        self.VcodecpIFpushButton_4.setEnabled(True)  # 解除禁止选择结尾文件
        self.VcodecpIFplainTextEdit.setEnabled(True)  # 禁止自定义编码参数
        logging.info("Unfreeze config.")
        # self.VcodecpIFconsole.appendPlainText("解除冻结配置")