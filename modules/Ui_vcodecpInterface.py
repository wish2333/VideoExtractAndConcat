# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vcodecpInterface.ui'
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

from qfluentwidgets import (CheckBox, ComboBox, DoubleSpinBox, EditableComboBox,
    ListWidget, PlainTextEdit, PrimaryPushButton, PushButton,
    RadioButton, ScrollArea, SpinBox, TimeEdit)

class Ui_VcodecpInterface(object):
    def setupUi(self, VcodecpInterface):
        if not VcodecpInterface.objectName():
            VcodecpInterface.setObjectName(u"VcodecpInterface")
        VcodecpInterface.resize(1085, 749)
        VcodecpInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(VcodecpInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VcodecpIFscrollArea = ScrollArea(VcodecpInterface)
        self.VcodecpIFscrollArea.setObjectName(u"VcodecpIFscrollArea")
        self.VcodecpIFscrollArea.setMinimumSize(QSize(760, 0))
        self.VcodecpIFscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.VcodecpIFscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.VcodecpIFscrollArea.setWidgetResizable(True)
        self.VcodecpIFfacescrollAreaWidgetContents = QWidget()
        self.VcodecpIFfacescrollAreaWidgetContents.setObjectName(u"VcodecpIFfacescrollAreaWidgetContents")
        self.VcodecpIFfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1050, 844))
        self.verticalLayout_3 = QVBoxLayout(self.VcodecpIFfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VcodecpIFbox01 = QHBoxLayout()
        self.VcodecpIFbox01.setSpacing(20)
        self.VcodecpIFbox01.setObjectName(u"VcodecpIFbox01")
        self.VcodecpIFbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.VcodecpIFverticalLayout_4 = QVBoxLayout()
        self.VcodecpIFverticalLayout_4.setObjectName(u"VcodecpIFverticalLayout_4")
        self.VcodecpIFverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.VcodecpIFTitle1 = QLabel(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFTitle1.setObjectName(u"VcodecpIFTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VcodecpIFTitle1.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle1.setSizePolicy(sizePolicy)
        self.VcodecpIFTitle1.setMaximumSize(QSize(120, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.VcodecpIFTitle1.setFont(font)

        self.VcodecpIFverticalLayout_4.addWidget(self.VcodecpIFTitle1)

        self.VcodecpIFTitle2 = QLabel(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFTitle2.setObjectName(u"VcodecpIFTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VcodecpIFTitle2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle2.setSizePolicy(sizePolicy1)
        self.VcodecpIFTitle2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.VcodecpIFTitle2.setFont(font1)

        self.VcodecpIFverticalLayout_4.addWidget(self.VcodecpIFTitle2)


        self.VcodecpIFbox01.addLayout(self.VcodecpIFverticalLayout_4)

        self.label = QLabel(self.VcodecpIFfacescrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 80))

        self.VcodecpIFbox01.addWidget(self.label)

        self.VcodecpIFhorizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.VcodecpIFbox01.addItem(self.VcodecpIFhorizontalSpacer)

        self.VcodecpIFpushBtn = PrimaryPushButton(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFpushBtn.setObjectName(u"VcodecpIFpushBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VcodecpIFpushBtn.sizePolicy().hasHeightForWidth())
        self.VcodecpIFpushBtn.setSizePolicy(sizePolicy2)
        self.VcodecpIFpushBtn.setMinimumSize(QSize(240, 60))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        self.VcodecpIFpushBtn.setFont(font2)
        self.VcodecpIFpushBtn.setFlat(False)

        self.VcodecpIFbox01.addWidget(self.VcodecpIFpushBtn)

        self.VcodecpIFSTBtn = QPushButton(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFSTBtn.setObjectName(u"VcodecpIFSTBtn")
        self.VcodecpIFSTBtn.setMinimumSize(QSize(120, 60))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.VcodecpIFSTBtn.setFont(font3)

        self.VcodecpIFbox01.addWidget(self.VcodecpIFSTBtn)

        self.VcodecpIFpushBtn_2 = PushButton(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFpushBtn_2.setObjectName(u"VcodecpIFpushBtn_2")
        self.VcodecpIFpushBtn_2.setMinimumSize(QSize(80, 60))
        self.VcodecpIFpushBtn_2.setFont(font3)

        self.VcodecpIFbox01.addWidget(self.VcodecpIFpushBtn_2)


        self.verticalLayout_3.addLayout(self.VcodecpIFbox01)

        self.VcodecpIFbox02 = QFrame(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFbox02.setObjectName(u"VcodecpIFbox02")
        self.VcodecpIFbox02.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.VcodecpIFbox02.sizePolicy().hasHeightForWidth())
        self.VcodecpIFbox02.setSizePolicy(sizePolicy3)
        self.VcodecpIFbox02.setMinimumSize(QSize(480, 145))
        self.VcodecpIFbox02.setMaximumSize(QSize(16777215, 240))
        self.VcodecpIFbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.VcodecpIFbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.VcodecpIFbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.VcodecpIFinputfile = PushButton(self.VcodecpIFbox02)
        self.VcodecpIFinputfile.setObjectName(u"VcodecpIFinputfile")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.VcodecpIFinputfile.setFont(font4)

        self.gridLayout.addWidget(self.VcodecpIFinputfile, 0, 0, 1, 1)

        self.VcodecpIFinputclear = PushButton(self.VcodecpIFbox02)
        self.VcodecpIFinputclear.setObjectName(u"VcodecpIFinputclear")
        self.VcodecpIFinputclear.setFont(font4)

        self.gridLayout.addWidget(self.VcodecpIFinputclear, 0, 1, 1, 1)

        self.VcodecpIFoutputfolder = QPushButton(self.VcodecpIFbox02)
        self.VcodecpIFoutputfolder.setObjectName(u"VcodecpIFoutputfolder")
        self.VcodecpIFoutputfolder.setFont(font4)

        self.gridLayout.addWidget(self.VcodecpIFoutputfolder, 0, 2, 1, 1)

        self.VcodecpIFinputlist = ListWidget(self.VcodecpIFbox02)
        self.VcodecpIFinputlist.setObjectName(u"VcodecpIFinputlist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.VcodecpIFinputlist.sizePolicy().hasHeightForWidth())
        self.VcodecpIFinputlist.setSizePolicy(sizePolicy4)
        self.VcodecpIFinputlist.setMinimumSize(QSize(0, 120))
        self.VcodecpIFinputlist.setMaximumSize(QSize(16777215, 200))
        self.VcodecpIFinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.VcodecpIFinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.VcodecpIFinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.VcodecpIFinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.VcodecpIFinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.VcodecpIFbox02)

        self.VcodecpIFbox03 = QHBoxLayout()
        self.VcodecpIFbox03.setObjectName(u"VcodecpIFbox03")
        self.VcodecpIFTitle2_3 = QLabel(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFTitle2_3.setObjectName(u"VcodecpIFTitle2_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.VcodecpIFTitle2_3.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle2_3.setSizePolicy(sizePolicy5)
        self.VcodecpIFTitle2_3.setMinimumSize(QSize(240, 45))
        self.VcodecpIFTitle2_3.setMaximumSize(QSize(600, 16777215))
        self.VcodecpIFTitle2_3.setFont(font1)

        self.VcodecpIFbox03.addWidget(self.VcodecpIFTitle2_3)

        self.VcodecpIFTitle2_2 = QLabel(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFTitle2_2.setObjectName(u"VcodecpIFTitle2_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.VcodecpIFTitle2_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFTitle2_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFTitle2_2.setMinimumSize(QSize(60, 45))
        self.VcodecpIFTitle2_2.setMaximumSize(QSize(240, 45))
        self.VcodecpIFTitle2_2.setFont(font1)

        self.VcodecpIFbox03.addWidget(self.VcodecpIFTitle2_2)


        self.verticalLayout_3.addLayout(self.VcodecpIFbox03)

        self.VcodecpIFbox04 = QHBoxLayout()
        self.VcodecpIFbox04.setObjectName(u"VcodecpIFbox04")
        self.VcodecpIFframe_2 = QFrame(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFframe_2.setObjectName(u"VcodecpIFframe_2")
        sizePolicy6.setHeightForWidth(self.VcodecpIFframe_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFframe_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFframe_2.setMinimumSize(QSize(600, 360))
        self.VcodecpIFframe_2.setMaximumSize(QSize(600, 360))
        self.VcodecpIFframe_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.VcodecpIFframe_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.VcodecpIFframe_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VcodecpIFgridLayout = QGridLayout()
        self.VcodecpIFgridLayout.setObjectName(u"VcodecpIFgridLayout")
        self.VcodecpIFgridLayout.setHorizontalSpacing(24)
        self.VcodecpIFgridLayout.setVerticalSpacing(16)
        self.VcodecpIFlabel_7 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel_7.setObjectName(u"VcodecpIFlabel_7")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setKerning(True)
        self.VcodecpIFlabel_7.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel_7, 2, 2, 1, 1)

        self.VcodecpIFlineEditAE = EditableComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFlineEditAE.setObjectName(u"VcodecpIFlineEditAE")
        self.VcodecpIFlineEditAE.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setPointSize(12)
        self.VcodecpIFlineEditAE.setFont(font6)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlineEditAE, 3, 1, 1, 1)

        self.VcodecpIFcomboBox_2 = ComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFcomboBox_2.addItem("")
        self.VcodecpIFcomboBox_2.addItem("")
        self.VcodecpIFcomboBox_2.addItem("")
        self.VcodecpIFcomboBox_2.addItem("")
        self.VcodecpIFcomboBox_2.addItem("")
        self.VcodecpIFcomboBox_2.setObjectName(u"VcodecpIFcomboBox_2")
        sizePolicy6.setHeightForWidth(self.VcodecpIFcomboBox_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFcomboBox_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFcomboBox_2.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setKerning(True)
        self.VcodecpIFcomboBox_2.setFont(font7)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcomboBox_2, 0, 3, 1, 1)

        self.VcodecpIFplainTextEdit = PlainTextEdit(self.VcodecpIFframe_2)
        self.VcodecpIFplainTextEdit.setObjectName(u"VcodecpIFplainTextEdit")
        self.VcodecpIFplainTextEdit.setFont(font6)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFplainTextEdit, 5, 1, 1, 3)

        self.VcodecpIFlabel_4 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel_4.setObjectName(u"VcodecpIFlabel_4")
        self.VcodecpIFlabel_4.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel_4, 3, 2, 1, 1)

        self.VcodecpIFTitle3_2 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFTitle3_2.setObjectName(u"VcodecpIFTitle3_2")
        self.VcodecpIFTitle3_2.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFTitle3_2, 0, 0, 1, 1)

        self.VcodecpIFlabel = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel.setObjectName(u"VcodecpIFlabel")
        self.VcodecpIFlabel.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel, 0, 2, 1, 1)

        self.VcodecpIFlineEdit_2 = EditableComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFlineEdit_2.setObjectName(u"VcodecpIFlineEdit_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.VcodecpIFlineEdit_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFlineEdit_2.setSizePolicy(sizePolicy7)
        font8 = QFont()
        font8.setPointSize(10)
        font8.setKerning(True)
        self.VcodecpIFlineEdit_2.setFont(font8)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlineEdit_2, 1, 3, 1, 1)

        self.VcodecpIFcomboBox_5 = ComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFcomboBox_5.addItem("")
        self.VcodecpIFcomboBox_5.setObjectName(u"VcodecpIFcomboBox_5")
        self.VcodecpIFcomboBox_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.VcodecpIFcomboBox_5.sizePolicy().hasHeightForWidth())
        self.VcodecpIFcomboBox_5.setSizePolicy(sizePolicy1)
        self.VcodecpIFcomboBox_5.setMinimumSize(QSize(0, 30))

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcomboBox_5, 4, 1, 1, 3)

        self.VcodecpIFcheckBox_2 = CheckBox(self.VcodecpIFframe_2)
        self.VcodecpIFcheckBox_2.setObjectName(u"VcodecpIFcheckBox_2")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setKerning(True)
        self.VcodecpIFcheckBox_2.setFont(font9)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcheckBox_2, 1, 0, 1, 1)

        self.VcodecpIFspinBox_2 = SpinBox(self.VcodecpIFframe_2)
        self.VcodecpIFspinBox_2.setObjectName(u"VcodecpIFspinBox_2")
        sizePolicy6.setHeightForWidth(self.VcodecpIFspinBox_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFspinBox_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFspinBox_2.setFont(font7)
        self.VcodecpIFspinBox_2.setMaximum(51)
        self.VcodecpIFspinBox_2.setValue(23)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFspinBox_2, 2, 3, 1, 1)

        self.VcodecpIFcheckBox_3 = CheckBox(self.VcodecpIFframe_2)
        self.VcodecpIFcheckBox_3.setObjectName(u"VcodecpIFcheckBox_3")
        self.VcodecpIFcheckBox_3.setFont(font9)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcheckBox_3, 1, 2, 1, 1)

        self.VcodecpIFlineEditVE = EditableComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFlineEditVE.setObjectName(u"VcodecpIFlineEditVE")
        self.VcodecpIFlineEditVE.setMinimumSize(QSize(0, 30))
        self.VcodecpIFlineEditVE.setFont(font6)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlineEditVE, 0, 1, 1, 1)

        self.VcodecpIFlabel_6 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel_6.setObjectName(u"VcodecpIFlabel_6")
        self.VcodecpIFlabel_6.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel_6, 2, 0, 1, 1)

        self.VcodecpIFspinBox = SpinBox(self.VcodecpIFframe_2)
        self.VcodecpIFspinBox.setObjectName(u"VcodecpIFspinBox")
        sizePolicy6.setHeightForWidth(self.VcodecpIFspinBox.sizePolicy().hasHeightForWidth())
        self.VcodecpIFspinBox.setSizePolicy(sizePolicy6)
        self.VcodecpIFspinBox.setMinimumSize(QSize(0, 30))
        self.VcodecpIFspinBox.setFont(font7)
        self.VcodecpIFspinBox.setMaximum(40000)
        self.VcodecpIFspinBox.setSingleStep(1000)
        self.VcodecpIFspinBox.setValue(800)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFspinBox, 2, 1, 1, 1)

        self.VcodecpIFlineEdit = EditableComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFlineEdit.setObjectName(u"VcodecpIFlineEdit")
        sizePolicy7.setHeightForWidth(self.VcodecpIFlineEdit.sizePolicy().hasHeightForWidth())
        self.VcodecpIFlineEdit.setSizePolicy(sizePolicy7)
        self.VcodecpIFlineEdit.setFont(font8)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlineEdit, 1, 1, 1, 1)

        self.VcodecpIFlabel_3 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel_3.setObjectName(u"VcodecpIFlabel_3")
        self.VcodecpIFlabel_3.setFont(font5)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel_3, 3, 0, 1, 1)

        self.VcodecpIFlabel_5 = QLabel(self.VcodecpIFframe_2)
        self.VcodecpIFlabel_5.setObjectName(u"VcodecpIFlabel_5")
        self.VcodecpIFlabel_5.setFont(font2)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFlabel_5, 5, 0, 1, 1)

        self.VcodecpIFcheckBox = CheckBox(self.VcodecpIFframe_2)
        self.VcodecpIFcheckBox.setObjectName(u"VcodecpIFcheckBox")
        self.VcodecpIFcheckBox.setSizeIncrement(QSize(0, 0))
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setKerning(True)
        font10.setHintingPreference(QFont.PreferDefaultHinting)
        self.VcodecpIFcheckBox.setFont(font10)
        self.VcodecpIFcheckBox.setMouseTracking(True)
        self.VcodecpIFcheckBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.VcodecpIFcheckBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.VcodecpIFcheckBox.setAutoExclusive(False)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcheckBox, 4, 0, 1, 1)

        self.VcodecpIFcomboBox_3 = ComboBox(self.VcodecpIFframe_2)
        self.VcodecpIFcomboBox_3.addItem("")
        self.VcodecpIFcomboBox_3.addItem("")
        self.VcodecpIFcomboBox_3.addItem("")
        self.VcodecpIFcomboBox_3.addItem("")
        self.VcodecpIFcomboBox_3.addItem("")
        self.VcodecpIFcomboBox_3.setObjectName(u"VcodecpIFcomboBox_3")
        sizePolicy3.setHeightForWidth(self.VcodecpIFcomboBox_3.sizePolicy().hasHeightForWidth())
        self.VcodecpIFcomboBox_3.setSizePolicy(sizePolicy3)
        self.VcodecpIFcomboBox_3.setMinimumSize(QSize(0, 30))
        self.VcodecpIFcomboBox_3.setFont(font7)

        self.VcodecpIFgridLayout.addWidget(self.VcodecpIFcomboBox_3, 3, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.VcodecpIFgridLayout)


        self.VcodecpIFbox04.addWidget(self.VcodecpIFframe_2)

        self.VcodecpIFframe_3 = QFrame(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFframe_3.setObjectName(u"VcodecpIFframe_3")
        sizePolicy6.setHeightForWidth(self.VcodecpIFframe_3.sizePolicy().hasHeightForWidth())
        self.VcodecpIFframe_3.setSizePolicy(sizePolicy6)
        self.VcodecpIFframe_3.setMinimumSize(QSize(280, 360))
        self.VcodecpIFframe_3.setMaximumSize(QSize(480, 360))
        self.VcodecpIFframe_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.VcodecpIFframe_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.VcodecpIFframe_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VcodecpIFlabel_2 = QLabel(self.VcodecpIFframe_3)
        self.VcodecpIFlabel_2.setObjectName(u"VcodecpIFlabel_2")
        sizePolicy6.setHeightForWidth(self.VcodecpIFlabel_2.sizePolicy().hasHeightForWidth())
        self.VcodecpIFlabel_2.setSizePolicy(sizePolicy6)
        self.VcodecpIFlabel_2.setMinimumSize(QSize(0, 35))
        self.VcodecpIFlabel_2.setMaximumSize(QSize(16777215, 40))
        self.VcodecpIFlabel_2.setFont(font5)

        self.gridLayout_3.addWidget(self.VcodecpIFlabel_2, 4, 0, 1, 1)

        self.VcodecpIFcheckBox_4 = CheckBox(self.VcodecpIFframe_3)
        self.VcodecpIFcheckBox_4.setObjectName(u"VcodecpIFcheckBox_4")
        sizePolicy6.setHeightForWidth(self.VcodecpIFcheckBox_4.sizePolicy().hasHeightForWidth())
        self.VcodecpIFcheckBox_4.setSizePolicy(sizePolicy6)
        self.VcodecpIFcheckBox_4.setMinimumSize(QSize(0, 35))
        self.VcodecpIFcheckBox_4.setMaximumSize(QSize(16777215, 40))
        self.VcodecpIFcheckBox_4.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFcheckBox_4, 1, 1, 1, 1)

        self.VcodecpIFtimeEdit_3 = TimeEdit(self.VcodecpIFframe_3)
        self.VcodecpIFtimeEdit_3.setObjectName(u"VcodecpIFtimeEdit_3")
        self.VcodecpIFtimeEdit_3.setMinimumSize(QSize(160, 30))
        self.VcodecpIFtimeEdit_3.setFont(font7)

        self.gridLayout_3.addWidget(self.VcodecpIFtimeEdit_3, 5, 0, 1, 1)

        self.VcodecpIFcutsomFilter = QLineEdit(self.VcodecpIFframe_3)
        self.VcodecpIFcutsomFilter.setObjectName(u"VcodecpIFcutsomFilter")

        self.gridLayout_3.addWidget(self.VcodecpIFcutsomFilter, 2, 0, 1, 1)

        self.VcodecpIFpushButton_4 = PushButton(self.VcodecpIFframe_3)
        self.VcodecpIFpushButton_4.setObjectName(u"VcodecpIFpushButton_4")
        sizePolicy6.setHeightForWidth(self.VcodecpIFpushButton_4.sizePolicy().hasHeightForWidth())
        self.VcodecpIFpushButton_4.setSizePolicy(sizePolicy6)
        self.VcodecpIFpushButton_4.setMinimumSize(QSize(0, 30))
        self.VcodecpIFpushButton_4.setFont(font6)

        self.gridLayout_3.addWidget(self.VcodecpIFpushButton_4, 8, 1, 1, 1)

        self.VcodecpIFlabel_9 = QLabel(self.VcodecpIFframe_3)
        self.VcodecpIFlabel_9.setObjectName(u"VcodecpIFlabel_9")
        self.VcodecpIFlabel_9.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFlabel_9, 7, 1, 1, 1)

        self.VcodecpIFcheckBox_merge = CheckBox(self.VcodecpIFframe_3)
        self.VcodecpIFcheckBox_merge.setObjectName(u"VcodecpIFcheckBox_merge")
        self.VcodecpIFcheckBox_merge.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFcheckBox_merge, 3, 1, 1, 1)

        self.VcodecpIFtFormat = EditableComboBox(self.VcodecpIFframe_3)
        self.VcodecpIFtFormat.setObjectName(u"VcodecpIFtFormat")
        self.VcodecpIFtFormat.setFont(font6)

        self.gridLayout_3.addWidget(self.VcodecpIFtFormat, 9, 1, 1, 1)

        self.VcodecpIFpushButton_3 = PushButton(self.VcodecpIFframe_3)
        self.VcodecpIFpushButton_3.setObjectName(u"VcodecpIFpushButton_3")
        sizePolicy4.setHeightForWidth(self.VcodecpIFpushButton_3.sizePolicy().hasHeightForWidth())
        self.VcodecpIFpushButton_3.setSizePolicy(sizePolicy4)
        self.VcodecpIFpushButton_3.setMinimumSize(QSize(0, 30))
        self.VcodecpIFpushButton_3.setFont(font6)

        self.gridLayout_3.addWidget(self.VcodecpIFpushButton_3, 5, 1, 1, 1)

        self.VcodecpIFtimeEdit_2 = TimeEdit(self.VcodecpIFframe_3)
        self.VcodecpIFtimeEdit_2.setObjectName(u"VcodecpIFtimeEdit_2")
        self.VcodecpIFtimeEdit_2.setMinimumSize(QSize(160, 30))
        self.VcodecpIFtimeEdit_2.setFont(font7)

        self.gridLayout_3.addWidget(self.VcodecpIFtimeEdit_2, 9, 0, 1, 1)

        self.VcodecpIFlabel_8 = QLabel(self.VcodecpIFframe_3)
        self.VcodecpIFlabel_8.setObjectName(u"VcodecpIFlabel_8")
        self.VcodecpIFlabel_8.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFlabel_8, 4, 1, 1, 1)

        self.VcodecpIFClearFil = PushButton(self.VcodecpIFframe_3)
        self.VcodecpIFClearFil.setObjectName(u"VcodecpIFClearFil")
        self.VcodecpIFClearFil.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.VcodecpIFClearFil, 1, 0, 1, 1)

        self.VcodecpIFradioButton = RadioButton(self.VcodecpIFframe_3)
        self.VcodecpIFradioButton.setObjectName(u"VcodecpIFradioButton")
        self.VcodecpIFradioButton.setMaximumSize(QSize(16777215, 20))
        self.VcodecpIFradioButton.setFont(font4)
        self.VcodecpIFradioButton.setChecked(True)

        self.gridLayout_3.addWidget(self.VcodecpIFradioButton, 7, 0, 1, 1)

        self.VcodecpIFdoubleSpinBox = DoubleSpinBox(self.VcodecpIFframe_3)
        self.VcodecpIFdoubleSpinBox.setObjectName(u"VcodecpIFdoubleSpinBox")
        sizePolicy7.setHeightForWidth(self.VcodecpIFdoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.VcodecpIFdoubleSpinBox.setSizePolicy(sizePolicy7)
        self.VcodecpIFdoubleSpinBox.setMinimumSize(QSize(150, 30))
        self.VcodecpIFdoubleSpinBox.setFont(font7)
        self.VcodecpIFdoubleSpinBox.setMinimum(0.500000000000000)
        self.VcodecpIFdoubleSpinBox.setMaximum(2.000000000000000)
        self.VcodecpIFdoubleSpinBox.setSingleStep(0.050000000000000)
        self.VcodecpIFdoubleSpinBox.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.VcodecpIFdoubleSpinBox, 2, 1, 1, 1)

        self.VcodecpIFcheckBox_extract = CheckBox(self.VcodecpIFframe_3)
        self.VcodecpIFcheckBox_extract.setObjectName(u"VcodecpIFcheckBox_extract")
        self.VcodecpIFcheckBox_extract.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFcheckBox_extract, 3, 0, 1, 1)

        self.VcodecpIFradioButton_2 = RadioButton(self.VcodecpIFframe_3)
        self.VcodecpIFradioButton_2.setObjectName(u"VcodecpIFradioButton_2")
        self.VcodecpIFradioButton_2.setMaximumSize(QSize(16777215, 20))
        self.VcodecpIFradioButton_2.setFont(font4)

        self.gridLayout_3.addWidget(self.VcodecpIFradioButton_2, 8, 0, 1, 1)


        self.VcodecpIFbox04.addWidget(self.VcodecpIFframe_3)


        self.verticalLayout_3.addLayout(self.VcodecpIFbox04)

        self.VcodecpIFconsole = PlainTextEdit(self.VcodecpIFfacescrollAreaWidgetContents)
        self.VcodecpIFconsole.setObjectName(u"VcodecpIFconsole")
        sizePolicy3.setHeightForWidth(self.VcodecpIFconsole.sizePolicy().hasHeightForWidth())
        self.VcodecpIFconsole.setSizePolicy(sizePolicy3)
        self.VcodecpIFconsole.setMinimumSize(QSize(640, 160))
        self.VcodecpIFconsole.setMaximumSize(QSize(6400, 300))
        self.VcodecpIFconsole.setUndoRedoEnabled(False)
        self.VcodecpIFconsole.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.VcodecpIFconsole.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.VcodecpIFconsole)

        self.VcodecpIFscrollArea.setWidget(self.VcodecpIFfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.VcodecpIFscrollArea)


        self.retranslateUi(VcodecpInterface)

        self.VcodecpIFpushBtn.setDefault(True)


        QMetaObject.connectSlotsByName(VcodecpInterface)
    # setupUi

    def retranslateUi(self, VcodecpInterface):
        VcodecpInterface.setWindowTitle(QCoreApplication.translate("VcodecpInterface", u"Form", None))
        self.VcodecpIFTitle1.setText(QCoreApplication.translate("VcodecpInterface", u"\u6279\u5904\u7406", None))
        self.VcodecpIFTitle2.setText(QCoreApplication.translate("VcodecpInterface", u"\u89c6\u9891", None))
        self.label.setText(QCoreApplication.translate("VcodecpInterface", u"\u4e0d\u6539\u53d8\u540e\u7f00\u540d\u7684\u6279\u91cf\u5904\u7406", None))
        self.VcodecpIFpushBtn.setText(QCoreApplication.translate("VcodecpInterface", u"\u5904\u7406\u89c6\u9891", None))
        self.VcodecpIFSTBtn.setText(QCoreApplication.translate("VcodecpInterface", u"\u4e2d\u6b62\u5904\u7406", None))
        self.VcodecpIFpushBtn_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u89e3\u51bb", None))
        self.VcodecpIFinputfile.setText(QCoreApplication.translate("VcodecpInterface", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.VcodecpIFinputclear.setText(QCoreApplication.translate("VcodecpInterface", u"\u6e05\u9664", None))
        self.VcodecpIFoutputfolder.setText(QCoreApplication.translate("VcodecpInterface", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.VcodecpIFTitle2_3.setText(QCoreApplication.translate("VcodecpInterface", u"\u7f16\u7801\u8bbe\u7f6e", None))
        self.VcodecpIFTitle2_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u6ee4\u955c\u8bbe\u7f6e", None))
        self.VcodecpIFlabel_7.setText(QCoreApplication.translate("VcodecpInterface", u"\u89c6\u9891\u54c1\u8d28", None))
        self.VcodecpIFlineEditAE.setText(QCoreApplication.translate("VcodecpInterface", u"aac", None))
        self.VcodecpIFcomboBox_2.setItemText(0, QCoreApplication.translate("VcodecpInterface", u"CRF\u54c1\u8d28-medium", None))
        self.VcodecpIFcomboBox_2.setItemText(1, QCoreApplication.translate("VcodecpInterface", u"CRF\u54c1\u8d28-fast", None))
        self.VcodecpIFcomboBox_2.setItemText(2, QCoreApplication.translate("VcodecpInterface", u"CBR\u5e73\u5747\u7801\u7387-medium", None))
        self.VcodecpIFcomboBox_2.setItemText(3, QCoreApplication.translate("VcodecpInterface", u"CBR\u5e73\u5747\u7801\u7387-fast", None))
        self.VcodecpIFcomboBox_2.setItemText(4, QCoreApplication.translate("VcodecpInterface", u"CQP\u786c\u7f16\u54c1\u8d28(*qsv)", None))

        self.VcodecpIFplainTextEdit.setPlainText(QCoreApplication.translate("VcodecpInterface", u"-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k", None))
        self.VcodecpIFlabel_4.setText(QCoreApplication.translate("VcodecpInterface", u"\u97f3\u9891\u7f16\u7801\u53c2\u6570", None))
        self.VcodecpIFTitle3_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u89c6\u9891\u7f16\u7801\u5668", None))
        self.VcodecpIFlabel.setText(QCoreApplication.translate("VcodecpInterface", u"\u89c6\u9891\u7f16\u7801\u53c2\u6570", None))
        self.VcodecpIFlineEdit_2.setText(QCoreApplication.translate("VcodecpInterface", u"60", None))
        self.VcodecpIFcomboBox_5.setItemText(0, QCoreApplication.translate("VcodecpInterface", u"\u9ed8\u8ba4", None))

        self.VcodecpIFcheckBox_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u5206\u8fa8\u7387", None))
        self.VcodecpIFcheckBox_3.setText(QCoreApplication.translate("VcodecpInterface", u"\u5e27\u7387", None))
        self.VcodecpIFlineEditVE.setText(QCoreApplication.translate("VcodecpInterface", u"libx264", None))
        self.VcodecpIFlabel_6.setText(QCoreApplication.translate("VcodecpInterface", u"\u89c6\u9891\u7801\u7387kbps", None))
        self.VcodecpIFlineEdit.setText(QCoreApplication.translate("VcodecpInterface", u"1920x1080", None))
        self.VcodecpIFlabel_3.setText(QCoreApplication.translate("VcodecpInterface", u"\u97f3\u9891\u7f16\u7801\u5668", None))
        self.VcodecpIFlabel_5.setText(QCoreApplication.translate("VcodecpInterface", u"\u81ea\u5b9a\u4e49\u7f16\u7801", None))
        self.VcodecpIFcheckBox.setText(QCoreApplication.translate("VcodecpInterface", u"\u4f7f\u7528\u9884\u8bbe", None))
        self.VcodecpIFcomboBox_3.setItemText(0, QCoreApplication.translate("VcodecpInterface", u"128k", None))
        self.VcodecpIFcomboBox_3.setItemText(1, QCoreApplication.translate("VcodecpInterface", u"64k", None))
        self.VcodecpIFcomboBox_3.setItemText(2, QCoreApplication.translate("VcodecpInterface", u"192k", None))
        self.VcodecpIFcomboBox_3.setItemText(3, QCoreApplication.translate("VcodecpInterface", u"320k", None))
        self.VcodecpIFcomboBox_3.setItemText(4, QCoreApplication.translate("VcodecpInterface", u"512k", None))

        self.VcodecpIFlabel_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u7247\u5934\u65f6\u957f", None))
        self.VcodecpIFcheckBox_4.setText(QCoreApplication.translate("VcodecpInterface", u"\u52a0\u901f\u500d\u7387", None))
        self.VcodecpIFtimeEdit_3.setDisplayFormat(QCoreApplication.translate("VcodecpInterface", u"H:mm:ss:zzz", None))
        self.VcodecpIFcutsomFilter.setText(QCoreApplication.translate("VcodecpInterface", u"\u81ea\u5b9a\u4e49\u6ee4\u955c\u9884\u7559", None))
        self.VcodecpIFpushButton_4.setText(QCoreApplication.translate("VcodecpInterface", u"\u9009\u62e9\u7247\u5c3e", None))
        self.VcodecpIFlabel_9.setText(QCoreApplication.translate("VcodecpInterface", u"\u8fde\u63a5\u7247\u5c3e", None))
        self.VcodecpIFcheckBox_merge.setText(QCoreApplication.translate("VcodecpInterface", u"\u5408\u5e76\u89c6\u9891", None))
        self.VcodecpIFtFormat.setText(QCoreApplication.translate("VcodecpInterface", u"test", None))
        self.VcodecpIFpushButton_3.setText(QCoreApplication.translate("VcodecpInterface", u"\u9009\u62e9\u7247\u5934", None))
        self.VcodecpIFtimeEdit_2.setDisplayFormat(QCoreApplication.translate("VcodecpInterface", u"H:mm:ss:zzz", None))
        self.VcodecpIFlabel_8.setText(QCoreApplication.translate("VcodecpInterface", u"\u8fde\u63a5\u7247\u5934", None))
        self.VcodecpIFClearFil.setText(QCoreApplication.translate("VcodecpInterface", u"\u6e05\u9664\u8bbe\u7f6e", None))
        self.VcodecpIFradioButton.setText(QCoreApplication.translate("VcodecpInterface", u"\u7247\u5c3e\u65f6\u957f", None))
        self.VcodecpIFcheckBox_extract.setText(QCoreApplication.translate("VcodecpInterface", u"\u5207\u5272\u89c6\u9891", None))
        self.VcodecpIFradioButton_2.setText(QCoreApplication.translate("VcodecpInterface", u"\u7ed3\u675f\u65f6\u95f4", None))
    # retranslateUi

