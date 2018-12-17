
#import ImageProcessUI
#import ChannelProcessUI

import sys
from PyQt5 import QtWidgets
#from mainUI import Ui_MainWindow
import mainUI

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #w.resize(400, 200)
    #w.setWindowTitle("hello PyQt5")
    MainWindow.show()
    exit(app.exec_())
'''
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 
'''
