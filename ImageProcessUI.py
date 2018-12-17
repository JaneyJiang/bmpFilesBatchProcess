# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\20181115\ProcessImage\QtViewer\ImageProcessor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
from PIL import ImageEnhance
from BmpAlphaImagePlugin import BmpAlphaImageFile
import BmpAlphaImagePlugin
import shutil
import os
import FinishedMessage

funD = {0:ImageEnhance.Brightness,
            1:ImageEnhance.Contrast,
            2:ImageEnhance.Color,
            3:ImageEnhance.Sharpness,
            }
def processInfo(mode,alpha):
    enhancePath = {0:'bri{:.2f}/'.format(alpha),
               1:'const{:.2f}/'.format(alpha),
               2:'color{:.2f}/'.format(alpha),
               3:'sharp{:.2f}/'.format(alpha),
               }
    return enhancePath[mode]

 #只返回一层文化件内容   
def file_name(filePath):
    for root, dirs, files in os.walk(filePath):
        return root,files


class Ui_Dialog(object):
    def setUnformatBmp(self,isChecked):
        self.isUnformatBmp = isChecked
    def setDirPath(self,dirpath):
        self.imageDir = dirpath
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 60, 181, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(14, 17, 18, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.enhanceMethodBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.enhanceMethodBox.setObjectName("enhanceMethodBox")
        self.enhanceMethodBox.addItem("")
        self.enhanceMethodBox.addItem("")
        self.enhanceMethodBox.addItem("")
        self.enhanceMethodBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enhanceMethodBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.enhanceAlpha = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enhanceAlpha.setObjectName("enhanceAlpha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enhanceAlpha)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 230, 165, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.buttonBox.accepted.connect(self.WholeImageProcess)
        #带参数的
        #self.buttonBox.accepted.connect(lambda: WholeImageProcess(mode,alpha))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "mode: "))
        self.enhanceMethodBox.setItemText(0, _translate("Dialog", "亮度"))
        self.enhanceMethodBox.setItemText(1, _translate("Dialog", "对比度"))
        self.enhanceMethodBox.setItemText(2, _translate("Dialog", "色彩"))
        self.enhanceMethodBox.setItemText(3, _translate("Dialog", "锐度"))
        self.label_2.setText(_translate("Dialog", "alpha:  "))
    
    def FinishedMessageWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = FinishedMessage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.exec_()

    def WholeImageProcess(self):
        orgImageDir,images = file_name(self.imageDir)
        alpha = float(self.enhanceAlpha.text())
        mode = self.enhanceMethodBox.currentIndex()
        AdditionalName = processInfo(mode,alpha)
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
                #BmpAlphaImagePlugin.setUnformatBmp(self.isUnformatBmp)
                #print(bool(self.isUnformatBmp))
                BmpAlphaImagePlugin.unformatBmp = bool(self.isUnformatBmp)
                im = BmpAlphaImageFile(imagePath)
                enhFunc = funD[mode](im)
                im = enhFunc.enhance(alpha)
                im.save(imageCopyPath)
        self.FinishedMessageWindow()
        #processFinished = QMessageBox.information(self,'提示',AdditionalName +' Finished!','ok')
    
    
        



        

