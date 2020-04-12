from PyQt5 import QtWidgets
from maingui import Ui_MainWindow
import sys
from square import MagickSquare

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):#вызывается конструктр супер класса
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()#вызываю то, что сформировано, 
        self.ui.setupUi(self)#собирает
        self.square = MagickSquare()#инициализация магического квадрата

        try:
            self.square.download()#метод 
            self.download()
        except Exception:
            self.ui.errorlabel.setText("Загрузка неудалась")#если сюда попало, то мы выскочила ошибка какая-то и инициализация 1 

        self.ui.resultButton.clicked.connect(self.checkMagickSquare)#кликер, метод, который вызывает обработчик ивента. Если жмакнула на кнопку, то вызвает метод, который прописан в скобках
        self.ui.creaeteButton.clicked.connect(self.crete_matrix)

    def download(self):#
        if self.square.N == 2:
            self.square = MagickSquare()
            self.ui.errorlabel.setText("Магического квадрата 2х2 не существует")
            self.ui.tableWidget.clear()#пространство, куда выводитя таблица. клиер вызывается всегда, чтобы очистить таблицу
        self.ui.spinBox.setValue(self.square.N)#вызываем размерность 
        self.ui.tableWidget.setRowCount(self.square.N)#начинает отрисовыывать таблицу. количество строк
        self.ui.tableWidget.setColumnCount(self.square.N)#количество столбцов
        for i in range(0, self.square.N): #чтобы можно было вводить только инт
            for j in range(0, self.square.N):
                tableSpinBox = QtWidgets.QSpinBox()#создание спинбокса, чтобы были только инты. бежит по каждый ячейке и засовывает туда спинбокс 
                tableSpinBox.setMinimum(0) #чтобы все нулями было 
                tableSpinBox.setMaximum(self.square.N ** 2)#максимум 
                tableSpinBox.setValue(self.square.square[i][j])#присваивает значение, если считал из файла 
                self.ui.tableWidget.setCellWidget(i, j, tableSpinBox)#поместил мой ыиджет, мою таблицу в таблицу

    def crete_matrix(self):
        N = self.ui.spinBox.value()
        self.square = MagickSquare(N)
        self.ui.errorlabel.clear()#очищает все поля
        self.ui.result.clear()
        self.download()#пересобирает матрицу

    def closeEvent(self, event):#переопределяется от класса родителя. метод крестик. 
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()#перед закрытием перезаписывается скваер
        self.square.save()
        event.accept()#выполнить евент, чтобы окно закрылось

    def checkMagickSquare(self):
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()#пробегается по всей таблице и записывает все элементы в скваер
        if self.square.ismagick(): #либо тру либо фолс
            self.ui.result.setText("Это магический квадрат!")
        else:
            self.ui.result.setText("Не магический квадрат")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
