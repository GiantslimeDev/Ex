import sys
from PyQt5 import QtWidgets
from Widgets.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.resize(1000, 800)
    window.show()

    app.exec_()
