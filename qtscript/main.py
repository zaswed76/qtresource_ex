import os
import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from  qtscript import images_rc

ROOT = os.path.join(os.path.dirname(__file__))
UI_DIR = os.path.join(ROOT, "ui")

class Main(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        # self.box = QtWidgets.QHBoxLayout(self)
        # self.form = uic.loadUi(
        #     os.path.join(UI_DIR, "one.ui"), self)
        # self.box.addWidget(self.form)

        self.lb = QtWidgets.QPushButton(self)
        self.lb.move(100, 100)
        # self.lb.setIcon(QtGui.QIcon(':two.png'))

        self.lb.setIconSize(QtCore.QSize(50, 50))
        self.resize(300, 200)


def main():

    app = QtWidgets.QApplication(sys.argv)

    css_file = os.path.join(ROOT, "css/tool.css")
    app.setStyleSheet(open(css_file, "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()