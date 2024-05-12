import sys
import logging
# 第三方库
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import FluentWindow, FluentIcon
# 自定义模块
from modules.vcodec_Interface import VcodecInterface
from modules.vcodecp_Interface import VcodecpInterface

# 初始化logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建一个文件处理器并设置级别、文件名和编码
file_handler = logging.FileHandler(r'log/log.txt', mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# 将处理器添加到日志记录器
logger.addHandler(file_handler)
# 记录日志
logger.info("logger initialized")

class mainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.init_windows()
        self.init_widget()
        self.init_navigation()

        
    def init_windows(self):
        self.resize(1280, 720)  # 设置窗口大小
        self.navigationInterface.setExpandWidth(200)  # 设置导航栏宽度
        self.setWindowTitle("VideoExtractAndConcat")  # 设置窗口标题

    def init_widget(self):
        self.homeInterface = VcodecInterface(self)
        self.videoInterface = VcodecpInterface(self)

    def init_navigation(self):
        self.addSubInterface(self.homeInterface, FluentIcon.HOME, "Home")
        self.addSubInterface(self.videoInterface, FluentIcon.VIDEO, "Video")

        # self.navigationInterface.addSeparator()

        # self.addSubInterface(self.settingInterface, FluentIcon.SETTINGS, "Setting")





if __name__ == '__main__':
    # enable dpi scale
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()