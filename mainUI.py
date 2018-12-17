# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\20181115\ProcessImage\QtViewer\mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ImageProcessUI
import ChannelProcessorUI

class Ui_MainWindow(object):
    #打开其他窗体的调用，一定得用self.value来定义窗体，如果用一个临时变量，则窗体会一闪而过，不能停留。
    def wholeImageWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = ImageProcessUI.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.setDirPath(self.dirPath)
        self.ui.setUnformatBmp(self.unformatRadioButton.isChecked)
        self.window.show()
        self.window.exec_()

    def channelImageWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = ChannelProcessorUI.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.setDirPath(self.dirPath)
        self.ui.setUnformatBmp(self.unformatRadioButton.isChecked)
        self.window.show()
        self.window.exec_()
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 463)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(230, 100, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFileButton.sizePolicy().hasHeightForWidth())
        self.openFileButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.openFileButton.setFont(font)
        self.openFileButton.setObjectName("openFileButton")
        self.unformatRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.unformatRadioButton.setEnabled(False)
        self.unformatRadioButton.setChecked(True)
        self.unformatRadioButton.setGeometry(QtCore.QRect(380, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        self.unformatRadioButton.setFont(font)
        self.unformatRadioButton.setObjectName("unformatRadioButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 220, 341, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wholeImageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wholeImageButton.sizePolicy().hasHeightForWidth())
        self.wholeImageButton.setSizePolicy(sizePolicy)
        self.wholeImageButton.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.wholeImageButton.setFont(font)
        self.wholeImageButton.setObjectName("wholeImageButton")
        self.horizontalLayout.addWidget(self.wholeImageButton)
        self.channelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channelButton.sizePolicy().hasHeightForWidth())
        self.channelButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.channelButton.setFont(font)
        self.channelButton.setObjectName("channelButton")
        self.horizontalLayout.addWidget(self.channelButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 160, 331, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.openFileButton.clicked.connect(self.selectDir)
        self.wholeImageButton.clicked.connect(self.wholeImageWindow)
        self.channelButton.clicked.connect(self.channelImageWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFileButton.setText(_translate("MainWindow", "选择文件夹"))
        self.unformatRadioButton.setText(_translate("MainWindow", "iQue非标准图片"))
        self.wholeImageButton.setText(_translate("MainWindow", "整张图像处理"))
        self.channelButton.setText(_translate("MainWindow", "图像通道处理"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "bmp图像处理工具"))

    def printMessage(self):
        print("choose files")
    
    def selectDir(self):
        #file_name = QtWidgets.QFileDialog.getOpenFileName(self,"open file dialog","","Txt files(*.txt)")
        self.dirPath =QtWidgets.QFileDialog.getExistingDirectory(None,"choose directory",os.getcwd())
        self.label.setText("loaded Directory: "+self.dirPath)