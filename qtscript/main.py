import os
import sys
from PyQt5 import QtWidgets, uic

ROOT = os.path.join(os.path.dirname(__file__))
UI_DIR = os.path.join(ROOT, "ui")

class Main(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.form = uic.loadUi(
            os.path.join(UI_DIR, "one.ui"), self)
        self.resize(300, 200)
        self.setText("TEST")

def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()