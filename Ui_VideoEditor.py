# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 546)
        MainWindow.setMouseTracking(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 2, 22, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 14, 0, 1, 1)

        self.importBn3 = QPushButton(self.centralwidget)
        self.importBn3.setObjectName(u"importBn3")

        self.gridLayout.addWidget(self.importBn3, 14, 1, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 11, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 19, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.exportBn2 = QPushButton(self.centralwidget)
        self.exportBn2.setObjectName(u"exportBn2")

        self.gridLayout.addWidget(self.exportBn2, 15, 1, 1, 1)

        self.importBn1 = QPushButton(self.centralwidget)
        self.importBn1.setObjectName(u"importBn1")

        self.gridLayout.addWidget(self.importBn1, 2, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 16, 1, 1, 1)

        self.line2 = QLineEdit(self.centralwidget)
        self.line2.setObjectName(u"line2")
        self.line2.setDragEnabled(False)

        self.gridLayout.addWidget(self.line2, 19, 1, 1, 1)

        self.time2 = QTimeEdit(self.centralwidget)
        self.time2.setObjectName(u"time2")

        self.gridLayout.addWidget(self.time2, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.exportBn1 = QPushButton(self.centralwidget)
        self.exportBn1.setObjectName(u"exportBn1")

        self.gridLayout.addWidget(self.exportBn1, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 21, 1, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 22, 0, 1, 3)

        self.time1 = QTimeEdit(self.centralwidget)
        self.time1.setObjectName(u"time1")
        self.time1.setEnabled(True)
        self.time1.setMinimumSize(QSize(140, 30))

        self.gridLayout.addWidget(self.time1, 5, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.importBn4 = QPushButton(self.centralwidget)
        self.importBn4.setObjectName(u"importBn4")

        self.gridLayout.addWidget(self.importBn4, 12, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 1, 1, 1)

        self.line = QLineEdit(self.centralwidget)
        self.line.setObjectName(u"line")

        self.gridLayout.addWidget(self.line, 7, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)

        self.importBn2 = QPushButton(self.centralwidget)
        self.importBn2.setObjectName(u"importBn2")

        self.gridLayout.addWidget(self.importBn2, 13, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 12, 0, 1, 1)

        self.pushButtonF = QPushButton(self.centralwidget)
        self.pushButtonF.setObjectName(u"pushButtonF")

        self.gridLayout.addWidget(self.pushButtonF, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")

        self.verticalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")

        self.verticalLayout.addWidget(self.pushButton2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7247\u5934\u7247\u5c3e\u6279\u5904\u7406", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u4ee3\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6\u5939", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7247\u5c3e\u6587\u4ef6", None))
        self.importBn3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u7247\u5934\u7247\u5c3e\u5408\u5e76\u6d41\u7a0b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7247\u5c3e\u65f6\u95f4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7f16\u7801\u683c\u5f0f", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7247\u5934\u7247\u5c3e\u5207\u5272\u6d41\u7a0b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5207\u5272\u8f93\u51fa", None))
        self.exportBn2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.importBn1.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7f16\u7801\u683c\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7247\u5934\u6587\u4ef6", None))
        self.line2.setText(QCoreApplication.translate("MainWindow", u"-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2", None))
        self.time2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss.zzz", None))
        self.exportBn1.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.time1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss.zzz", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7247\u5934\u65f6\u95f4", None))
        self.importBn4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.line.setText(QCoreApplication.translate("MainWindow", u"-c:v copy -c:a copy", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5408\u5e76\u8f93\u51fa", None))
        self.importBn2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6\u5939", None))
        self.pushButtonF.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u6574ffmpeg", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"Start Extract", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Start Concat", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

