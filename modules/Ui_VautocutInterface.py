# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VautocutInterface.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, EditableComboBox, ListWidget, PlainTextEdit,
    PrimaryPushButton, PushButton, ScrollArea)

class Ui_VautocutInterface(object):
    def setupUi(self, VautocutInterface):
        if not VautocutInterface.objectName():
            VautocutInterface.setObjectName(u"VautocutInterface")
        VautocutInterface.resize(1085, 749)
        VautocutInterface.setMinimumSize(QSize(780, 0))
        self.verticalLayout = QVBoxLayout(VautocutInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VautocutscrollArea = ScrollArea(VautocutInterface)
        self.VautocutscrollArea.setObjectName(u"VautocutscrollArea")
        self.VautocutscrollArea.setMinimumSize(QSize(760, 0))
        self.VautocutscrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.VautocutscrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.VautocutscrollArea.setWidgetResizable(True)
        self.VautocutfacescrollAreaWidgetContents = QWidget()
        self.VautocutfacescrollAreaWidgetContents.setObjectName(u"VautocutfacescrollAreaWidgetContents")
        self.VautocutfacescrollAreaWidgetContents.setGeometry(QRect(0, 0, 1067, 731))
        self.verticalLayout_3 = QVBoxLayout(self.VautocutfacescrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Vautocutbox01 = QHBoxLayout()
        self.Vautocutbox01.setSpacing(20)
        self.Vautocutbox01.setObjectName(u"Vautocutbox01")
        self.Vautocutbox01.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.VautocutverticalLayout_4 = QVBoxLayout()
        self.VautocutverticalLayout_4.setObjectName(u"VautocutverticalLayout_4")
        self.VautocutverticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.VautocutTitle1 = QLabel(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutTitle1.setObjectName(u"VautocutTitle1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VautocutTitle1.sizePolicy().hasHeightForWidth())
        self.VautocutTitle1.setSizePolicy(sizePolicy)
        self.VautocutTitle1.setMaximumSize(QSize(150, 64))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.VautocutTitle1.setFont(font)

        self.VautocutverticalLayout_4.addWidget(self.VautocutTitle1)

        self.VautocutTitle2 = QLabel(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutTitle2.setObjectName(u"VautocutTitle2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VautocutTitle2.sizePolicy().hasHeightForWidth())
        self.VautocutTitle2.setSizePolicy(sizePolicy1)
        self.VautocutTitle2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.VautocutTitle2.setFont(font1)

        self.VautocutverticalLayout_4.addWidget(self.VautocutTitle2)


        self.Vautocutbox01.addLayout(self.VautocutverticalLayout_4)

        self.Vautocutlabel = QLabel(self.VautocutfacescrollAreaWidgetContents)
        self.Vautocutlabel.setObjectName(u"Vautocutlabel")
        self.Vautocutlabel.setMaximumSize(QSize(16777215, 80))

        self.Vautocutbox01.addWidget(self.Vautocutlabel)

        self.VautocuthorizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Vautocutbox01.addItem(self.VautocuthorizontalSpacer)

        self.VautocutpushBtn = PrimaryPushButton(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutpushBtn.setObjectName(u"VautocutpushBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.VautocutpushBtn.sizePolicy().hasHeightForWidth())
        self.VautocutpushBtn.setSizePolicy(sizePolicy2)
        self.VautocutpushBtn.setMinimumSize(QSize(240, 60))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        self.VautocutpushBtn.setFont(font2)
        self.VautocutpushBtn.setFlat(False)

        self.Vautocutbox01.addWidget(self.VautocutpushBtn)

        self.VautocutSTBtn = QPushButton(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutSTBtn.setObjectName(u"VautocutSTBtn")
        self.VautocutSTBtn.setMinimumSize(QSize(120, 60))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.VautocutSTBtn.setFont(font3)

        self.Vautocutbox01.addWidget(self.VautocutSTBtn)

        self.VautocutpushBtn_2 = PushButton(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutpushBtn_2.setObjectName(u"VautocutpushBtn_2")
        self.VautocutpushBtn_2.setMinimumSize(QSize(80, 60))
        self.VautocutpushBtn_2.setFont(font3)

        self.Vautocutbox01.addWidget(self.VautocutpushBtn_2)


        self.verticalLayout_3.addLayout(self.Vautocutbox01)

        self.Vautocutbox02 = QFrame(self.VautocutfacescrollAreaWidgetContents)
        self.Vautocutbox02.setObjectName(u"Vautocutbox02")
        self.Vautocutbox02.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Vautocutbox02.sizePolicy().hasHeightForWidth())
        self.Vautocutbox02.setSizePolicy(sizePolicy3)
        self.Vautocutbox02.setMinimumSize(QSize(480, 145))
        self.Vautocutbox02.setMaximumSize(QSize(16777215, 240))
        self.Vautocutbox02.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vautocutbox02.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.Vautocutbox02)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Vautocutinputfile = PushButton(self.Vautocutbox02)
        self.Vautocutinputfile.setObjectName(u"Vautocutinputfile")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.Vautocutinputfile.setFont(font4)

        self.gridLayout.addWidget(self.Vautocutinputfile, 0, 0, 1, 1)

        self.Vautocutinputclear = PushButton(self.Vautocutbox02)
        self.Vautocutinputclear.setObjectName(u"Vautocutinputclear")
        self.Vautocutinputclear.setFont(font4)

        self.gridLayout.addWidget(self.Vautocutinputclear, 0, 1, 1, 1)

        self.Vautocutoutputfolder = QPushButton(self.Vautocutbox02)
        self.Vautocutoutputfolder.setObjectName(u"Vautocutoutputfolder")
        self.Vautocutoutputfolder.setFont(font4)

        self.gridLayout.addWidget(self.Vautocutoutputfolder, 0, 2, 1, 1)

        self.Vautocutinputlist = ListWidget(self.Vautocutbox02)
        self.Vautocutinputlist.setObjectName(u"Vautocutinputlist")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Vautocutinputlist.sizePolicy().hasHeightForWidth())
        self.Vautocutinputlist.setSizePolicy(sizePolicy4)
        self.Vautocutinputlist.setMinimumSize(QSize(0, 120))
        self.Vautocutinputlist.setMaximumSize(QSize(16777215, 200))
        self.Vautocutinputlist.setAcceptDrops(True)
        self.Vautocutinputlist.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Vautocutinputlist.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Vautocutinputlist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Vautocutinputlist.setDragEnabled(False)

        self.gridLayout.addWidget(self.Vautocutinputlist, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.Vautocutbox02)

        self.Vautocutbox03 = QHBoxLayout()
        self.Vautocutbox03.setObjectName(u"Vautocutbox03")
        self.VautocutTitle2_3 = QLabel(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutTitle2_3.setObjectName(u"VautocutTitle2_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.VautocutTitle2_3.sizePolicy().hasHeightForWidth())
        self.VautocutTitle2_3.setSizePolicy(sizePolicy5)
        self.VautocutTitle2_3.setMinimumSize(QSize(240, 45))
        self.VautocutTitle2_3.setMaximumSize(QSize(600, 16777215))
        self.VautocutTitle2_3.setFont(font1)

        self.Vautocutbox03.addWidget(self.VautocutTitle2_3)

        self.VautocutTitle2_2 = QLabel(self.VautocutfacescrollAreaWidgetContents)
        self.VautocutTitle2_2.setObjectName(u"VautocutTitle2_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.VautocutTitle2_2.sizePolicy().hasHeightForWidth())
        self.VautocutTitle2_2.setSizePolicy(sizePolicy6)
        self.VautocutTitle2_2.setMinimumSize(QSize(60, 45))
        self.VautocutTitle2_2.setMaximumSize(QSize(240, 45))
        self.VautocutTitle2_2.setFont(font1)

        self.Vautocutbox03.addWidget(self.VautocutTitle2_2)


        self.verticalLayout_3.addLayout(self.Vautocutbox03)

        self.Vautocutbox04 = QHBoxLayout()
        self.Vautocutbox04.setObjectName(u"Vautocutbox04")
        self.Vautocutframe_2 = QFrame(self.VautocutfacescrollAreaWidgetContents)
        self.Vautocutframe_2.setObjectName(u"Vautocutframe_2")
        sizePolicy6.setHeightForWidth(self.Vautocutframe_2.sizePolicy().hasHeightForWidth())
        self.Vautocutframe_2.setSizePolicy(sizePolicy6)
        self.Vautocutframe_2.setMinimumSize(QSize(600, 360))
        self.Vautocutframe_2.setMaximumSize(QSize(600, 360))
        self.Vautocutframe_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vautocutframe_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Vautocutframe_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VautocutgridLayout = QGridLayout()
        self.VautocutgridLayout.setObjectName(u"VautocutgridLayout")
        self.VautocutgridLayout.setHorizontalSpacing(24)
        self.VautocutgridLayout.setVerticalSpacing(16)
        self.VautocutlineEditVE = EditableComboBox(self.Vautocutframe_2)
        self.VautocutlineEditVE.setObjectName(u"VautocutlineEditVE")
        self.VautocutlineEditVE.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setPointSize(12)
        self.VautocutlineEditVE.setFont(font5)
        self.VautocutlineEditVE.setReadOnly(False)

        self.VautocutgridLayout.addWidget(self.VautocutlineEditVE, 0, 1, 1, 1)

        self.Vautocutlabel_4 = QLabel(self.Vautocutframe_2)
        self.Vautocutlabel_4.setObjectName(u"Vautocutlabel_4")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setKerning(True)
        self.Vautocutlabel_4.setFont(font6)

        self.VautocutgridLayout.addWidget(self.Vautocutlabel_4, 1, 2, 1, 1)

        self.VautocutradioButton_3 = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton_3.setObjectName(u"VautocutradioButton_3")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton_3, 3, 2, 1, 1)

        self.VautocutradioButton = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton.setObjectName(u"VautocutradioButton")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton, 3, 0, 1, 1)

        self.Vautocutlabel_2 = QLabel(self.Vautocutframe_2)
        self.Vautocutlabel_2.setObjectName(u"Vautocutlabel_2")
        self.Vautocutlabel_2.setFont(font6)

        self.VautocutgridLayout.addWidget(self.Vautocutlabel_2, 0, 2, 1, 1)

        self.VautocutradioButton_4 = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton_4.setObjectName(u"VautocutradioButton_4")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton_4, 3, 3, 1, 1)

        self.VautocutradioButton_2 = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton_2.setObjectName(u"VautocutradioButton_2")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton_2, 3, 1, 1, 1)

        self.Vautocutlabel_3 = QLabel(self.Vautocutframe_2)
        self.Vautocutlabel_3.setObjectName(u"Vautocutlabel_3")
        self.Vautocutlabel_3.setFont(font6)

        self.VautocutgridLayout.addWidget(self.Vautocutlabel_3, 1, 0, 1, 1)

        self.VcodecpIFplainTextEdit = PlainTextEdit(self.Vautocutframe_2)
        self.VcodecpIFplainTextEdit.setObjectName(u"VcodecpIFplainTextEdit")
        self.VcodecpIFplainTextEdit.setFont(font5)

        self.VautocutgridLayout.addWidget(self.VcodecpIFplainTextEdit, 5, 1, 1, 3)

        self.VautocutTitle3_2 = QLabel(self.Vautocutframe_2)
        self.VautocutTitle3_2.setObjectName(u"VautocutTitle3_2")
        self.VautocutTitle3_2.setFont(font6)

        self.VautocutgridLayout.addWidget(self.VautocutTitle3_2, 0, 0, 1, 1)

        self.VautocutcomboBox_3 = ComboBox(self.Vautocutframe_2)
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.addItem("")
        self.VautocutcomboBox_3.setObjectName(u"VautocutcomboBox_3")
        sizePolicy3.setHeightForWidth(self.VautocutcomboBox_3.sizePolicy().hasHeightForWidth())
        self.VautocutcomboBox_3.setSizePolicy(sizePolicy3)
        self.VautocutcomboBox_3.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setKerning(True)
        self.VautocutcomboBox_3.setFont(font7)

        self.VautocutgridLayout.addWidget(self.VautocutcomboBox_3, 1, 3, 1, 1)

        self.Vautocutlabel_5 = QLabel(self.Vautocutframe_2)
        self.Vautocutlabel_5.setObjectName(u"Vautocutlabel_5")
        self.Vautocutlabel_5.setFont(font2)

        self.VautocutgridLayout.addWidget(self.Vautocutlabel_5, 5, 0, 1, 1)

        self.VautocutlineEditAE = EditableComboBox(self.Vautocutframe_2)
        self.VautocutlineEditAE.setObjectName(u"VautocutlineEditAE")
        self.VautocutlineEditAE.setMinimumSize(QSize(0, 30))
        self.VautocutlineEditAE.setFont(font5)
        self.VautocutlineEditAE.setReadOnly(False)

        self.VautocutgridLayout.addWidget(self.VautocutlineEditAE, 1, 1, 1, 1)

        self.VautocutlineEdit = EditableComboBox(self.Vautocutframe_2)
        self.VautocutlineEdit.setObjectName(u"VautocutlineEdit")
        self.VautocutlineEdit.setFont(font5)

        self.VautocutgridLayout.addWidget(self.VautocutlineEdit, 0, 3, 1, 1)

        self.VautocutcheckBox = QCheckBox(self.Vautocutframe_2)
        self.VautocutcheckBox.setObjectName(u"VautocutcheckBox")

        self.VautocutgridLayout.addWidget(self.VautocutcheckBox, 2, 0, 1, 1)

        self.VautocutradioButton_5 = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton_5.setObjectName(u"VautocutradioButton_5")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton_5, 2, 1, 1, 1)

        self.VautocutradioButton_11 = QRadioButton(self.Vautocutframe_2)
        self.VautocutradioButton_11.setObjectName(u"VautocutradioButton_11")

        self.VautocutgridLayout.addWidget(self.VautocutradioButton_11, 2, 2, 1, 1)

        self.VautocutcheckBox_2 = QCheckBox(self.Vautocutframe_2)
        self.VautocutcheckBox_2.setObjectName(u"VautocutcheckBox_2")

        self.VautocutgridLayout.addWidget(self.VautocutcheckBox_2, 2, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.VautocutgridLayout)


        self.Vautocutbox04.addWidget(self.Vautocutframe_2)

        self.Vautocutframe_3 = QFrame(self.VautocutfacescrollAreaWidgetContents)
        self.Vautocutframe_3.setObjectName(u"Vautocutframe_3")
        sizePolicy6.setHeightForWidth(self.Vautocutframe_3.sizePolicy().hasHeightForWidth())
        self.Vautocutframe_3.setSizePolicy(sizePolicy6)
        self.Vautocutframe_3.setMinimumSize(QSize(280, 360))
        self.Vautocutframe_3.setMaximumSize(QSize(480, 360))
        self.Vautocutframe_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vautocutframe_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.Vautocutframe_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VautocutdoubleSpinBox = QDoubleSpinBox(self.Vautocutframe_3)
        self.VautocutdoubleSpinBox.setObjectName(u"VautocutdoubleSpinBox")
        self.VautocutdoubleSpinBox.setFont(font5)
        self.VautocutdoubleSpinBox.setDecimals(2)
        self.VautocutdoubleSpinBox.setMaximum(99.000000000000000)
        self.VautocutdoubleSpinBox.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.VautocutdoubleSpinBox, 0, 1, 1, 1)

        self.VautocutdoubleSpinBox_4 = QDoubleSpinBox(self.Vautocutframe_3)
        self.VautocutdoubleSpinBox_4.setObjectName(u"VautocutdoubleSpinBox_4")
        self.VautocutdoubleSpinBox_4.setFont(font5)
        self.VautocutdoubleSpinBox_4.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.VautocutdoubleSpinBox_4, 1, 1, 1, 1)

        self.Vautocutlabel_9 = QLabel(self.Vautocutframe_3)
        self.Vautocutlabel_9.setObjectName(u"Vautocutlabel_9")
        self.Vautocutlabel_9.setMaximumSize(QSize(120, 16777215))
        self.Vautocutlabel_9.setFont(font5)

        self.gridLayout_3.addWidget(self.Vautocutlabel_9, 2, 0, 1, 1)

        self.Vautocutframe = QFrame(self.Vautocutframe_3)
        self.Vautocutframe.setObjectName(u"Vautocutframe")
        self.Vautocutframe.setMaximumSize(QSize(16777215, 160))
        self.Vautocutframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.Vautocutframe.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.Vautocutframe)
        self.formLayout.setObjectName(u"formLayout")
        self.Vautocutlabel_7 = QLabel(self.Vautocutframe)
        self.Vautocutlabel_7.setObjectName(u"Vautocutlabel_7")
        self.Vautocutlabel_7.setMaximumSize(QSize(16777215, 30))
        self.Vautocutlabel_7.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Vautocutlabel_7)

        self.VautocutradioButton_6 = QRadioButton(self.Vautocutframe)
        self.VautocutradioButton_6.setObjectName(u"VautocutradioButton_6")
        font8 = QFont()
        font8.setPointSize(10)
        self.VautocutradioButton_6.setFont(font8)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.VautocutradioButton_6)

        self.VautocutradioButton_7 = QRadioButton(self.Vautocutframe)
        self.VautocutradioButton_7.setObjectName(u"VautocutradioButton_7")
        self.VautocutradioButton_7.setFont(font8)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.VautocutradioButton_7)

        self.VautocutradioButton_8 = QRadioButton(self.Vautocutframe)
        self.VautocutradioButton_8.setObjectName(u"VautocutradioButton_8")
        self.VautocutradioButton_8.setFont(font8)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.VautocutradioButton_8)

        self.VautocutradioButton_9 = QRadioButton(self.Vautocutframe)
        self.VautocutradioButton_9.setObjectName(u"VautocutradioButton_9")
        self.VautocutradioButton_9.setFont(font8)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.VautocutradioButton_9)

        self.VautocutradioButton_10 = QRadioButton(self.Vautocutframe)
        self.VautocutradioButton_10.setObjectName(u"VautocutradioButton_10")
        self.VautocutradioButton_10.setFont(font8)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.VautocutradioButton_10)

        self.VautocutlineEdit_2 = QLineEdit(self.Vautocutframe)
        self.VautocutlineEdit_2.setObjectName(u"VautocutlineEdit_2")
        self.VautocutlineEdit_2.setMaximumSize(QSize(240, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.VautocutlineEdit_2)

        self.VautocutlineEdit_3 = QLineEdit(self.Vautocutframe)
        self.VautocutlineEdit_3.setObjectName(u"VautocutlineEdit_3")
        self.VautocutlineEdit_3.setMaximumSize(QSize(240, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.VautocutlineEdit_3)

        self.VautocutlineEdit_4 = QLineEdit(self.Vautocutframe)
        self.VautocutlineEdit_4.setObjectName(u"VautocutlineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.VautocutlineEdit_4)


        self.gridLayout_3.addWidget(self.Vautocutframe, 5, 0, 1, 2)

        self.Vautocutlabel_11 = QLabel(self.Vautocutframe_3)
        self.Vautocutlabel_11.setObjectName(u"Vautocutlabel_11")
        self.Vautocutlabel_11.setMaximumSize(QSize(120, 16777215))
        self.Vautocutlabel_11.setFont(font5)

        self.gridLayout_3.addWidget(self.Vautocutlabel_11, 1, 0, 1, 1)

        self.VautocutdoubleSpinBox_3 = QDoubleSpinBox(self.Vautocutframe_3)
        self.VautocutdoubleSpinBox_3.setObjectName(u"VautocutdoubleSpinBox_3")
        self.VautocutdoubleSpinBox_3.setFont(font5)
        self.VautocutdoubleSpinBox_3.setMaximum(9999.000000000000000)
        self.VautocutdoubleSpinBox_3.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.VautocutdoubleSpinBox_3, 3, 1, 1, 1)

        self.Vautocutlabel_8 = QLabel(self.Vautocutframe_3)
        self.Vautocutlabel_8.setObjectName(u"Vautocutlabel_8")
        self.Vautocutlabel_8.setMaximumSize(QSize(120, 16777215))
        self.Vautocutlabel_8.setFont(font5)

        self.gridLayout_3.addWidget(self.Vautocutlabel_8, 0, 0, 1, 1)

        self.Vautocutlabel_10 = QLabel(self.Vautocutframe_3)
        self.Vautocutlabel_10.setObjectName(u"Vautocutlabel_10")
        self.Vautocutlabel_10.setMaximumSize(QSize(120, 16777215))
        self.Vautocutlabel_10.setFont(font5)

        self.gridLayout_3.addWidget(self.Vautocutlabel_10, 3, 0, 1, 1)

        self.VautocutdoubleSpinBox_2 = QDoubleSpinBox(self.Vautocutframe_3)
        self.VautocutdoubleSpinBox_2.setObjectName(u"VautocutdoubleSpinBox_2")
        self.VautocutdoubleSpinBox_2.setFont(font5)
        self.VautocutdoubleSpinBox_2.setMaximum(9999.000000000000000)
        self.VautocutdoubleSpinBox_2.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.VautocutdoubleSpinBox_2, 2, 1, 1, 1)

        self.Vautocutlabel_6 = QLabel(self.Vautocutframe_3)
        self.Vautocutlabel_6.setObjectName(u"Vautocutlabel_6")
        self.Vautocutlabel_6.setMaximumSize(QSize(120, 16777215))
        self.Vautocutlabel_6.setFont(font5)

        self.gridLayout_3.addWidget(self.Vautocutlabel_6, 4, 0, 1, 1)

        self.VautocutdoubleSpinBox_5 = QDoubleSpinBox(self.Vautocutframe_3)
        self.VautocutdoubleSpinBox_5.setObjectName(u"VautocutdoubleSpinBox_5")
        self.VautocutdoubleSpinBox_5.setFont(font5)
        self.VautocutdoubleSpinBox_5.setMinimum(0.500000000000000)
        self.VautocutdoubleSpinBox_5.setMaximum(2.000000000000000)
        self.VautocutdoubleSpinBox_5.setSingleStep(0.050000000000000)
        self.VautocutdoubleSpinBox_5.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.VautocutdoubleSpinBox_5, 4, 1, 1, 1)


        self.Vautocutbox04.addWidget(self.Vautocutframe_3)


        self.verticalLayout_3.addLayout(self.Vautocutbox04)

        self.VautocutscrollArea.setWidget(self.VautocutfacescrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.VautocutscrollArea)


        self.retranslateUi(VautocutInterface)

        self.VautocutpushBtn.setDefault(True)


        QMetaObject.connectSlotsByName(VautocutInterface)
    # setupUi

    def retranslateUi(self, VautocutInterface):
        VautocutInterface.setWindowTitle(QCoreApplication.translate("VautocutInterface", u"Form", None))
        self.VautocutTitle1.setText(QCoreApplication.translate("VautocutInterface", u"\u81ea\u52a8\u526a\u8f91", None))
        self.VautocutTitle2.setText(QCoreApplication.translate("VautocutInterface", u"\u89c6\u9891", None))
        self.Vautocutlabel.setText(QCoreApplication.translate("VautocutInterface", u"\u57fa\u4e8eauto-editor\u7684\u81ea\u52a8\u526a\u8f91", None))
        self.VautocutpushBtn.setText(QCoreApplication.translate("VautocutInterface", u"\u5904\u7406\u89c6\u9891", None))
        self.VautocutSTBtn.setText(QCoreApplication.translate("VautocutInterface", u"\u4e2d\u6b62\u5904\u7406", None))
        self.VautocutpushBtn_2.setText(QCoreApplication.translate("VautocutInterface", u"\u89e3\u51bb", None))
        self.Vautocutinputfile.setText(QCoreApplication.translate("VautocutInterface", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.Vautocutinputclear.setText(QCoreApplication.translate("VautocutInterface", u"\u6e05\u9664", None))
        self.Vautocutoutputfolder.setText(QCoreApplication.translate("VautocutInterface", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.VautocutTitle2_3.setText(QCoreApplication.translate("VautocutInterface", u"\u7f16\u7801\u8bbe\u7f6e", None))
        self.VautocutTitle2_2.setText(QCoreApplication.translate("VautocutInterface", u"\u81ea\u52a8\u526a\u8f91\u8bbe\u7f6e", None))
        self.VautocutlineEditVE.setText(QCoreApplication.translate("VautocutInterface", u"default", None))
        self.Vautocutlabel_4.setText(QCoreApplication.translate("VautocutInterface", u"\u97f3\u9891\u7f16\u7801\u53c2\u6570", None))
        self.VautocutradioButton_3.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51fashotcut", None))
        self.VautocutradioButton.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51fapremiere", None))
        self.Vautocutlabel_2.setText(QCoreApplication.translate("VautocutInterface", u"\u89c6\u9891\u7f16\u7801\u53c2\u6570", None))
        self.VautocutradioButton_4.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51fa\u5207\u7247", None))
        self.VautocutradioButton_2.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51faresolve", None))
        self.Vautocutlabel_3.setText(QCoreApplication.translate("VautocutInterface", u"\u97f3\u9891\u7f16\u7801\u5668", None))
        self.VcodecpIFplainTextEdit.setPlainText("")
        self.VautocutTitle3_2.setText(QCoreApplication.translate("VautocutInterface", u"\u89c6\u9891\u7f16\u7801\u5668", None))
        self.VautocutcomboBox_3.setItemText(0, QCoreApplication.translate("VautocutInterface", u"256k", None))
        self.VautocutcomboBox_3.setItemText(1, QCoreApplication.translate("VautocutInterface", u"128k", None))
        self.VautocutcomboBox_3.setItemText(2, QCoreApplication.translate("VautocutInterface", u"64k", None))
        self.VautocutcomboBox_3.setItemText(3, QCoreApplication.translate("VautocutInterface", u"192k", None))
        self.VautocutcomboBox_3.setItemText(4, QCoreApplication.translate("VautocutInterface", u"320k", None))
        self.VautocutcomboBox_3.setItemText(5, QCoreApplication.translate("VautocutInterface", u"512k", None))

        self.Vautocutlabel_5.setText(QCoreApplication.translate("VautocutInterface", u"\u81ea\u5b9a\u4e49\u7f16\u7801", None))
        self.VautocutlineEditAE.setText(QCoreApplication.translate("VautocutInterface", u"default", None))
        self.VautocutcheckBox.setText(QCoreApplication.translate("VautocutInterface", u"\u97f3\u9891\u6807\u51c6\u5316", None))
        self.VautocutradioButton_5.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51faWAV", None))
        self.VautocutradioButton_11.setText(QCoreApplication.translate("VautocutInterface", u"\u5bfc\u51fa\u89c6\u9891", None))
        self.VautocutcheckBox_2.setText(QCoreApplication.translate("VautocutInterface", u"\u5de5\u7a0b\u4e0d\u5220\u9664silent", None))
        self.Vautocutlabel_9.setText(QCoreApplication.translate("VautocutInterface", u"\u7247\u5934\u65f6\u957f", None))
        self.Vautocutlabel_7.setText(QCoreApplication.translate("VautocutInterface", u"\u81ea\u52a8\u526a\u8f91\u9608\u503c\u8bbe\u7f6e", None))
        self.VautocutradioButton_6.setText(QCoreApplication.translate("VautocutInterface", u"\u97f3\u9891\u9608\u503c", None))
        self.VautocutradioButton_7.setText(QCoreApplication.translate("VautocutInterface", u"\u89c6\u9891\u9608\u503c", None))
        self.VautocutradioButton_8.setText(QCoreApplication.translate("VautocutInterface", u"\u97f3\u89c6\u9891\u9608\u503c", None))
        self.VautocutradioButton_9.setText(QCoreApplication.translate("VautocutInterface", u"\u4e0d\u8fdb\u884c\u81ea\u52a8\u526a\u8f91", None))
        self.VautocutradioButton_10.setText(QCoreApplication.translate("VautocutInterface", u"\u9ed8\u8ba4", None))
        self.VautocutlineEdit_2.setText(QCoreApplication.translate("VautocutInterface", u"audio:threshold=0.04", None))
        self.VautocutlineEdit_3.setText(QCoreApplication.translate("VautocutInterface", u"motion:threshold=0.02,blur=3", None))
        self.VautocutlineEdit_4.setText(QCoreApplication.translate("VautocutInterface", u"(or audio:4% motion:2%,blur=3)", None))
        self.Vautocutlabel_11.setText(QCoreApplication.translate("VautocutInterface", u"margin-after", None))
        self.Vautocutlabel_8.setText(QCoreApplication.translate("VautocutInterface", u"margin-before", None))
        self.Vautocutlabel_10.setText(QCoreApplication.translate("VautocutInterface", u"\u7247\u5c3e\u65f6\u957f", None))
        self.Vautocutlabel_6.setText(QCoreApplication.translate("VautocutInterface", u"\u53d8\u901f\u500d\u7387", None))
    # retranslateUi

