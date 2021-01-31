import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
import sqlite3

con = sqlite3.connect('coffee.sqlite')

cur = con.cursor()
# https://github.com/stepan124773/-.git 8e985f5
cursor = con.execute('select * from coffee')
names = [e[0] for e in cursor.description]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.table = QTableWidget(self)

        self.gridLayout_2.addWidget(self.table, 0, 0)
        self.pushButton.clicked.connect(self.dobav)
        self.tablee()

    def dobav(self):
        ex2.show()
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


class MyWidget2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.dobav)
        self.pushButton_3.clicked.connect(self.uzmen)
        self.ids = [el[0] for el in cur.execute('''SELECT ID from coffee ''').fetchall()]

    def uzmen(self):
        self.id = self.lineEdit.text()
        self.name = self.lineEdit_2.text()
        self.degree = self.lineEdit_3.text()
        self.ground = self.lineEdit_4.text()
        self.taste = self.lineEdit_5.text()
        self.price = self.lineEdit_6.text()
        self.volume = self.lineEdit_7.text()
        cur.execute('''UPDATE coffee
                SET name = ? 
                    WHERE ID = ?''', (self.name, self.id,))
        cur.execute('''UPDATE coffee
                SET degree = ? 
                    WHERE ID = ?''', (self.degree, self.id,))
        cur.execute('''UPDATE coffee
                SET ground = ? 
                    WHERE ID = ?''', (self.ground, self.id,))
        cur.execute('''UPDATE coffee
                SET taste = ? 
                    WHERE ID = ?''', (self.taste, self.id,))
        cur.execute('''UPDATE coffee
                SET price = ? 
                    WHERE ID = ?''', (self.price, self.id,))
        cur.execute('''UPDATE coffee
                SET volume = ? 
                    WHERE ID = ?''', (self.volume, self.id,))
        con.commit()

    def dobav(self):
        self.id = 1
        while self.id in self.ids:
            self.id += 1
        self.name = self.lineEdit_2.text()
        self.degree = self.lineEdit_3.text()
        self.ground = self.lineEdit_4.text()
        self.taste = self.lineEdit_5.text()
        self.price = self.lineEdit_6.text()
        self.volume = self.lineEdit_7.text()
        cur.execute('''INSERT INTO coffee(ID,name,degree,ground, taste, price,volume) VALUES(?,?,?,?,?,?,?)''',
                    (self.id, self.name, self.degree, self.ground, self.taste, self.price, self.volume))

    con.commit()

    def delete(self):
        cur.execute('''DELETE from coffee
        where ID = ?''', (int(self.lineEdit.text()),)).fetchall()
        con.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex2 = MyWidget2()
    ex.show()

    sys.exit(app.exec())
con.close()
