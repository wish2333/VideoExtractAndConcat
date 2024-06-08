# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (ListWidget, PlainTextEdit, PushButton, ScrollArea)

class Ui_SettingInterface(object):
    def setupUi(self, SettingInterface):
        if not SettingInterface.objectName():
            SettingInterface.setObjectName(u"SettingInterface")
        SettingInterface.resize(1089, 757)
        SettingInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(SettingInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SettingIFscrollArea = ScrollArea(SettingInterface)
        self.SettingIFscrollArea.setObjectName(u"SettingIFscrollArea")
        self.SettingIFscrollArea.setMinimumSize(QSize(760, 0))
        self.SettingIFscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.SettingIFscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.SettingIFscrollArea.setWidgetResizable(True)
        self.SettingIFfacescrollAreaWidgetContents = QWidget()
        self.SettingIFfacescrollAreaWidgetContents.setObjectName(u"SettingIFfacescrollAreaWidgetContents")
        self.SettingIFfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1071, 739))
        self.verticalLayout_3 = QVBoxLayout(self.SettingIFfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SettingIFbox01 = QHBoxLayout()
        self.SettingIFbox01.setSpacing(20)
        self.SettingIFbox01.setObjectName(u"SettingIFbox01")
        self.SettingIFbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.SettingIFverticalLayout_4 = QVBoxLayout()
        self.SettingIFverticalLayout_4.setObjectName(u"SettingIFverticalLayout_4")
        self.SettingIFverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.SettingIFTitle1 = QLabel(self.SettingIFfacescrollAreaWidgetContents)
        self.SettingIFTitle1.setObjectName(u"SettingIFTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SettingIFTitle1.sizePolicy().hasHeightForWidth())
        self.SettingIFTitle1.setSizePolicy(sizePolicy)
        self.SettingIFTitle1.setMaximumSize(QSize(100, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.SettingIFTitle1.setFont(font)

        self.SettingIFverticalLayout_4.addWidget(self.SettingIFTitle1)

        self.SettingIFTitle2 = QLabel(self.SettingIFfacescrollAreaWidgetContents)
        self.SettingIFTitle2.setObjectName(u"SettingIFTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SettingIFTitle2.sizePolicy().hasHeightForWidth())
        self.SettingIFTitle2.setSizePolicy(sizePolicy1)
        self.SettingIFTitle2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.SettingIFTitle2.setFont(font1)

        self.SettingIFverticalLayout_4.addWidget(self.SettingIFTitle2)


        self.SettingIFbox01.addLayout(self.SettingIFverticalLayout_4)

        self.Settinglabel = QLabel(self.SettingIFfacescrollAreaWidgetContents)
        self.Settinglabel.setObjectName(u"Settinglabel")
        self.Settinglabel.setMaximumSize(QSize(16777215, 80))

        self.SettingIFbox01.addWidget(self.Settinglabel)

        self.SettingIFhorizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.SettingIFbox01.addItem(self.SettingIFhorizontalSpacer)


        self.verticalLayout_3.addLayout(self.SettingIFbox01)

        self.SettingIFbox02 = QFrame(self.SettingIFfacescrollAreaWidgetContents)
        self.SettingIFbox02.setObjectName(u"SettingIFbox02")
        self.SettingIFbox02.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SettingIFbox02.sizePolicy().hasHeightForWidth())
        self.SettingIFbox02.setSizePolicy(sizePolicy2)
        self.SettingIFbox02.setMinimumSize(QSize(480, 145))
        self.SettingIFbox02.setMaximumSize(QSize(16777215, 240))
        self.SettingIFbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.SettingIFbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.SettingIFbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SettingIFinputfile = PushButton(self.SettingIFbox02)
        self.SettingIFinputfile.setObjectName(u"SettingIFinputfile")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.SettingIFinputfile.setFont(font2)

        self.gridLayout.addWidget(self.SettingIFinputfile, 0, 0, 1, 1)

        self.SettingIFinputclear = PushButton(self.SettingIFbox02)
        self.SettingIFinputclear.setObjectName(u"SettingIFinputclear")
        self.SettingIFinputclear.setFont(font2)

        self.gridLayout.addWidget(self.SettingIFinputclear, 0, 1, 1, 1)

        self.SettingIFoutputfolder = QPushButton(self.SettingIFbox02)
        self.SettingIFoutputfolder.setObjectName(u"SettingIFoutputfolder")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.SettingIFoutputfolder.setFont(font3)

        self.gridLayout.addWidget(self.SettingIFoutputfolder, 0, 2, 1, 1)

        self.SettingIFinputlist = ListWidget(self.SettingIFbox02)
        self.SettingIFinputlist.setObjectName(u"SettingIFinputlist")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SettingIFinputlist.sizePolicy().hasHeightForWidth())
        self.SettingIFinputlist.setSizePolicy(sizePolicy3)
        self.SettingIFinputlist.setMinimumSize(QSize(0, 120))
        self.SettingIFinputlist.setMaximumSize(QSize(16777215, 200))
        self.SettingIFinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.SettingIFinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.SettingIFinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.SettingIFinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.SettingIFinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.SettingIFbox02)

        self.SettingIFbox03 = QHBoxLayout()
        self.SettingIFbox03.setObjectName(u"SettingIFbox03")
        self.SettingIFframe = QFrame(self.SettingIFfacescrollAreaWidgetContents)
        self.SettingIFframe.setObjectName(u"SettingIFframe")
        self.SettingIFframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.SettingIFframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.SettingIFframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SettingIFpushButton = QPushButton(self.SettingIFframe)
        self.SettingIFpushButton.setObjectName(u"SettingIFpushButton")
        self.SettingIFpushButton.setMinimumSize(QSize(0, 30))
        self.SettingIFpushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.SettingIFpushButton)

        self.SettingIFlineEdit = QLineEdit(self.SettingIFframe)
        self.SettingIFlineEdit.setObjectName(u"SettingIFlineEdit")
        font4 = QFont()
        font4.setPointSize(12)
        self.SettingIFlineEdit.setFont(font4)

        self.horizontalLayout.addWidget(self.SettingIFlineEdit)

        self.SettingIFpushButton_2 = QPushButton(self.SettingIFframe)
        self.SettingIFpushButton_2.setObjectName(u"SettingIFpushButton_2")
        self.SettingIFpushButton_2.setFont(font4)

        self.horizontalLayout.addWidget(self.SettingIFpushButton_2)


        self.SettingIFbox03.addWidget(self.SettingIFframe)


        self.verticalLayout_3.addLayout(self.SettingIFbox03)

        self.SettingIFbox04 = QHBoxLayout()
        self.SettingIFbox04.setObjectName(u"SettingIFbox04")

        self.verticalLayout_3.addLayout(self.SettingIFbox04)

        self.SettingIFconsole = PlainTextEdit(self.SettingIFfacescrollAreaWidgetContents)
        self.SettingIFconsole.setObjectName(u"SettingIFconsole")
        sizePolicy2.setHeightForWidth(self.SettingIFconsole.sizePolicy().hasHeightForWidth())
        self.SettingIFconsole.setSizePolicy(sizePolicy2)
        self.SettingIFconsole.setMinimumSize(QSize(640, 160))
        self.SettingIFconsole.setMaximumSize(QSize(6400, 300))
        self.SettingIFconsole.setUndoRedoEnabled(False)
        self.SettingIFconsole.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.SettingIFconsole.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.SettingIFconsole)

        self.SettingIFscrollArea.setWidget(self.SettingIFfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SettingIFscrollArea)


        self.retranslateUi(SettingInterface)

        QMetaObject.connectSlotsByName(SettingInterface)
    # setupUi

    def retranslateUi(self, SettingInterface):
        SettingInterface.setWindowTitle(QCoreApplication.translate("SettingInterface", u"Form", None))
        self.SettingIFTitle1.setText(QCoreApplication.translate("SettingInterface", u"\u8bbe\u7f6e", None))
        self.SettingIFTitle2.setText(QCoreApplication.translate("SettingInterface", u"FFmpeg", None))
        self.Settinglabel.setText(QCoreApplication.translate("SettingInterface", u"\u8f6f\u4ef6\u7684\u5168\u5c40\u8bbe\u7f6e", None))
        self.SettingIFinputfile.setText(QCoreApplication.translate("SettingInterface", u"\u8bbe\u7f6eFFmpeg\u8def\u5f84", None))
        self.SettingIFinputclear.setText(QCoreApplication.translate("SettingInterface", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.SettingIFoutputfolder.setText(QCoreApplication.translate("SettingInterface", u"FFmpeg\u8def\u5f84\u68c0\u6d4b\u901a\u8fc7", None))
        self.SettingIFpushButton.setText(QCoreApplication.translate("SettingInterface", u"\u8bbe\u7f6eauto-editor\u8def\u5f84", None))
        self.SettingIFpushButton_2.setText(QCoreApplication.translate("SettingInterface", u"auto-editor\u8def\u5f84\u68c0\u6d4b\u901a\u8fc7", None))
    # retranslateUi

