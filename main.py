import sys
import logging
# 第三方库
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import FluentWindow, FluentIcon
# 自定义模块
from modules.venco_Interface import VencoInterface

# 初始化logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建一个文件处理器并设置级别、文件名和编码
file_handler = logging.FileHandler('log.txt', mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# 将处理器添加到日志记录器
logger.addHandler(file_handler)
# 记录日志
logger.info("logger initialized")

class mainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venco Interface")  # 设置窗口标题
        # self.setWindowIcon(QIcon("icon.png"))  # 设置窗口图标
        self.resize(1280, 720)  # 设置窗口大小
        self.navigationInterface.setExpandWidth(200)  # 设置导航栏宽度
        # 添加VencoInterface子界面
        self.vencoInterface = VencoInterface(self)  # 实例化VencoInterface子界面
        self.addSubInterface(self.vencoInterface, FluentIcon.RINGER, "Venco Interface")  # 添加子界面到主界面



if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()