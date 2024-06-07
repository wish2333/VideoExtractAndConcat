# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VfilterInterface.ui'
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

from qfluentwidgets import (CheckBox, EditableComboBox, ListWidget, PlainTextEdit,
    PrimaryPushButton, PushButton, ScrollArea)

class Ui_VfilterInterface(object):
    def setupUi(self, VfilterInterface):
        if not VfilterInterface.objectName():
            VfilterInterface.setObjectName(u"VfilterInterface")
        VfilterInterface.resize(1081, 741)
        VfilterInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(VfilterInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VfilterscrollArea = ScrollArea(VfilterInterface)
        self.VfilterscrollArea.setObjectName(u"VfilterscrollArea")
        self.VfilterscrollArea.setMinimumSize(QSize(760, 0))
        self.VfilterscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.VfilterscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.VfilterscrollArea.setWidgetResizable(True)
        self.VfilterfacescrollAreaWidgetContents = QWidget()
        self.VfilterfacescrollAreaWidgetContents.setObjectName(u"VfilterfacescrollAreaWidgetContents")
        self.VfilterfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1063, 723))
        self.verticalLayout_3 = QVBoxLayout(self.VfilterfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Vfilterbox01 = QHBoxLayout()
        self.Vfilterbox01.setSpacing(20)
        self.Vfilterbox01.setObjectName(u"Vfilterbox01")
        self.Vfilterbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.VfilterverticalLayout_4 = QVBoxLayout()
        self.VfilterverticalLayout_4.setObjectName(u"VfilterverticalLayout_4")
        self.VfilterverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.VfilterTitle1 = QLabel(self.VfilterfacescrollAreaWidgetContents)
        self.VfilterTitle1.setObjectName(u"VfilterTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VfilterTitle1.sizePolicy().hasHeightForWidth())
        self.VfilterTitle1.setSizePolicy(sizePolicy)
        self.VfilterTitle1.setMaximumSize(QSize(150, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.VfilterTitle1.setFont(font)

        self.VfilterverticalLayout_4.addWidget(self.VfilterTitle1)

        self.VfilterTitle2 = QLabel(self.VfilterfacescrollAreaWidgetContents)
        self.VfilterTitle2.setObjectName(u"VfilterTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VfilterTitle2.sizePolicy().hasHeightForWidth())
        self.VfilterTitle2.setSizePolicy(sizePolicy1)
        self.VfilterTitle2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.VfilterTitle2.setFont(font1)

        self.VfilterverticalLayout_4.addWidget(self.VfilterTitle2)


        self.Vfilterbox01.addLayout(self.VfilterverticalLayout_4)

        self.Vfilterlabel = QLabel(self.VfilterfacescrollAreaWidgetContents)
        self.Vfilterlabel.setObjectName(u"Vfilterlabel")
        self.Vfilterlabel.setMaximumSize(QSize(16777215, 80))

        self.Vfilterbox01.addWidget(self.Vfilterlabel)

        self.VfilterhorizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Vfilterbox01.addItem(self.VfilterhorizontalSpacer)

        self.VfilterpushBtn = PrimaryPushButton(self.VfilterfacescrollAreaWidgetContents)
        self.VfilterpushBtn.setObjectName(u"VfilterpushBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VfilterpushBtn.sizePolicy().hasHeightForWidth())
        self.VfilterpushBtn.setSizePolicy(sizePolicy2)
        self.VfilterpushBtn.setMinimumSize(QSize(240, 60))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        self.VfilterpushBtn.setFont(font2)
        self.VfilterpushBtn.setFlat(False)

        self.Vfilterbox01.addWidget(self.VfilterpushBtn)

        self.VfilterSTBtn = QPushButton(self.VfilterfacescrollAreaWidgetContents)
        self.VfilterSTBtn.setObjectName(u"VfilterSTBtn")
        self.VfilterSTBtn.setMinimumSize(QSize(120, 60))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.VfilterSTBtn.setFont(font3)

        self.Vfilterbox01.addWidget(self.VfilterSTBtn)

        self.VfilterpushBtn_2 = PushButton(self.VfilterfacescrollAreaWidgetContents)
        self.VfilterpushBtn_2.setObjectName(u"VfilterpushBtn_2")
        self.VfilterpushBtn_2.setMinimumSize(QSize(80, 60))
        self.VfilterpushBtn_2.setFont(font3)

        self.Vfilterbox01.addWidget(self.VfilterpushBtn_2)


        self.verticalLayout_3.addLayout(self.Vfilterbox01)

        self.Vfilterbox02 = QFrame(self.VfilterfacescrollAreaWidgetContents)
        self.Vfilterbox02.setObjectName(u"Vfilterbox02")
        self.Vfilterbox02.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Vfilterbox02.sizePolicy().hasHeightForWidth())
        self.Vfilterbox02.setSizePolicy(sizePolicy3)
        self.Vfilterbox02.setMinimumSize(QSize(480, 145))
        self.Vfilterbox02.setMaximumSize(QSize(16777215, 240))
        self.Vfilterbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vfilterbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.Vfilterbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Vfilterinputfile = PushButton(self.Vfilterbox02)
        self.Vfilterinputfile.setObjectName(u"Vfilterinputfile")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.Vfilterinputfile.setFont(font4)

        self.gridLayout.addWidget(self.Vfilterinputfile, 0, 0, 1, 1)

        self.Vfilterinputclear = PushButton(self.Vfilterbox02)
        self.Vfilterinputclear.setObjectName(u"Vfilterinputclear")
        self.Vfilterinputclear.setFont(font4)

        self.gridLayout.addWidget(self.Vfilterinputclear, 0, 1, 1, 1)

        self.Vfilteroutputfolder = QPushButton(self.Vfilterbox02)
        self.Vfilteroutputfolder.setObjectName(u"Vfilteroutputfolder")
        self.Vfilteroutputfolder.setFont(font4)

        self.gridLayout.addWidget(self.Vfilteroutputfolder, 0, 2, 1, 1)

        self.Vfilterinputlist = ListWidget(self.Vfilterbox02)
        self.Vfilterinputlist.setObjectName(u"Vfilterinputlist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Vfilterinputlist.sizePolicy().hasHeightForWidth())
        self.Vfilterinputlist.setSizePolicy(sizePolicy4)
        self.Vfilterinputlist.setMinimumSize(QSize(0, 120))
        self.Vfilterinputlist.setMaximumSize(QSize(16777215, 200))
        self.Vfilterinputlist.setAcceptDrops(True)
        self.Vfilterinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Vfilterinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Vfilterinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Vfilterinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.Vfilterinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.Vfilterbox02)

        self.Vfilterbox03 = QHBoxLayout()
        self.Vfilterbox03.setObjectName(u"Vfilterbox03")
        self.VcodecpIFTitle2_3 = QLabel(self.VfilterfacescrollAreaWidgetContents)
        self.VcodecpIFTitle2_3.setObjectName(u"VcodecpIFTitle2_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.VcodecpIFTitle2_3.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle2_3.setSizePolicy(sizePolicy5)
        self.VcodecpIFTitle2_3.setMinimumSize(QSize(240, 45))
        self.VcodecpIFTitle2_3.setMaximumSize(QSize(600, 16777215))
        self.VcodecpIFTitle2_3.setFont(font1)

        self.Vfilterbox03.addWidget(self.VcodecpIFTitle2_3)

        self.VcodecpIFTitle2_2 = QLabel(self.VfilterfacescrollAreaWidgetContents)
        self.VcodecpIFTitle2_2.setObjectName(u"VcodecpIFTitle2_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.VcodecpIFTitle2_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle2_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFTitle2_2.setMinimumSize(QSize(60, 45))
        self.VcodecpIFTitle2_2.setMaximumSize(QSize(240, 45))
        self.VcodecpIFTitle2_2.setFont(font1)

        self.Vfilterbox03.addWidget(self.VcodecpIFTitle2_2)


        self.verticalLayout_3.addLayout(self.Vfilterbox03)

        self.Vfilterbox04 = QHBoxLayout()
        self.Vfilterbox04.setObjectName(u"Vfilterbox04")
        self.Vfilterframe_2 = QFrame(self.VfilterfacescrollAreaWidgetContents)
        self.Vfilterframe_2.setObjectName(u"Vfilterframe_2")
        sizePolicy6.setHeightForWidth(self.Vfilterframe_2.sizePolicy().hasHeightForWidth())
        self.Vfilterframe_2.setSizePolicy(sizePolicy6)
        self.Vfilterframe_2.setMinimumSize(QSize(600, 360))
        self.Vfilterframe_2.setMaximumSize(QSize(600, 360))
        self.Vfilterframe_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vfilterframe_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Vfilterframe_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VfiltergridLayout = QGridLayout()
        self.VfiltergridLayout.setObjectName(u"VfiltergridLayout")
        self.VfiltergridLayout.setHorizontalSpacing(24)
        self.VfiltergridLayout.setVerticalSpacing(16)
        self.Vfilterlabel_5 = QLabel(self.Vfilterframe_2)
        self.Vfilterlabel_5.setObjectName(u"Vfilterlabel_5")
        self.Vfilterlabel_5.setFont(font2)

        self.VfiltergridLayout.addWidget(self.Vfilterlabel_5, 0, 0, 1, 1)

        self.VfilterplainTextEdit = PlainTextEdit(self.Vfilterframe_2)
        self.VfilterplainTextEdit.setObjectName(u"VfilterplainTextEdit")
        font5 = QFont()
        font5.setPointSize(12)
        self.VfilterplainTextEdit.setFont(font5)

        self.VfiltergridLayout.addWidget(self.VfilterplainTextEdit, 0, 1, 1, 2)


        self.verticalLayout_2.addLayout(self.VfiltergridLayout)


        self.Vfilterbox04.addWidget(self.Vfilterframe_2)

        self.Vfilterframe_3 = QFrame(self.VfilterfacescrollAreaWidgetContents)
        self.Vfilterframe_3.setObjectName(u"Vfilterframe_3")
        sizePolicy6.setHeightForWidth(self.Vfilterframe_3.sizePolicy().hasHeightForWidth())
        self.Vfilterframe_3.setSizePolicy(sizePolicy6)
        self.Vfilterframe_3.setMinimumSize(QSize(280, 360))
        self.Vfilterframe_3.setMaximumSize(QSize(480, 360))
        self.Vfilterframe_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vfilterframe_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.Vfilterframe_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VcodecpIFcheckBox_4 = CheckBox(self.Vfilterframe_3)
        self.VcodecpIFcheckBox_4.setObjectName(u"VcodecpIFcheckBox_4")
        sizePolicy6.setHeightForWidth(self.VcodecpIFcheckBox_4.sizePolicy().hasHeightForWidth())
        self.VcodecpIFcheckBox_4.setSizePolicy(sizePolicy6)
        self.VcodecpIFcheckBox_4.setMinimumSize(QSize(0, 35))
        self.VcodecpIFcheckBox_4.setMaximumSize(QSize(16777215, 40))
        self.VcodecpIFcheckBox_4.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFcheckBox_4, 1, 1, 1, 1)

        self.VfilterlineEdit_3 = QLineEdit(self.Vfilterframe_3)
        self.VfilterlineEdit_3.setObjectName(u"VfilterlineEdit_3")

        self.gridLayout_3.addWidget(self.VfilterlineEdit_3, 4, 1, 1, 1)

        self.Vfilterlabel_8 = QLabel(self.Vfilterframe_3)
        self.Vfilterlabel_8.setObjectName(u"Vfilterlabel_8")

        self.gridLayout_3.addWidget(self.Vfilterlabel_8, 3, 1, 1, 1)

        self.VfilterplainTextEdit_2 = QPlainTextEdit(self.Vfilterframe_3)
        self.VfilterplainTextEdit_2.setObjectName(u"VfilterplainTextEdit_2")
        font6 = QFont()
        font6.setPointSize(10)
        self.VfilterplainTextEdit_2.setFont(font6)
        self.VfilterplainTextEdit_2.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)

        self.gridLayout_3.addWidget(self.VfilterplainTextEdit_2, 6, 0, 1, 2)

        self.VcodecpIFClearFil = PushButton(self.Vfilterframe_3)
        self.VcodecpIFClearFil.setObjectName(u"VcodecpIFClearFil")
        self.VcodecpIFClearFil.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.VcodecpIFClearFil, 1, 0, 1, 1)

        self.VcodecpIFcutsomFilter = EditableComboBox(self.Vfilterframe_3)
        self.VcodecpIFcutsomFilter.setObjectName(u"VcodecpIFcutsomFilter")
        self.VcodecpIFcutsomFilter.setFont(font5)
        self.VcodecpIFcutsomFilter.setReadOnly(True)

        self.gridLayout_3.addWidget(self.VcodecpIFcutsomFilter, 3, 0, 1, 1)

        self.Vfilterbgimg = PushButton(self.Vfilterframe_3)
        self.Vfilterbgimg.setObjectName(u"Vfilterbgimg")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Vfilterbgimg.sizePolicy().hasHeightForWidth())
        self.Vfilterbgimg.setSizePolicy(sizePolicy7)
        self.Vfilterbgimg.setMaximumSize(QSize(240, 30))
        self.Vfilterbgimg.setFont(font5)

        self.gridLayout_3.addWidget(self.Vfilterbgimg, 4, 0, 1, 1)


        self.Vfilterbox04.addWidget(self.Vfilterframe_3)


        self.verticalLayout_3.addLayout(self.Vfilterbox04)

        self.VfilterscrollArea.setWidget(self.VfilterfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.VfilterscrollArea)


        self.retranslateUi(VfilterInterface)

        self.VfilterpushBtn.setDefault(True)


        QMetaObject.connectSlotsByName(VfilterInterface)
    # setupUi

    def retranslateUi(self, VfilterInterface):
        VfilterInterface.setWindowTitle(QCoreApplication.translate("VfilterInterface", u"Form", None))
        self.VfilterTitle1.setText(QCoreApplication.translate("VfilterInterface", u"\u590d\u6742\u6ee4\u955c", None))
        self.VfilterTitle2.setText(QCoreApplication.translate("VfilterInterface", u"\u89c6\u9891", None))
        self.Vfilterlabel.setText(QCoreApplication.translate("VfilterInterface", u"\u5173\u4e8e\u590d\u6742\u6ee4\u955c\u7684\u5904\u7406", None))
        self.VfilterpushBtn.setText(QCoreApplication.translate("VfilterInterface", u"\u5904\u7406\u89c6\u9891", None))
        self.VfilterSTBtn.setText(QCoreApplication.translate("VfilterInterface", u"\u4e2d\u6b62\u5904\u7406", None))
        self.VfilterpushBtn_2.setText(QCoreApplication.translate("VfilterInterface", u"\u89e3\u51bb", None))
        self.Vfilterinputfile.setText(QCoreApplication.translate("VfilterInterface", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.Vfilterinputclear.setText(QCoreApplication.translate("VfilterInterface", u"\u6e05\u9664", None))
        self.Vfilteroutputfolder.setText(QCoreApplication.translate("VfilterInterface", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.VcodecpIFTitle2_3.setText(QCoreApplication.translate("VfilterInterface", u"\u7f16\u7801\u8bbe\u7f6e(\u8bf7\u76f4\u63a5\u4ece\u6279\u5904\u7406\u9762\u677f\u590d\u5236\u81ea\u5b9a\u4e49\u7f16\u7801)", None))
        self.VcodecpIFTitle2_2.setText(QCoreApplication.translate("VfilterInterface", u"\u6a2a\u7ad6\u5c4f\u8f6c\u6362", None))
        self.Vfilterlabel_5.setText(QCoreApplication.translate("VfilterInterface", u"\u81ea\u5b9a\u4e49\u7f16\u7801", None))
        self.VfilterplainTextEdit.setPlainText(QCoreApplication.translate("VfilterInterface", u"-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 256k", None))
        self.VcodecpIFcheckBox_4.setText(QCoreApplication.translate("VfilterInterface", u"\u97f3\u9891\u6807\u51c6\u5316\u81f3-16LUFS", None))
        self.VfilterlineEdit_3.setText(QCoreApplication.translate("VfilterInterface", u"x", None))
        self.Vfilterlabel_8.setText(QCoreApplication.translate("VfilterInterface", u"\u6a2a\u7ad6\u5c4f\u8f6c\u6362\u76ee\u6807\u5206\u8fa8\u7387", None))
        self.VfilterplainTextEdit_2.setPlainText(QCoreApplication.translate("VfilterInterface", u"\u6ee4\u955c\u53c2\u6570\uff1a", None))
        self.VcodecpIFClearFil.setText(QCoreApplication.translate("VfilterInterface", u"\u6e05\u9664\u8bbe\u7f6e", None))
        self.VcodecpIFcutsomFilter.setText(QCoreApplication.translate("VfilterInterface", u"\u6a2a\u7ad6\u5c4f\u8f6c\u6362", None))
        self.Vfilterbgimg.setText(QCoreApplication.translate("VfilterInterface", u"\u6a2a\u7ad6\u5c4f\u8f6c\u6362\u80cc\u666f\u56fe", None))
    # retranslateUi

