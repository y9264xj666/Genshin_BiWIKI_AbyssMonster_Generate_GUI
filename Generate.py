from GenerateUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

class mainWindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(mainWindowUI, self).__init__()
        # self.resize(800,600)
        # self.setFixedSize(self.width(),self.height())
    
    def setupUi(self, MainWindow):
        
        return super().setupUi(MainWindow)

    def show(self) -> None:
        return super().show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    ui = mainWindowUI()
    ui.setupUi(ui)
    ui.show()

    sys.exit(app.exec_())
    