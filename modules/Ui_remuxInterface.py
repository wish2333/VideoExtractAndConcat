# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remuxInterface.ui'
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
    QHBoxLayout, QLabel, QLayout, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, ListWidget, PrimaryPushButton, PushButton,
    ScrollArea)

class Ui_remuxInterface(object):
    def setupUi(self, remuxInterface):
        if not remuxInterface.objectName():
            remuxInterface.setObjectName(u"remuxInterface")
        remuxInterface.resize(1085, 642)
        remuxInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(remuxInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.remuxIFscrollArea = ScrollArea(remuxInterface)
        self.remuxIFscrollArea.setObjectName(u"remuxIFscrollArea")
        self.remuxIFscrollArea.setMinimumSize(QSize(760, 0))
        self.remuxIFscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.remuxIFscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.remuxIFscrollArea.setWidgetResizable(True)
        self.remuxIFfacescrollAreaWidgetContents = QWidget()
        self.remuxIFfacescrollAreaWidgetContents.setObjectName(u"remuxIFfacescrollAreaWidgetContents")
        self.remuxIFfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1067, 624))
        self.verticalLayout_3 = QVBoxLayout(self.remuxIFfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.remuxIFbox01 = QHBoxLayout()
        self.remuxIFbox01.setSpacing(20)
        self.remuxIFbox01.setObjectName(u"remuxIFbox01")
        self.remuxIFbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.remuxIFverticalLayout_4 = QVBoxLayout()
        self.remuxIFverticalLayout_4.setObjectName(u"remuxIFverticalLayout_4")
        self.remuxIFverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.remuxIFTitle1 = QLabel(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxIFTitle1.setObjectName(u"remuxIFTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remuxIFTitle1.sizePolicy().hasHeightForWidth())
        self.remuxIFTitle1.setSizePolicy(sizePolicy)
        self.remuxIFTitle1.setMaximumSize(QSize(120, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.remuxIFTitle1.setFont(font)

        self.remuxIFverticalLayout_4.addWidget(self.remuxIFTitle1)

        self.remuxIFTitle2 = QLabel(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxIFTitle2.setObjectName(u"remuxIFTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.remuxIFTitle2.sizePolicy().hasHeightForWidth())
        self.remuxIFTitle2.setSizePolicy(sizePolicy1)
        self.remuxIFTitle2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.remuxIFTitle2.setFont(font1)

        self.remuxIFverticalLayout_4.addWidget(self.remuxIFTitle2)


        self.remuxIFbox01.addLayout(self.remuxIFverticalLayout_4)

        self.remuxlabel = QLabel(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxlabel.setObjectName(u"remuxlabel")
        self.remuxlabel.setMaximumSize(QSize(16777215, 80))

        self.remuxIFbox01.addWidget(self.remuxlabel)

        self.remuxIFhorizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.remuxIFbox01.addItem(self.remuxIFhorizontalSpacer)

        self.remuxIFpushBtn = PrimaryPushButton(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxIFpushBtn.setObjectName(u"remuxIFpushBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.remuxIFpushBtn.sizePolicy().hasHeightForWidth())
        self.remuxIFpushBtn.setSizePolicy(sizePolicy2)
        self.remuxIFpushBtn.setMinimumSize(QSize(240, 60))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        self.remuxIFpushBtn.setFont(font2)
        self.remuxIFpushBtn.setFlat(False)

        self.remuxIFbox01.addWidget(self.remuxIFpushBtn)

        self.remuxIFSTBtn = QPushButton(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxIFSTBtn.setObjectName(u"remuxIFSTBtn")
        self.remuxIFSTBtn.setMinimumSize(QSize(120, 60))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.remuxIFSTBtn.setFont(font3)

        self.remuxIFbox01.addWidget(self.remuxIFSTBtn)


        self.verticalLayout_3.addLayout(self.remuxIFbox01)

        self.remuxIFbox02 = QFrame(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxIFbox02.setObjectName(u"remuxIFbox02")
        self.remuxIFbox02.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.remuxIFbox02.sizePolicy().hasHeightForWidth())
        self.remuxIFbox02.setSizePolicy(sizePolicy3)
        self.remuxIFbox02.setMinimumSize(QSize(480, 145))
        self.remuxIFbox02.setMaximumSize(QSize(16777215, 240))
        self.remuxIFbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.remuxIFbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.remuxIFbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.remuxIFinputfile = PushButton(self.remuxIFbox02)
        self.remuxIFinputfile.setObjectName(u"remuxIFinputfile")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.remuxIFinputfile.setFont(font4)

        self.gridLayout.addWidget(self.remuxIFinputfile, 0, 0, 1, 1)

        self.remuxIFoutputfolder = QPushButton(self.remuxIFbox02)
        self.remuxIFoutputfolder.setObjectName(u"remuxIFoutputfolder")
        self.remuxIFoutputfolder.setFont(font4)

        self.gridLayout.addWidget(self.remuxIFoutputfolder, 0, 2, 1, 1)

        self.remuxIFinputclear = PushButton(self.remuxIFbox02)
        self.remuxIFinputclear.setObjectName(u"remuxIFinputclear")
        self.remuxIFinputclear.setFont(font4)

        self.gridLayout.addWidget(self.remuxIFinputclear, 0, 1, 1, 1)

        self.remuxIFinputlist = ListWidget(self.remuxIFbox02)
        self.remuxIFinputlist.setObjectName(u"remuxIFinputlist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.remuxIFinputlist.sizePolicy().hasHeightForWidth())
        self.remuxIFinputlist.setSizePolicy(sizePolicy4)
        self.remuxIFinputlist.setMinimumSize(QSize(0, 120))
        self.remuxIFinputlist.setMaximumSize(QSize(16777215, 200))
        self.remuxIFinputlist.setAcceptDrops(True)
        self.remuxIFinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.remuxIFinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.remuxIFinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.remuxIFinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.remuxIFinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.remuxIFbox02)

        self.remuxIFbox04 = QHBoxLayout()
        self.remuxIFbox04.setObjectName(u"remuxIFbox04")
        self.remuxframe = QFrame(self.remuxIFfacescrollAreaWidgetContents)
        self.remuxframe.setObjectName(u"remuxframe")
        self.remuxframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.remuxframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.remuxframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.remuxhorizontalLayout = QHBoxLayout()
        self.remuxhorizontalLayout.setObjectName(u"remuxhorizontalLayout")
        self.remuxhorizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.remuxcomboBox = ComboBox(self.remuxframe)
        self.remuxcomboBox.addItem("")
        self.remuxcomboBox.addItem("")
        self.remuxcomboBox.addItem("")
        self.remuxcomboBox.addItem("")
        self.remuxcomboBox.setObjectName(u"remuxcomboBox")
        self.remuxcomboBox.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setPointSize(12)
        self.remuxcomboBox.setFont(font5)

        self.remuxhorizontalLayout.addWidget(self.remuxcomboBox)

        self.remuxpushButton = PushButton(self.remuxframe)
        self.remuxpushButton.setObjectName(u"remuxpushButton")
        self.remuxpushButton.setMinimumSize(QSize(0, 30))
        self.remuxpushButton.setFont(font5)

        self.remuxhorizontalLayout.addWidget(self.remuxpushButton)


        self.verticalLayout_2.addLayout(self.remuxhorizontalLayout)

        self.remuxhorizontalLayout_2 = QHBoxLayout()
        self.remuxhorizontalLayout_2.setObjectName(u"remuxhorizontalLayout_2")
        self.remuxhorizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.remuxpushButton_2 = PushButton(self.remuxframe)
        self.remuxpushButton_2.setObjectName(u"remuxpushButton_2")
        self.remuxpushButton_2.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_2.setFont(font5)

        self.remuxhorizontalLayout_2.addWidget(self.remuxpushButton_2)

        self.remuxpushButton_3 = PushButton(self.remuxframe)
        self.remuxpushButton_3.setObjectName(u"remuxpushButton_3")
        self.remuxpushButton_3.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_3.setFont(font5)

        self.remuxhorizontalLayout_2.addWidget(self.remuxpushButton_3)

        self.remuxpushButton_5 = PushButton(self.remuxframe)
        self.remuxpushButton_5.setObjectName(u"remuxpushButton_5")
        self.remuxpushButton_5.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_5.setFont(font5)

        self.remuxhorizontalLayout_2.addWidget(self.remuxpushButton_5)


        self.verticalLayout_2.addLayout(self.remuxhorizontalLayout_2)

        self.remuxhorizontalLayout_3 = QHBoxLayout()
        self.remuxhorizontalLayout_3.setObjectName(u"remuxhorizontalLayout_3")
        self.remuxhorizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.remuxpushButton_6 = PushButton(self.remuxframe)
        self.remuxpushButton_6.setObjectName(u"remuxpushButton_6")
        self.remuxpushButton_6.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_6.setFont(font5)

        self.remuxhorizontalLayout_3.addWidget(self.remuxpushButton_6)

        self.remuxpushButton_4 = PushButton(self.remuxframe)
        self.remuxpushButton_4.setObjectName(u"remuxpushButton_4")
        self.remuxpushButton_4.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_4.setFont(font5)

        self.remuxhorizontalLayout_3.addWidget(self.remuxpushButton_4)

        self.remuxpushButton_7 = PushButton(self.remuxframe)
        self.remuxpushButton_7.setObjectName(u"remuxpushButton_7")
        self.remuxpushButton_7.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_7.setFont(font5)

        self.remuxhorizontalLayout_3.addWidget(self.remuxpushButton_7)


        self.verticalLayout_2.addLayout(self.remuxhorizontalLayout_3)

        self.remuxhorizontalLayout_4 = QHBoxLayout()
        self.remuxhorizontalLayout_4.setObjectName(u"remuxhorizontalLayout_4")
        self.remuxhorizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.remuxpushButton_10 = PushButton(self.remuxframe)
        self.remuxpushButton_10.setObjectName(u"remuxpushButton_10")
        self.remuxpushButton_10.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_10.setFont(font5)

        self.remuxhorizontalLayout_4.addWidget(self.remuxpushButton_10)

        self.remuxpushButton_8 = PushButton(self.remuxframe)
        self.remuxpushButton_8.setObjectName(u"remuxpushButton_8")
        self.remuxpushButton_8.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_8.setFont(font5)

        self.remuxhorizontalLayout_4.addWidget(self.remuxpushButton_8)

        self.remuxpushButton_9 = PushButton(self.remuxframe)
        self.remuxpushButton_9.setObjectName(u"remuxpushButton_9")
        self.remuxpushButton_9.setMinimumSize(QSize(0, 30))
        self.remuxpushButton_9.setFont(font5)

        self.remuxhorizontalLayout_4.addWidget(self.remuxpushButton_9)


        self.verticalLayout_2.addLayout(self.remuxhorizontalLayout_4)


        self.remuxIFbox04.addWidget(self.remuxframe)


        self.verticalLayout_3.addLayout(self.remuxIFbox04)

        self.remuxIFscrollArea.setWidget(self.remuxIFfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.remuxIFscrollArea)


        self.retranslateUi(remuxInterface)

        self.remuxIFpushBtn.setDefault(True)


        QMetaObject.connectSlotsByName(remuxInterface)
    # setupUi

    def retranslateUi(self, remuxInterface):
        remuxInterface.setWindowTitle(QCoreApplication.translate("remuxInterface", u"Form", None))
        self.remuxIFTitle1.setText(QCoreApplication.translate("remuxInterface", u"\u8f6c\u5c01\u88c5", None))
        self.remuxIFTitle2.setText(QCoreApplication.translate("remuxInterface", u"\u89c6\u9891", None))
        self.remuxlabel.setText(QCoreApplication.translate("remuxInterface", u"\u4e0d\u91cd\u65b0\u7f16\u7801\u7684\u64cd\u4f5c", None))
        self.remuxIFpushBtn.setText(QCoreApplication.translate("remuxInterface", u"\u5904\u7406\u89c6\u9891", None))
        self.remuxIFSTBtn.setText(QCoreApplication.translate("remuxInterface", u"\u4e2d\u6b62\u5904\u7406", None))
        self.remuxIFinputfile.setText(QCoreApplication.translate("remuxInterface", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.remuxIFoutputfolder.setText(QCoreApplication.translate("remuxInterface", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.remuxIFinputclear.setText(QCoreApplication.translate("remuxInterface", u"\u6e05\u9664", None))
        self.remuxcomboBox.setItemText(0, QCoreApplication.translate("remuxInterface", u"mp4", None))
        self.remuxcomboBox.setItemText(1, QCoreApplication.translate("remuxInterface", u"mkv", None))
        self.remuxcomboBox.setItemText(2, QCoreApplication.translate("remuxInterface", u"flv", None))
        self.remuxcomboBox.setItemText(3, QCoreApplication.translate("remuxInterface", u"mov", None))

        self.remuxpushButton.setText(QCoreApplication.translate("remuxInterface", u"\u8f6c\u5c01\u88c5", None))
        self.remuxpushButton_2.setText(QCoreApplication.translate("remuxInterface", u"\u5e38\u89c4\u63d0\u53d6\u89c6\u9891", None))
        self.remuxpushButton_3.setText(QCoreApplication.translate("remuxInterface", u"\u5e38\u89c4\u63d0\u53d6\u97f3\u9891", None))
        self.remuxpushButton_5.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u89c6\u9891\u8f68", None))
        self.remuxpushButton_6.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u97f3\u98911", None))
        self.remuxpushButton_4.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u97f3\u98912", None))
        self.remuxpushButton_7.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u97f3\u98913", None))
        self.remuxpushButton_10.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u97f3\u98914", None))
        self.remuxpushButton_8.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u5b57\u5e551", None))
        self.remuxpushButton_9.setText(QCoreApplication.translate("remuxInterface", u"\u591a\u8f68\u63d0\u53d6\u5b57\u5e552", None))
    # retranslateUi

