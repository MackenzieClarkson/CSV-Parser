import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
import bigdataEx1
# This is our window from QtCreator
import csv_main_v1
import pandas as pd

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
class MainWindow(QMainWindow, csv_main_v1.Ui_MainWindow, bigdataEx1.Datas1):

    def rowIsolate(self, text):
        global rowSeries
        rowSeries =  (self.rowInfo(data, text))
        rowParsedStr = str(self.rowInfo(data, text))
        self.setText2(rowParsedStr)


    def FindinRow(self, key):
        #print (rowParsed)
        Key_location = self.Query_Point_in_row(rowSeries, key)
        print(Key_location)
        self.setText2(Key_location)

    def Thresholds(self, col, threshlow,threshigh):

       ThreshRet = self.Threshold_Query(data,col,threshlow,threshigh)
       self.setText2(str(ThreshRet))
       print (str(ThreshRet))
    def columnIsolate(self, data, col):
        global columnSeries
        columnSeries = self.columnInfo(data, col)

        self.setText2(str(columnSeries))

    def FindinColumn(self,data,key):
        key = float(key)
        self.setText2(str(self.Query_Point_in_Column(data, key, self.getText3())))

    def plotColumns(self, data, col1, col2):

        self.plot(data, col1, col2)
    def __init__(self):
        pd.set_option('display.height', 1000)
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('max_colwidth', 25)
        pd.set_option('display.precision', 3)
        global data
        data = pd.read_csv('2017.csv', index_col=False, low_memory=False)
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file

        self.pushButton.clicked.connect(lambda: self.rowIsolate(self.getText1()))
        self.pushButton_3.clicked.connect(lambda: self.FindinRow(self.getText4()))
        self.pushButton_2.clicked.connect(lambda: self.columnIsolate(data, self.getText3()))
        self.pushButton_5.clicked.connect(lambda: self.Thresholds(self.getText25(),self.getText7(), self.getText8()))
        self.pushButton_4.clicked.connect(lambda: self.plotColumns(data, self.getText5(), self.getText6()))
        self.pushButton_6.clicked.connect(lambda: self.FindinColumn(data, self.getText9()))

        #text1 = self.getText()
        #print text1
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
if __name__ == "__main__":
        main()