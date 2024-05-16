# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutInterface.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ListWidget, PlainTextEdit, PushButton, ScrollArea)

class Ui_AboutInterface(object):
    def setupUi(self, AboutInterface):
        if not AboutInterface.objectName():
            AboutInterface.setObjectName(u"AboutInterface")
        AboutInterface.resize(1085, 749)
        AboutInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(AboutInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AboutIFscrollArea = ScrollArea(AboutInterface)
        self.AboutIFscrollArea.setObjectName(u"AboutIFscrollArea")
        self.AboutIFscrollArea.setMinimumSize(QSize(760, 0))
        self.AboutIFscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.AboutIFscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.AboutIFscrollArea.setWidgetResizable(True)
        self.AboutIFfacescrollAreaWidgetContents = QWidget()
        self.AboutIFfacescrollAreaWidgetContents.setObjectName(u"AboutIFfacescrollAreaWidgetContents")
        self.AboutIFfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1067, 731))
        self.verticalLayout_3 = QVBoxLayout(self.AboutIFfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.AboutIFbox01 = QHBoxLayout()
        self.AboutIFbox01.setSpacing(20)
        self.AboutIFbox01.setObjectName(u"AboutIFbox01")
        self.AboutIFbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.AboutIFverticalLayout_4 = QVBoxLayout()
        self.AboutIFverticalLayout_4.setObjectName(u"AboutIFverticalLayout_4")
        self.AboutIFverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.AboutIFTitle1 = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFTitle1.setObjectName(u"AboutIFTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutIFTitle1.sizePolicy().hasHeightForWidth())
        self.AboutIFTitle1.setSizePolicy(sizePolicy)
        self.AboutIFTitle1.setMaximumSize(QSize(100, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.AboutIFTitle1.setFont(font)

        self.AboutIFverticalLayout_4.addWidget(self.AboutIFTitle1)

        self.AboutIFTitle2 = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFTitle2.setObjectName(u"AboutIFTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AboutIFTitle2.sizePolicy().hasHeightForWidth())
        self.AboutIFTitle2.setSizePolicy(sizePolicy1)
        self.AboutIFTitle2.setMaximumSize(QSize(300, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.AboutIFTitle2.setFont(font1)

        self.AboutIFverticalLayout_4.addWidget(self.AboutIFTitle2)


        self.AboutIFbox01.addLayout(self.AboutIFverticalLayout_4)

        self.Aboutlabel = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.Aboutlabel.setObjectName(u"Aboutlabel")
        self.Aboutlabel.setMaximumSize(QSize(16777215, 80))

        self.AboutIFbox01.addWidget(self.Aboutlabel)

        self.AboutIFhorizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AboutIFbox01.addItem(self.AboutIFhorizontalSpacer)


        self.verticalLayout_3.addLayout(self.AboutIFbox01)

        self.AboutIFbox02 = QFrame(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFbox02.setObjectName(u"AboutIFbox02")
        self.AboutIFbox02.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AboutIFbox02.sizePolicy().hasHeightForWidth())
        self.AboutIFbox02.setSizePolicy(sizePolicy2)
        self.AboutIFbox02.setMinimumSize(QSize(480, 145))
        self.AboutIFbox02.setMaximumSize(QSize(16777215, 240))
        self.AboutIFbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutIFbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.AboutIFbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AboutIFinputfile = PushButton(self.AboutIFbox02)
        self.AboutIFinputfile.setObjectName(u"AboutIFinputfile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AboutIFinputfile.sizePolicy().hasHeightForWidth())
        self.AboutIFinputfile.setSizePolicy(sizePolicy3)
        self.AboutIFinputfile.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.AboutIFinputfile.setFont(font2)

        self.gridLayout.addWidget(self.AboutIFinputfile, 0, 0, 1, 1)

        self.AboutIFinputclear = PushButton(self.AboutIFbox02)
        self.AboutIFinputclear.setObjectName(u"AboutIFinputclear")
        sizePolicy3.setHeightForWidth(self.AboutIFinputclear.sizePolicy().hasHeightForWidth())
        self.AboutIFinputclear.setSizePolicy(sizePolicy3)
        self.AboutIFinputclear.setMinimumSize(QSize(0, 60))
        self.AboutIFinputclear.setFont(font2)

        self.gridLayout.addWidget(self.AboutIFinputclear, 0, 1, 1, 1)

        self.AboutIFoutputfolder = QPushButton(self.AboutIFbox02)
        self.AboutIFoutputfolder.setObjectName(u"AboutIFoutputfolder")
        sizePolicy3.setHeightForWidth(self.AboutIFoutputfolder.sizePolicy().hasHeightForWidth())
        self.AboutIFoutputfolder.setSizePolicy(sizePolicy3)
        self.AboutIFoutputfolder.setMinimumSize(QSize(0, 60))
        self.AboutIFoutputfolder.setFont(font2)

        self.gridLayout.addWidget(self.AboutIFoutputfolder, 0, 2, 1, 1)

        self.AboutIFinputlist = ListWidget(self.AboutIFbox02)
        self.AboutIFinputlist.setObjectName(u"AboutIFinputlist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.AboutIFinputlist.sizePolicy().hasHeightForWidth())
        self.AboutIFinputlist.setSizePolicy(sizePolicy4)
        self.AboutIFinputlist.setMinimumSize(QSize(0, 120))
        self.AboutIFinputlist.setMaximumSize(QSize(16777215, 200))
        self.AboutIFinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.AboutIFinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.AboutIFinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.AboutIFinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.AboutIFinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.AboutIFbox02)

        self.AboutIFbox03 = QHBoxLayout()
        self.AboutIFbox03.setObjectName(u"AboutIFbox03")

        self.verticalLayout_3.addLayout(self.AboutIFbox03)

        self.AboutIFbox04 = QHBoxLayout()
        self.AboutIFbox04.setObjectName(u"AboutIFbox04")

        self.verticalLayout_3.addLayout(self.AboutIFbox04)

        self.AboutIFconsole = PlainTextEdit(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFconsole.setObjectName(u"AboutIFconsole")
        sizePolicy2.setHeightForWidth(self.AboutIFconsole.sizePolicy().hasHeightForWidth())
        self.AboutIFconsole.setSizePolicy(sizePolicy2)
        self.AboutIFconsole.setMinimumSize(QSize(640, 160))
        self.AboutIFconsole.setMaximumSize(QSize(6400, 300))
        self.AboutIFconsole.setUndoRedoEnabled(False)
        self.AboutIFconsole.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.AboutIFconsole.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.AboutIFconsole)

        self.AboutIFscrollArea.setWidget(self.AboutIFfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.AboutIFscrollArea)


        self.retranslateUi(AboutInterface)

        QMetaObject.connectSlotsByName(AboutInterface)
    # setupUi

    def retranslateUi(self, AboutInterface):
        AboutInterface.setWindowTitle(QCoreApplication.translate("AboutInterface", u"Form", None))
        self.AboutIFTitle1.setText(QCoreApplication.translate("AboutInterface", u"\u5173\u4e8e", None))
        self.AboutIFTitle2.setText(QCoreApplication.translate("AboutInterface", u"\u4f5c\u8005\uff1awish_2333", None))
        self.Aboutlabel.setText(QCoreApplication.translate("AboutInterface", u"\u4e00\u4e2a\u89c6\u9891\u6279\u5904\u7406\u7684\u5de5\u5177\u7bb1", None))
        self.AboutIFinputfile.setText(QCoreApplication.translate("AboutInterface", u"Github\uff1awish2333", None))
        self.AboutIFinputclear.setText(QCoreApplication.translate("AboutInterface", u"Bilibili\uff1awish_2333", None))
        self.AboutIFoutputfolder.setText(QCoreApplication.translate("AboutInterface", u"\u4e2a\u4eba\u535a\u5ba2\uff1aWish's Blog", None))
    # retranslateUi

