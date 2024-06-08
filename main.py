import sys
# import logging
import os
# 第三方库
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import FluentWindow, FluentIcon, NavigationItemPosition
# 自定义模块
from modules.logger_config import logger
from modules.setting_Interface import SettingInterface
from modules.vcodecp_Interface import VcodecpInterface
from modules.vcodec_Interface import VcodecInterface
from modules.remuxInterface import RemuxInterface
from modules.VfilterInterface import VfilterInterface
from modules.VautocutInterface import VautocutInterface
from modules.about_Interface import AboutInterface
from modules.config import init_ffpath, init_autopath



# # 初始化logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# # 创建一个文件处理器并设置级别、文件名和编码
# if os.path.exists(r'log') == False:
#     os.mkdir(r'log')
# file_handler = logging.handlers.RotatingFileHandler(r'log/log.txt', mode='a', encoding='utf-8', maxBytes=1024 * 1024 * 5, backupCount=5)
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(logging.Formatter('%(asctime)s-%(name)s-%(levelname)s - %(message)s'))
# # 创建一个控制台处理器并设置级别
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
# # 将处理器添加到日志记录器
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
# 记录日志
logger.info("logger initialized")
logger.debug("This should be written to log.txt only")

class mainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.init_windows()
        self.init_widget()
        self.init_navigation()
        self.init_config()
        
    def init_windows(self):
        self.resize(1280, 720)  # 设置窗口大小
        self.navigationInterface.setExpandWidth(250)  # 设置导航栏宽度
        self.setWindowTitle("VideoExtractAndConcat")  # 设置窗口标题

    def init_widget(self):
        self.siglevideoInterface = VcodecInterface(self)
        self.videoInterface = VcodecpInterface(self)
        self.remuxInterface = RemuxInterface(self)
        self.VfilterInterface = VfilterInterface(self)
        self.VautocutInterface = VautocutInterface(self)
        self.SettingInterface = SettingInterface(self)
        self.AboutInterface = AboutInterface(self)

    def init_navigation(self):
        
        self.addSubInterface(self.videoInterface, FluentIcon.HOME, "    Home")
        self.addSubInterface(self.siglevideoInterface, FluentIcon.VIDEO, "    Single Video")
        self.addSubInterface(self.remuxInterface, FluentIcon.FILTER, "    Remux")
        self.addSubInterface(self.VfilterInterface, FluentIcon.TRANSPARENT, "    Video Filter")

        self.navigationInterface.addSeparator()
        self.addSubInterface(self.VautocutInterface, FluentIcon.CODE, "    Autocut")

        self.addSubInterface(self.AboutInterface, FluentIcon.INFO, "    About", NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.SettingInterface, FluentIcon.SETTING, "    Setting", NavigationItemPosition.BOTTOM)

    def init_config(self):
        init_ffpath()
        init_autopath()
        self.SettingInterface.init_action()




if __name__ == '__main__':
    # enable dpi scale
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()