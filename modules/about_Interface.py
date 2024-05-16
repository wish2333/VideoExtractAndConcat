import logging
import os
import configparser

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QListWidgetItem
from qfluentwidgets import FluentIcon

from modules.config import ffpath, set_config
from modules.Ui_aboutInterface import Ui_AboutInterface

class AboutInterface(QWidget, Ui_AboutInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_icons()
        self.bind()
        # 必须给子界面设置全局唯一的对象名

    def init_icons(self):
        self.AboutIFinputfile.setIcon(FluentIcon.GITHUB)
        # self.AboutIFinputclear.setIcon(FluentIcon.)
        # self.AboutIFoutputfolder.setIcon(FluentIcon.)

    # Bind Event
    def bind(self):

        # Bind Button Event
        self.AboutIFinputfile.clicked.connect(self.open_github)
        self.AboutIFinputclear.clicked.connect(self.open_bilibili)
        self.AboutIFoutputfolder.clicked.connect(self.open_blog)

        # Check Event
        

        # LineEdit/ComboBox/SpinBox Event

        
        # self.VcodecpIFdoubleSpinBox.valueChanged.connect(self.change_accelerated)
    
    def open_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/wish2333/VideoExtractAndConcat"))
    def open_bilibili(self):
        QDesktopServices.openUrl(QUrl("https://space.bilibili.com/18775396"))
    def open_blog(self):
        QDesktopServices.openUrl(QUrl("https://wish2333.github.io/zh/"))