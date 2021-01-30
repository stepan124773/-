import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
import sqlite3

con = sqlite3.connect('coffee.sqlite')

cur = con.cursor()

cursor = con.execute('select * from coffee')
names = [e[0] for e in cursor.description]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.table = QTableWidget(self)

        self.gridLayout_2.addWidget(self.table, 0, 0)
        # self.pushButton_2.clicked.connect(self.dobav)
        self.tablee()

    def tablee(self):

        result = con.execute('''SELECT id,name, degree, ground,taste, price, volume FROM coffee''').fetchall()

        result = [(str(result[i][0]), str(result[i][1]), str(result[i][2]), str(result[i][3]),
                   str(result[i][4])) for i
                  in range(len(result))]

        self.table.setColumnCount(5)
        self.table.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(5):
                item = QTableWidgetItem(result[i][j])
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.table.setItem(i, j, item)
        for i in range(len(names)):
            item = QTableWidgetItem()
            item.setText(names[i])
            self.table.setHorizontalHeaderItem(i, item)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()

    ex.show()

    sys.exit(app.exec())
con.close()
