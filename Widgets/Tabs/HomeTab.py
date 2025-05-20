from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont

from Models.Data import Data

class HomeTab(QtWidgets.QWidget):
    def __init__(self, OnDataLoad):
        super().__init__()
        QtWidgets.QVBoxLayout(self)
        self._Delegate = OnDataLoad
        font = QFont(None, 14)

        infoText = QtWidgets.QTextBrowser()
        infoText.setReadOnly(True)
        infoText.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        infoText.setFont(font)
        infoText.setFontPointSize(14)

        infoText.setSource(QUrl("resources/HomeText.md"))

        self.layout().addWidget(infoText)

        self.SelectDataButton = QtWidgets.QPushButton("Выбор файла", self)
        self.SelectDataButton.setFixedHeight(50)
        self.SelectDataButton.clicked.connect(self.OpenFileDialog)
        self.SelectDataButton.setGeometry(100, 100, 400, 400)

        self.layout().addWidget(self.SelectDataButton)


    #@pyqtSlot()
    def OpenFileDialog(self):
        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setWindowTitle("Выберите файл")
        fileDialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        fileDialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)

        if fileDialog.exec():
            selection = fileDialog.selectedFiles()
            Data.initDataFrame(selection[0])

            self._Delegate()
