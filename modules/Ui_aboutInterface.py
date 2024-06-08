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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (PushButton, ScrollArea)

class Ui_AboutInterface(object):
    def setupUi(self, AboutInterface):
        if not AboutInterface.objectName():
            AboutInterface.setObjectName(u"AboutInterface")
        AboutInterface.resize(1093, 765)
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
        self.AboutIFfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1075, 747))
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
        self.AboutIFbox02.setMaximumSize(QSize(16777215, 480))
        self.AboutIFbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutIFbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.AboutIFbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AboutIFlabel = QLabel(self.AboutIFbox02)
        self.AboutIFlabel.setObjectName(u"AboutIFlabel")
        sizePolicy2.setHeightForWidth(self.AboutIFlabel.sizePolicy().hasHeightForWidth())
        self.AboutIFlabel.setSizePolicy(sizePolicy2)
        self.AboutIFlabel.setMinimumSize(QSize(720, 120))
        font2 = QFont()
        font2.setPointSize(12)
        self.AboutIFlabel.setFont(font2)
        self.AboutIFlabel.setFrameShadow(QFrame.Shadow.Plain)
        self.AboutIFlabel.setLineWidth(1)
        self.AboutIFlabel.setTextFormat(Qt.TextFormat.AutoText)
        self.AboutIFlabel.setScaledContents(False)
        self.AboutIFlabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.AboutIFlabel.setWordWrap(True)
        self.AboutIFlabel.setMargin(24)
        self.AboutIFlabel.setIndent(-1)
        self.AboutIFlabel.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.AboutIFlabel, 1, 0, 1, 3)

        self.AboutIFinputclear = PushButton(self.AboutIFbox02)
        self.AboutIFinputclear.setObjectName(u"AboutIFinputclear")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AboutIFinputclear.sizePolicy().hasHeightForWidth())
        self.AboutIFinputclear.setSizePolicy(sizePolicy3)
        self.AboutIFinputclear.setMinimumSize(QSize(0, 120))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.AboutIFinputclear.setFont(font3)

        self.gridLayout.addWidget(self.AboutIFinputclear, 0, 1, 1, 1)

        self.AboutIFinputfile = PushButton(self.AboutIFbox02)
        self.AboutIFinputfile.setObjectName(u"AboutIFinputfile")
        sizePolicy3.setHeightForWidth(self.AboutIFinputfile.sizePolicy().hasHeightForWidth())
        self.AboutIFinputfile.setSizePolicy(sizePolicy3)
        self.AboutIFinputfile.setMinimumSize(QSize(0, 120))
        self.AboutIFinputfile.setFont(font3)

        self.gridLayout.addWidget(self.AboutIFinputfile, 0, 0, 1, 1)

        self.AboutIFoutputfolder = QPushButton(self.AboutIFbox02)
        self.AboutIFoutputfolder.setObjectName(u"AboutIFoutputfolder")
        sizePolicy3.setHeightForWidth(self.AboutIFoutputfolder.sizePolicy().hasHeightForWidth())
        self.AboutIFoutputfolder.setSizePolicy(sizePolicy3)
        self.AboutIFoutputfolder.setMinimumSize(QSize(0, 120))
        self.AboutIFoutputfolder.setFont(font3)

        self.gridLayout.addWidget(self.AboutIFoutputfolder, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.AboutIFbox02)

        self.AboutIFlabel_2 = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFlabel_2.setObjectName(u"AboutIFlabel_2")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.AboutIFlabel_2.setFont(font4)

        self.verticalLayout_3.addWidget(self.AboutIFlabel_2)

        self.AboutIFbox04 = QFrame(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFbox04.setObjectName(u"AboutIFbox04")
        self.AboutIFbox04.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutIFbox04.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.AboutIFbox04)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AboutIFrefer1 = QPushButton(self.AboutIFbox04)
        self.AboutIFrefer1.setObjectName(u"AboutIFrefer1")
        sizePolicy3.setHeightForWidth(self.AboutIFrefer1.sizePolicy().hasHeightForWidth())
        self.AboutIFrefer1.setSizePolicy(sizePolicy3)
        self.AboutIFrefer1.setMinimumSize(QSize(0, 60))
        self.AboutIFrefer1.setFont(font3)

        self.horizontalLayout.addWidget(self.AboutIFrefer1)

        self.AboutIFrefer3 = QPushButton(self.AboutIFbox04)
        self.AboutIFrefer3.setObjectName(u"AboutIFrefer3")
        sizePolicy3.setHeightForWidth(self.AboutIFrefer3.sizePolicy().hasHeightForWidth())
        self.AboutIFrefer3.setSizePolicy(sizePolicy3)
        self.AboutIFrefer3.setMinimumSize(QSize(0, 60))
        self.AboutIFrefer3.setFont(font3)

        self.horizontalLayout.addWidget(self.AboutIFrefer3)

        self.AboutIFrefer2 = QPushButton(self.AboutIFbox04)
        self.AboutIFrefer2.setObjectName(u"AboutIFrefer2")
        sizePolicy3.setHeightForWidth(self.AboutIFrefer2.sizePolicy().hasHeightForWidth())
        self.AboutIFrefer2.setSizePolicy(sizePolicy3)
        self.AboutIFrefer2.setMinimumSize(QSize(0, 60))
        self.AboutIFrefer2.setFont(font3)

        self.horizontalLayout.addWidget(self.AboutIFrefer2)


        self.verticalLayout_3.addWidget(self.AboutIFbox04)

        self.AboutIFlabel_3 = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.AboutIFlabel_3.setObjectName(u"AboutIFlabel_3")
        self.AboutIFlabel_3.setFont(font4)

        self.verticalLayout_3.addWidget(self.AboutIFlabel_3)

        self.label = QLabel(self.AboutIFfacescrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setMargin(12)

        self.verticalLayout_3.addWidget(self.label)

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
        self.AboutIFlabel.setText(QCoreApplication.translate("AboutInterface", u"VideoExtractAndConcat\n"
"\n"
"\u672c\u9879\u76ee\u65e8\u5728\u5f00\u53d1\u4e00\u4e2a\u7528\u6237\u53cb\u597d\u7684\u56fe\u5f62\u754c\u9762\u5e94\u7528\u7a0b\u5e8f\uff0c\u7528\u4e8e\u89c6\u9891\u7247\u5934\u548c\u7247\u5c3e\u7684\u5feb\u901f\u5207\u5272\u4e0e\u5408\u5e76\u529f\u80fd\u3002\u901a\u8fc7\u96c6\u6210QtDesigner\u8bbe\u8ba1\u7684\u754c\u9762\u4e0ePython\u7f16\u7a0b\u8bed\u8a00\uff0c\u7ed3\u5408\u5f3a\u5927\u7684ffmpeg\u5de5\u5177\uff0c\u7528\u6237\u80fd\u591f\u8f7b\u677e\u6307\u5b9a\u89c6\u9891\u6587\u4ef6\u3001\u8bbe\u7f6e\u5207\u5272\u65f6\u95f4\u70b9\uff0c\u5b8c\u6210\u89c6\u9891\u5904\u7406\u4efb\u52a1\u3002\u9879\u76ee\u6700\u7ec8\u76ee\u6807\u662f\u63d0\u9ad8\u89c6\u9891\u7f16\u8f91\u6548\u7387\uff0c\u5c24\u5176\u9002\u5408\u9700\u8981\u6279\u91cf\u5904\u7406\u89c6\u9891\u7684\u7528\u6237\u3002", None))
        self.AboutIFinputclear.setText(QCoreApplication.translate("AboutInterface", u"Bilibili\uff1awish_2333", None))
        self.AboutIFinputfile.setText(QCoreApplication.translate("AboutInterface", u"Github\uff1awish2333", None))
        self.AboutIFoutputfolder.setText(QCoreApplication.translate("AboutInterface", u"\u4e2a\u4eba\u535a\u5ba2\uff1aWish's Blog", None))
        self.AboutIFlabel_2.setText(QCoreApplication.translate("AboutInterface", u"\u53c2\u8003\u9879\u76ee", None))
        self.AboutIFrefer1.setText(QCoreApplication.translate("AboutInterface", u"API: FFmpeg", None))
        self.AboutIFrefer3.setText(QCoreApplication.translate("AboutInterface", u"API\uff1aauto-editor", None))
        self.AboutIFrefer2.setText(QCoreApplication.translate("AboutInterface", u"UI: Fluent-Widget", None))
        self.AboutIFlabel_3.setText(QCoreApplication.translate("AboutInterface", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.label.setText(QCoreApplication.translate("AboutInterface", u"## Update20240607\n"
"**version-1.0**\n"
"- \u65b0\u589e\u81ea\u52a8\u526a\u8f91\u754c\u9762\uff08\u652f\u6301\u526a\u5207\u6c14\u53e3\uff0c\u751f\u6210\u89c6\u9891\u3001\u97f3\u9891\u3001\u5207\u7247\u3001\u5de5\u7a0b\u6587\u4ef6\uff09", None))
    # retranslateUi

