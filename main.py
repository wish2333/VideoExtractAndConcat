from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QThread, Signal, QObject
from qt_material import apply_stylesheet

import os
import sys
import logging

from Ui_VideoEditor import Ui_MainWindow
from ffmpegApi import FFmpeg
from config import ffpath

# 初始化logger
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    filename='log.txt', 
    filemode='w', 
    encoding='utf-8'
)
# 添加一个StreamHandler用于控制台输出（可选）
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(console_handler)
logging.info("logger initialized")

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
        elif self.task_type =='merge_video':
            self.merge_video(*self.task_args)
        self.finished.emit()  # 任务完成，发出信号

    # 在这里可以添加更多任务类型的判断和调用
    def extract_video(self, input_folder, start_time, end_time, output_folder, encoder, overwrite):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.extract_video(input_folder, start_time, end_time, output_folder, encoder, overwrite)
    def merge_video(self, input_folder, file1, file2, output_folder, encoder, overwrite):
        ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
        ffmpeg_instance.merge_video(input_folder, file1, file2, output_folder, encoder, overwrite)
        
# 继承自QThread的子类，用于后台执行任务的线程类
class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    def run(self):
        self.worker.run_ffmpeg_task()

# 主窗口类
class MainWindow(QMainWindow, Ui_MainWindow):
    # 初始化窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        self.init_print()

    # 初始化打印
    def init_print(self):
        self.textEdit.append("欢迎使用FFmpeg-python视频处理工具！")
        self.textEdit.append(f"ffmpeg初始化：{ffpath.ffmpeg_path}")
        self.textEdit.append(f"ffprobe初始化：{ffpath.ffprobe_path}")
        # 判断ffmpeg文件是否存在
        if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
            self.textEdit.append("ffmpeg路径或ffprobe路径错误，请检查！")

    # 绑定事件槽
    def bind(self):
        # 设置按钮的信号槽
        self.importBn1.clicked.connect(self.import_video_folder1)
        self.importBn2.clicked.connect(self.import_video_file1)
        self.importBn3.clicked.connect(self.import_video_file2)
        self.importBn4.clicked.connect(self.import_video_folder2)
        self.exportBn1.clicked.connect(self.export_video_folder1)
        self.exportBn2.clicked.connect(self.export_video_folder2)
        self.pushButton1.clicked.connect(self.process_extract)
        self.pushButton2.clicked.connect(self.process_concat)
        self.pushButtonF.clicked.connect(self.adjust_ffmpeg_path)

    # 调整ffmpeg路径
    def adjust_ffmpeg_path(self):
        ffmpeg_folder = QFileDialog.getExistingDirectory(
            self, "选择bin文件夹", "./")
        ffpath.ffmpeg_path = f"{ffmpeg_folder}\\ffmpeg.exe"
        ffpath.ffprobe_path = f"{ffmpeg_folder}\\ffprobe.exe"
        # 检查ffmpeg文件是否存在
        if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
            self.textEdit.append("ffmpeg路径或ffprobe路径错误，请检查！")
            return
        else:
            self.textEdit.append(f"ffmpeg路径修改为：{ffpath.ffmpeg_path}")
            self.textEdit.append(f"ffprobe路径修改为：{ffpath.ffprobe_path}")

    # 切割流程
    # 点击导入视频文件夹按钮，弹出文件选择对话框，选择视频文件夹，选择完成后显示在文本框中
    def import_video_folder1(self):
        self.folder_path1 = QFileDialog.getExistingDirectory(
            self, "选择视频文件夹", "./")
        if self.folder_path1:
            self.textEdit.append(f"切割：输入文件夹为{self.folder_path1}")
    # 点击导出切割文件夹按钮，弹出文件选择对话框，选择文件夹，选择完成后显示在文本框中
    def export_video_folder1(self):
        self.folder1_path = QFileDialog.getExistingDirectory(
            self, "选择导出文件夹", "./")
        if self.folder1_path:
            self.textEdit.append(f"切割：输出文件夹为{self.folder1_path}")
    # 点击切割按钮，调用FFmpegApi的extract_video函数，切割视频
    def process_extract(self):
        # 检测程序是否输入了视频文件夹
        if not hasattr(self, 'folder_path1'):
            self.textEdit.append("切割：请先输入视频文件夹")
            return
        if not hasattr(self, 'folder1_path'):
            self.textEdit.append("切割：请先输入视频文件夹")
            return
        # 读取片头时间和片尾时间，以及编码格式
        start_time = self.time1.text()
        end_time = self.time2.text()
        encoder = self.line.text()
        # overwrite = self.checkBox.isChecked()
        # 开始切割视频
        if self.folder_path1 and self.folder1_path:
            # 创建Worker实例
            self.worker = Worker('extract_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.folder_path1, start_time, end_time, self.folder1_path, encoder, '-y')
            # 实例化WorkerThread
            self.thread = WorkerThread(self.worker)
            self.thread.started.connect(lambda: self.textEdit.append("开始切割视频"))  # 线程开始时显示提示信息
            self.thread.finished.connect(lambda: self.textEdit.append("视频切割完成"))  # 线程结束时显示提示信息
            self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
            self.thread.start()  # 开始线程
        else:
            self.textEdit.append("切割：请先输入视频文件夹")
    
    # 合并流程
    # 点击导入视频文件夹按钮，弹出文件选择对话框，选择视频文件夹，选择完成后显示在文本框中
    def import_video_folder2(self):
        self.folder_path2 = QFileDialog.getExistingDirectory(
            self, "选择视频文件夹", "./")
        if self.folder_path2:
            self.textEdit.append(f"合并：输入文件夹为{self.folder_path2}")
    # 点击导入片头视频文件按钮，弹出文件选择对话框，选择视频文件，选择完成后添加到文本框中且不覆盖前面的文字内容
    def import_video_file1(self):
        self.file1_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "./", "视频文件 (*.mp4)")
        if self.file1_path:
            self.textEdit.append(f"合并：输入片头文件为{self.file1_path}")

    # 点击导入片尾视频文件按钮，弹出文件选择对话框，选择视频文件，选择完成后添加到文本框中且不覆盖前面的文字内容
    def import_video_file2(self):
        self.file2_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "./", "视频文件 (*.mp4)")
        if self.file2_path:
            self.textEdit.append(f"合并：输入片尾文件为{self.file2_path}")

    # 点击导出合并文件夹按钮，弹出文件选择对话框，选择文件夹，选择完成后显示在文本框中
    def export_video_folder2(self):
        self.folder2_path = QFileDialog.getExistingDirectory(
            self, "选择导出文件夹", "./")
        if self.folder2_path:
            self.textEdit.append(f"合并：输出文件夹为{self.folder2_path}")
    # 点击开始合并按钮，调用FFmpegApi的merge_video函数，合并视频
    def process_concat(self):
        # 检测程序是否输入了视频文件夹
        if not hasattr(self, 'folder_path2'):
            self.textEdit.append("合并：请先输入视频文件夹")
            return
        if not hasattr(self, 'file1_path'):
            self.textEdit.append("合并：请先输入片头视频文件")
            return
        if not hasattr(self, 'file2_path'):
            self.textEdit.append("合并：请先输入片尾视频文件")
            return
        if not hasattr(self, 'folder2_path'):
            self.textEdit.append("合并：请先输入导出文件夹")
            return
        # 开始合并视频
        # 读取片头时间和片尾时间，以及编码格式
        encoder = self.line2.text()
        # overwrite = self.checkBox2.isChecked()
        if self.folder_path2 and self.file1_path and self.file2_path and self.folder2_path:
            # 创建Worker实例
            self.worker = Worker('merge_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.folder_path2, self.file1_path, self.file2_path, self.folder2_path, encoder, '-y')
            # 实例化WorkerThread
            self.thread = WorkerThread(self.worker)
            self.thread.started.connect(lambda: self.textEdit.append("开始合并视频"))  # 线程开始时显示提示信息
            self.thread.finished.connect(lambda: self.textEdit.append("视频合并完成"))  # 线程结束时显示提示信息
            self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
            self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
            self.thread.start()  # 开始线程
        else:
            self.textEdit.append("合并：请先输入视频文件夹")

    

# 运行窗口程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()  # 创建窗口对象
    apply_stylesheet(app, theme='dark_blue.xml')
    window.show()  # 显示窗口
    app.exec()  # 运行程序