# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\20181115\ProcessImage\QtViewer\ChannelProcessor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BmpAlphaImagePlugin import BmpAlphaImageFile
import BmpAlphaImagePlugin
from PIL import Image
import shutil
import os
import FinishedMessage
def processInfo(mode,channel,alpha):
    if mode == 0:#加法运算
        enhancePath = {
            0:'R{:+d}/'.format(int(alpha)),
            1:'G{:+d}/'.format(int(alpha)),
            2:'B{:+d}/'.format(int(alpha)),
            3:'A{:+d}/'.format(int(alpha)),
            }
    else:#乘法运算
        enhancePath = {
            0:'Rx{:.2f}/'.format(alpha),
            1:'Gx{:.2f}/'.format(alpha),
            2:'Bx{:.2f}/'.format(alpha),
            3:'Ax{:.2f}/'.format(alpha),
            }

    return enhancePath[channel]

 #只返回一层文化件内容   
def file_name(filePath):
    for root, dirs, files in os.walk(filePath):
        return root,files

class ChannelProcess:
    def __init__(self,img):
        self.im = img
        self.source = img.split()
    def enhance(self,alpha,mode,channel):
        if mode == 0:#0为加法
            pro = self.source[channel].point(lambda i:i+alpha)
            self.source[channel].paste(pro)
            return Image.merge(self.im.mode,self.source)
        else:
            pro = self.source[channel].point(lambda i:i*alpha)
            self.source[channel].paste(pro)
            return Image.merge(self.im.mode,self.source)

class Ui_Dialog(object):
    def setUnformatBmp(self,isChecked):
        self.isUnformatBmp = isChecked
    def setDirPath(self,dirpath):
        self.imageDir = dirpath
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 311, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(16, 0, 16, 0)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.channelComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.channelComboBox.setObjectName("comboBox")
        self.channelComboBox.addItem("")
        self.channelComboBox.addItem("")
        self.channelComboBox.addItem("")
        self.channelComboBox.addItem("")
        self.horizontalLayout.addWidget(self.channelComboBox)
        self.operatorBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.operatorBox.setObjectName("operatorBox")
        self.operatorBox.addItem("")
        self.operatorBox.addItem("")
        self.horizontalLayout.addWidget(self.operatorBox)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.alphaValue = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.alphaValue.setObjectName("alphaValue")
        self.horizontalLayout.addWidget(self.alphaValue)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)#会让当前窗口消失，如果不想消失则不需要加这句
        self.buttonBox.accepted.connect(self.ChannelImageProcess)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.channelComboBox.setItemText(0, _translate("Dialog", "Red"))
        self.channelComboBox.setItemText(1, _translate("Dialog", "Green"))
        self.channelComboBox.setItemText(2, _translate("Dialog", "Blue"))
        self.channelComboBox.setItemText(3, _translate("Dialog", "A"))
        self.operatorBox.setItemText(0, _translate("Dialog", "Add"))
        self.operatorBox.setItemText(1, _translate("Dialog", "Multi"))
        self.label.setText(_translate("Dialog", "value: "))

    def FinishedMessageWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = FinishedMessage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.exec_()

    def ChannelImageProcess(self):
        orgImageDir,images = file_name(self.imageDir)
        alpha = float(self.alphaValue.text())
        mode = self.operatorBox.currentIndex()
        channel = self.channelComboBox.currentIndex()
        AdditionalName = processInfo(mode,channel,alpha)
        copyImageDir = orgImageDir + AdditionalName
        if not os.path.exists(copyImageDir):
            os.makedirs(copyImageDir)
        for image in images:
            imagePath = os.path.join(orgImageDir,image)
            imageCopyPath = os.path.join(copyImageDir,image)
            if image=='Thumbs.db':
                continue
            elif image[-4:]!='.bmp':
                shutil.copyfile(imagePath,imageCopyPath)
                continue
            else:
                BmpAlphaImagePlugin.unformatBmp = bool(self.isUnformatBmp)
                im = BmpAlphaImageFile(imagePath)
                cp = ChannelProcess(im)
                im = cp.enhance(alpha,mode,channel)
                im.save(imageCopyPath)

        self.FinishedMessageWindow()
        #processFinished = QMessageBox.information(self,'提示',AdditionalName+' Finished!','ok')