from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl

from Models.Data import Data
from Widgets.ColumnsListWidget import ColumnsListWidget

class DataPrepTab(QtWidgets.QWidget):
    def __init__(self, onPreparationFinished):
        super().__init__()
        self._DataYValue = QtWidgets.QLabel()
        self._DataYValue.setFixedHeight(50)

        self._Delegate = onPreparationFinished

        font = QFont(None, 14)
        self._DataYValue.setFont(font)

        self._DataXValues = ColumnsListWidget("Независимые переменные", selection=False, single_selection=False)

        self.duplicatesButton = QtWidgets.QPushButton("Удаление дубликатов")
        self.duplicatesButton.setFixedHeight(50)
        self.duplicatesButton.clicked.connect(self._buttonDuplicatesClicked)

        self.emptyValuesButton = QtWidgets.QPushButton("Удаление пропусков")
        self.emptyValuesButton.setFixedHeight(50)
        self.emptyValuesButton.clicked.connect(self._buttonEmptyValuesClicked)

        self.finishButton = QtWidgets.QPushButton("Готово")
        self.finishButton.clicked.connect(self._buttonNextClicked)
        self.finishButton.setFixedHeight(50)

        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addWidget(self.duplicatesButton)
        buttonsLayout.addWidget(self.emptyValuesButton)
        buttonsLayout.addWidget(self.finishButton)

        infoText = QtWidgets.QTextBrowser()
        infoText.setReadOnly(True)
        infoText.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        infoText.setFont(font)
        infoText.setFontPointSize(14)

        infoText.setSource(QUrl("resources/DataPreparation.md"))

        pageLayout = QtWidgets.QVBoxLayout()
        centerLayout = QtWidgets.QHBoxLayout()
        leftLayout = QtWidgets.QVBoxLayout()
        rightLayout = QtWidgets.QVBoxLayout()

        rightLayout.addWidget(infoText, 1)
        leftLayout.addWidget(self._DataXValues, 0)

        centerLayout.addLayout(leftLayout)
        centerLayout.addLayout(rightLayout)

        pageLayout.addWidget(self._DataYValue)
        pageLayout.addLayout(centerLayout)
        pageLayout.addLayout(buttonsLayout)

        self.setLayout(pageLayout)

    def populate(self):
        x, y = Data.getMLVars()
        self._DataYValue.setText(f"Целевая переменная: {y}")
        self._DataXValues.populate(x)

    def _buttonNextClicked(self):
        self._Delegate()
        self.finishButton.setEnabled(False)
        self.duplicatesButton.setEnabled(False)
        self.emptyValuesButton.setEnabled(False)

    def _buttonDuplicatesClicked(self):
        Data.dropDuplicates()
        self.duplicatesButton.setEnabled(False)

    def _buttonEmptyValuesClicked(self):
        Data.dropNa()
        self.emptyValuesButton.setEnabled(False)
