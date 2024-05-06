from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Ui_VideoEditor import Ui_MainWindow
from ffmpegApi import FFmpeg
from config import ffpath

# 导入ffmpeg路径
init1 = print("初始化ffmpeg路径为：", ffpath.ffmpeg_path)
init2 = print("初始化ffprobe路径为：", ffpath.ffprobe_path)

# 主窗口类
class MainWindow(QMainWindow, Ui_MainWindow):
    # 初始化窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        # 打开控制台窗口
        # TODO：未完成
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
        if ffpath.ffmpeg_path:
            self.textEdit.append(f"ffmpeg路径修改为：{ffpath.ffmpeg_path}；{ffpath.ffprobe_path}")
            print(ffpath.ffmpeg_path)

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
        # 开始切割视频
        # 读取片头时间和片尾时间，以及编码格式
        start_time = self.time1.text()
        end_time = self.time2.text()
        encoder = self.line.text()
        if self.folder_path1 and self.folder1_path:
            # 实例化FFmpegApi
            ffmpeg_instance = FFmpeg(ffpath.ffmpeg_path)
            # 调用extract_video函数
            ffmpeg_instance.extract_video(self.folder_path1, start_time, end_time,self.folder1_path, encoder)
            self.textEdit.append("视频切割完成")
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
        if self.folder_path2 and self.file1_path and self.file2_path and self.folder2_path:
            # 实例化FFmpegApi
            ffmpeg_instance = FFmpeg(ffpath.ffmpeg_path)
            # 调用merge_video函数
            ffmpeg_instance.merge_video(self.folder_path2, self.file1_path, self.file2_path, self.folder2_path, encoder)
            self.textEdit.append("视频合并完成")
        else:
            self.textEdit.append("合并：请先输入视频文件夹")

    

# 运行窗口程序
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()  # 创建窗口对象
    window.show()  # 显示窗口
    app.exec_()  # 运行程序