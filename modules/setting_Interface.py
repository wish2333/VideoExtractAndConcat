from modules.logger_config import logger
import os
import configparser

from PySide6.QtCore import Qt, QThread, Signal, QObject, QTime
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QListWidgetItem
from qfluentwidgets import MessageBox

from modules.config import ffpath, autopath, set_config, set_auto_path
from modules.Ui_settingInterface import Ui_SettingInterface


# 打印初始化ffmpeg路径为：
# logger.info(f"初始化ffmpeg路径为：{ffpath.ffmpeg_path}")
# logger.info(f"初始化ffprobe路径为：{ffpath.ffprobe_path}")


class SettingInterface(QWidget, Ui_SettingInterface):

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
        # ffpath
        ffpath.ffmpeg_path = ffpath.ffmpeg_path
        ffpath.ffprobe_path = ffpath.ffprobe_path
        # ffpath.ffplay_path = ffpath.ffplay_path
        # autopath
        autopath.auto_path = autopath.auto_path

    # Init_action
    def init_action(self):
        self.SettingIFinputlist.clear()
        # 判断ffmpeg文件是否存在
        if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(
                ffpath.ffprobe_path)):
            self.SettingIFoutputfolder.setText("FFmpeg路径错误，请检查！")
        elif (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
            self.SettingIFoutputfolder.setText("FFmpeg路径检测通过")

        if os.path.isfile(ffpath.ffmpeg_path):
            self.SettingIFinputlist.addItem(ffpath.ffmpeg_path)
        else:
            self.SettingIFinputlist.addItem("ffmpeg路径错误，请检查！")

        if os.path.isfile(ffpath.ffprobe_path):
            self.SettingIFinputlist.addItem(ffpath.ffprobe_path)
        else:
            self.SettingIFinputlist.addItem("ffprobe路径错误，请检查！")

        # if os.path.isfile(ffpath.ffplay_path):
        #     self.SettingIFinputlist.addItem(ffpath.ffplay_path)
        # else:
        #     self.SettingIFinputlist.addItem("ffplay路径错误，请检查！")

        if os.path.isfile(autopath.auto_path):
            self.SettingIFlineEdit.setText(autopath.auto_path)
            self.SettingIFpushButton_2.setText('auto-editor路径检测通过')
        else:
            self.SettingIFlineEdit.setText("auto-editor路径错误，请检查！")
            self.SettingIFpushButton_2.setText('请检查')

    # Init_print
    def init_print(self):
        logger.debug("SettingInterface is initialized！")

    # Bind Event
    def bind(self):

        # Bind Button Event
        self.SettingIFinputfile.clicked.connect(self.set_ffmpeg_path)
        self.SettingIFoutputfolder.clicked.connect(self.set_ffmpeg_path)
        # self.SettingIFinputclear.clicked.connect(self.default_ffmpeg_path)

        self.SettingIFpushButton.clicked.connect(self.set_auto_path)

        # Check Event

        # LineEdit/ComboBox/SpinBox Event

        # self.VcodecpIFdoubleSpinBox.valueChanged.connect(self.change_accelerated)

    # Set ffmpeg path
    def set_ffmpeg_path(self):
        ffpath_folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "")
        if ffpath_folder:
            ffmpeg_path = os.path.join(ffpath_folder, "ffmpeg.exe")
            ffprobe_path = os.path.join(ffpath_folder, "ffprobe.exe")
            # ffplay_path = os.path.join(ffpath_folder, "ffplay.exe")
            set_config(ffmpeg_path, ffprobe_path)
            ffpath.reset(ffpath)
            self.init_variables()
            self.init_action()

    def set_auto_path(self):
        auto_path = QFileDialog.getOpenFileName(self, "选择auto-editor路径", "", "auto-editor.exe")[0]
        if auto_path:
            set_auto_path(auto_path)
            autopath.reset(autopath)
            self.init_variables()
            self.init_action()

    # def default_ffmpeg_path(self):
    #     ffpath.ffmpeg_path = ""
    #     ffpath.ffprobe_path = ""
    #     ffpath.ffplay_path = ""
    #     self.SettingIFinputlist.clear()

    # def unfreeze_default(self):
