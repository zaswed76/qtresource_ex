

import sys
from PyQt5 import QtWidgets

class Main(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
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