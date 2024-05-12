# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vencoInterface.ui'
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
    QLabel, QLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, ComboBox, LineEdit, PlainTextEdit,
    PrimaryPushButton, SpinBox, TimeEdit)

class Ui_VcodecInterfacee(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 640)
        Form.setMinimumSize(QSize(960, 640))
        Form.setMaximumSize(QSize(1920, 1080))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.Title1 = QLabel(Form)
        self.Title1.setObjectName(u"Title1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title1.sizePolicy().hasHeightForWidth())
        self.Title1.setSizePolicy(sizePolicy)
        self.Title1.setMaximumSize(QSize(100, 64))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(28)
        font.setBold(True)
        font.setKerning(True)
        self.Title1.setFont(font)

        self.verticalLayout_4.addWidget(self.Title1)

        self.Title2 = QLabel(Form)
        self.Title2.setObjectName(u"Title2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Title2.sizePolicy().hasHeightForWidth())
        self.Title2.setSizePolicy(sizePolicy1)
        self.Title2.setMaximumSize(QSize(100, 45))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setKerning(True)
        self.Title2.setFont(font1)

        self.verticalLayout_4.addWidget(self.Title2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.console = PlainTextEdit(Form)
        self.console.setObjectName(u"console")
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QSize(640, 0))
        self.console.setMaximumSize(QSize(640, 96))
        self.console.setUndoRedoEnabled(False)
        self.console.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.console.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.console)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(480, 0))
        self.frame.setMaximumSize(QSize(16777215, 160))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title3_1 = QLabel(self.frame)
        self.Title3_1.setObjectName(u"Title3_1")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setKerning(True)
        self.Title3_1.setFont(font2)

        self.horizontalLayout.addWidget(self.Title3_1)

        self.lineEdit1 = LineEdit(self.frame)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setKerning(True)
        self.lineEdit1.setFont(font3)

        self.horizontalLayout.addWidget(self.lineEdit1)

        self.fileBtn_1 = QPushButton(self.frame)
        self.fileBtn_1.setObjectName(u"fileBtn_1")
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setKerning(True)
        self.fileBtn_1.setFont(font4)

        self.horizontalLayout.addWidget(self.fileBtn_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Title3_4 = QLabel(self.frame)
        self.Title3_4.setObjectName(u"Title3_4")
        self.Title3_4.setFont(font2)

        self.horizontalLayout_2.addWidget(self.Title3_4)

        self.lineEdit2 = LineEdit(self.frame)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setMinimumSize(QSize(0, 25))
        self.lineEdit2.setFont(font3)

        self.horizontalLayout_2.addWidget(self.lineEdit2)

        self.fileBtn_2 = QPushButton(self.frame)
        self.fileBtn_2.setObjectName(u"fileBtn_2")
        self.fileBtn_2.setFont(font4)

        self.horizontalLayout_2.addWidget(self.fileBtn_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Title3_8 = QLabel(self.frame)
        self.Title3_8.setObjectName(u"Title3_8")
        self.Title3_8.setFont(font2)

        self.horizontalLayout_6.addWidget(self.Title3_8)

        self.lineEdit4 = LineEdit(self.frame)
        self.lineEdit4.setObjectName(u"lineEdit4")
        self.lineEdit4.setMinimumSize(QSize(0, 25))
        self.lineEdit4.setFont(font3)

        self.horizontalLayout_6.addWidget(self.lineEdit4)

        self.fileBtn_4 = QPushButton(self.frame)
        self.fileBtn_4.setObjectName(u"fileBtn_4")
        self.fileBtn_4.setFont(font4)

        self.horizontalLayout_6.addWidget(self.fileBtn_4)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Title3_7 = QLabel(self.frame)
        self.Title3_7.setObjectName(u"Title3_7")
        self.Title3_7.setFont(font2)

        self.horizontalLayout_5.addWidget(self.Title3_7)

        self.lineEdit3 = LineEdit(self.frame)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setMinimumSize(QSize(0, 25))
        self.lineEdit3.setFont(font3)

        self.horizontalLayout_5.addWidget(self.lineEdit3)

        self.fileBtn_3 = QPushButton(self.frame)
        self.fileBtn_3.setObjectName(u"fileBtn_3")
        self.fileBtn_3.setFont(font4)

        self.horizontalLayout_5.addWidget(self.fileBtn_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.frame)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Title2_2 = QLabel(Form)
        self.Title2_2.setObjectName(u"Title2_2")
        self.Title2_2.setMaximumSize(QSize(16777215, 45))
        self.Title2_2.setFont(font1)

        self.horizontalLayout_8.addWidget(self.Title2_2)

        self.Title2_3 = QLabel(Form)
        self.Title2_3.setObjectName(u"Title2_3")
        sizePolicy1.setHeightForWidth(self.Title2_3.sizePolicy().hasHeightForWidth())
        self.Title2_3.setSizePolicy(sizePolicy1)
        self.Title2_3.setMinimumSize(QSize(240, 0))
        self.Title2_3.setMaximumSize(QSize(220, 16777215))
        self.Title2_3.setFont(font1)

        self.horizontalLayout_8.addWidget(self.Title2_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(670, 200))
        self.frame_2.setMaximumSize(QSize(16777215, 360))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(16)
        self.comboBox_5 = ComboBox(self.frame_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.comboBox_5, 4, 1, 1, 3)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setKerning(True)
        self.label_5.setFont(font5)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.checkBox_2 = CheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.comboBox_2 = ComboBox(self.frame_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setKerning(True)
        self.comboBox_2.setFont(font6)

        self.gridLayout.addWidget(self.comboBox_2, 0, 3, 1, 1)

        self.comboBox_3 = ComboBox(self.frame_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy3)
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setFont(font6)

        self.gridLayout.addWidget(self.comboBox_3, 3, 3, 1, 1)

        self.Title3_2 = QLabel(self.frame_2)
        self.Title3_2.setObjectName(u"Title3_2")
        self.Title3_2.setFont(font2)

        self.gridLayout.addWidget(self.Title3_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.lineEdit = LineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.spinBox = SpinBox(self.frame_2)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy2.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy2)
        self.spinBox.setMinimumSize(QSize(0, 30))
        self.spinBox.setFont(font6)
        self.spinBox.setMaximum(40000)
        self.spinBox.setValue(800)

        self.gridLayout.addWidget(self.spinBox, 2, 1, 1, 1)

        self.lineEdit_2 = LineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.checkBox_3 = CheckBox(self.frame_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)

        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)

        self.comboBox_4 = ComboBox(self.frame_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy3.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy3)
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setFont(font6)

        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)

        self.comboBox = ComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamilies([u"Microsoft YaHei UI"])
        font7.setPointSize(12)
        font7.setKerning(True)
        self.comboBox.setFont(font7)

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.spinBox_2 = SpinBox(self.frame_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy2.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy2)
        self.spinBox_2.setFont(font6)
        self.spinBox_2.setMaximum(51)
        self.spinBox_2.setValue(23)

        self.gridLayout.addWidget(self.spinBox_2, 2, 3, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)

        self.checkBox = CheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setSizeIncrement(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Microsoft YaHei UI"])
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setKerning(True)
        font8.setHintingPreference(QFont.PreferDefaultHinting)
        self.checkBox.setFont(font8)
        self.checkBox.setMouseTracking(True)
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.checkBox.setAutoExclusive(False)

        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)

        self.plainTextEdit = PlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font9 = QFont()
        font9.setPointSize(12)
        self.plainTextEdit.setFont(font9)

        self.gridLayout.addWidget(self.plainTextEdit, 5, 1, 1, 3)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_9.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(240, 200))
        self.frame_3.setMaximumSize(QSize(240, 360))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.Title3_3 = QLabel(self.frame_3)
        self.Title3_3.setObjectName(u"Title3_3")
        self.Title3_3.setFont(font5)

        self.verticalLayout_3.addWidget(self.Title3_3)

        self.timeEdit = TimeEdit(self.frame_3)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy4.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy4)
        self.timeEdit.setMinimumSize(QSize(150, 30))
        self.timeEdit.setFont(font6)

        self.verticalLayout_3.addWidget(self.timeEdit)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.verticalLayout_3.addWidget(self.label_2)

        self.timeEdit_2 = TimeEdit(self.frame_3)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMinimumSize(QSize(150, 30))
        self.timeEdit_2.setFont(font6)

        self.verticalLayout_3.addWidget(self.timeEdit_2)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushBtn = PrimaryPushButton(self.frame_3)
        self.pushBtn.setObjectName(u"pushBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushBtn.sizePolicy().hasHeightForWidth())
        self.pushBtn.setSizePolicy(sizePolicy5)
        self.pushBtn.setFont(font5)
        self.pushBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushBtn)


        self.horizontalLayout_9.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Form)
        self.comboBox_5.currentTextChanged.connect(self.plainTextEdit.setPlainText)

        self.pushBtn.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title1.setText(QCoreApplication.translate("Form", u"\u8f6c\u7801", None))
        self.Title2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6", None))
        self.Title3_1.setText(QCoreApplication.translate("Form", u"\u8f93\u5165", None))
        self.fileBtn_1.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.Title3_4.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.fileBtn_2.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.Title3_8.setText(QCoreApplication.translate("Form", u"\u5b57\u5e55", None))
        self.fileBtn_4.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.Title3_7.setText(QCoreApplication.translate("Form", u"\u97f3\u9891", None))
        self.fileBtn_3.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.Title2_2.setText(QCoreApplication.translate("Form", u"\u7f16\u7801\u8bbe\u7f6e", None))
        self.Title2_3.setText(QCoreApplication.translate("Form", u"\u5207\u5272\u8bbe\u7f6e", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u97f3\u9891\u7f16\u7801\u5668", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u7f16\u7801", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u5206\u8fa8\u7387", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u7801\u7387kbps", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"CRF\u54c1\u8d28-medium", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"CRF\u54c1\u8d28-fast", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"CBR\u5e73\u5747\u7801\u7387-medium", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"CBR\u5e73\u5747\u7801\u7387-fast", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"CQP\u786c\u7f16\u54c1\u8d28(*qsv)", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"128k", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"64k", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"192k", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"320k", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Form", u"512k", None))

        self.Title3_2.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u7f16\u7801\u5668", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u54c1\u8d28", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"1920x1080", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"60", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u7f16\u7801\u53c2\u6570", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u5e27\u7387", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"aac", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Form", u"alac", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Form", u"flac", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Form", u"opus", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("Form", u"copy", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("Form", u"custom", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"libx264", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"h264_nvenc", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"h264_qsv", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"h264_amf", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"copy", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"custom", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u97f3\u9891\u7f16\u7801\u53c2\u6570", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u9884\u8bbe", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u"-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k", None))
        self.Title3_3.setText(QCoreApplication.translate("Form", u"\u7247\u5934\u65f6\u957f", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("Form", u"H:mm:ss:zzz", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7247\u5c3e\u65f6\u957f", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("Form", u"H:mm:ss:zzz", None))
        self.pushBtn.setText(QCoreApplication.translate("Form", u"\u5904\u7406\u89c6\u9891", None))
    # retranslateUi

