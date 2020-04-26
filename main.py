from PyQt5 import QtWidgets
from maingui import Ui_MainWindow
import sys
from square import MagickSquare

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.square = MagickSquare()

        try:
            self.square.download()
            self.download()
        except Exception:
            self.ui.errorlabel.setText("Загрузка неудалась")

        self.ui.resultButton.clicked.connect(self.checkMagickSquare)
        self.ui.creaeteButton.clicked.connect(self.crete_matrix)

    def download(self):#
        if self.square.N == 2:
            self.square = MagickSquare()
            self.ui.errorlabel.setText("Магического квадрата 2х2 не существует")
            self.ui.tableWidget.clear()
        self.ui.spinBox.setValue(self.square.N)
        self.ui.tableWidget.setRowCount(self.square.N)
        self.ui.tableWidget.setColumnCount(self.square.N)
        for i in range(0, self.square.N): 
            for j in range(0, self.square.N):
                tableSpinBox = QtWidgets.QSpinBox()
                tableSpinBox.setMinimum(0) 
                tableSpinBox.setMaximum(self.square.N ** 2)
                tableSpinBox.setValue(self.square.square[i][j]) 
                self.ui.tableWidget.setCellWidget(i, j, tableSpinBox)

    def crete_matrix(self):
        N = self.ui.spinBox.value()
        self.square = MagickSquare(N)
        self.ui.errorlabel.clear()
        self.ui.result.clear()
        self.download()

    def closeEvent(self, event):
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()
        self.square.save()
        event.accept()

    def checkMagickSquare(self):
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()
        if self.square.ismagick(): 
            self.ui.result.setText("Это магический квадрат!")
        else:
            self.ui.result.setText("Не магический квадрат")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
