# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\20181115\ProcessImage\QtViewer\ChannelProcessor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 350, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 0, 16, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.redCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.redCheckBox.setObjectName("redCheckBox")
        self.horizontalLayout.addWidget(self.redCheckBox)
        self.operatorRedBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.operatorRedBox.setObjectName("operatorRedBox")
        self.operatorRedBox.addItem("")
        self.operatorRedBox.addItem("")
        self.horizontalLayout.addWidget(self.operatorRedBox)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.alphaRedValue = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.alphaRedValue.setObjectName("alphaRedValue")
        self.horizontalLayout.addWidget(self.alphaRedValue)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 350, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 0, 16, 0)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.greenCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.greenCheckBox.setObjectName("greenCheckBox")
        self.horizontalLayout_2.addWidget(self.greenCheckBox)
        self.operatorBlueBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.operatorBlueBox.setObjectName("operatorBlueBox")
        self.operatorBlueBox.addItem("")
        self.operatorBlueBox.addItem("")
        self.horizontalLayout_2.addWidget(self.operatorBlueBox)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.alphaGreenValue = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.alphaGreenValue.setObjectName("alphaGreenValue")
        self.horizontalLayout_2.addWidget(self.alphaGreenValue)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 350, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(11, 0, 16, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.blueCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.blueCheckBox.setObjectName("blueCheckBox")
        self.horizontalLayout_3.addWidget(self.blueCheckBox)
        self.operatorBlueBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.operatorBlueBox_2.setObjectName("operatorBlueBox_2")
        self.operatorBlueBox_2.addItem("")
        self.operatorBlueBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.operatorBlueBox_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.alphaBlueLineValue = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.alphaBlueLineValue.setObjectName("alphaBlueLineValue")
        self.horizontalLayout_3.addWidget(self.alphaBlueLineValue)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.redCheckBox.setText(_translate("Dialog", "Red   "))
        self.operatorRedBox.setItemText(0, _translate("Dialog", "Add"))
        self.operatorRedBox.setItemText(1, _translate("Dialog", "Multi"))
        self.label.setText(_translate("Dialog", "value:  "))
        self.greenCheckBox.setText(_translate("Dialog", "Green "))
        self.operatorBlueBox.setItemText(0, _translate("Dialog", "Add"))
        self.operatorBlueBox.setItemText(1, _translate("Dialog", "Multiple"))
        self.label_2.setText(_translate("Dialog", "value:  "))
        self.blueCheckBox.setText(_translate("Dialog", "Blue  "))
        self.operatorBlueBox_2.setItemText(0, _translate("Dialog", "Add"))
        self.operatorBlueBox_2.setItemText(1, _translate("Dialog", "Multiple"))
        self.label_3.setText(_translate("Dialog", "value:  "))

