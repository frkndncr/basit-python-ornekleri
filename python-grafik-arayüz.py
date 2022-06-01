import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def clicked(self):
    print('Merhaba')

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('Furkan')
    win.setGeometry(200,200,500,500,)
    win.setToolTip('PROGRAM')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soyadınız: ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(100, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(100, 70)

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Kaydet')
    btn_save.move(100,110)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()
