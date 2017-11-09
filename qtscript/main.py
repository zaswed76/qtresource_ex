import os
import sys
from PyQt5 import QtWidgets, uic, QtGui
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

        self.lb = QtWidgets.QLabel(self)
        self.lb.setPixmap(QtGui.QPixmap(':two.png'))
        self.resize(300, 200)


def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()