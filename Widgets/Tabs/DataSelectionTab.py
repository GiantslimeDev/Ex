from PyQt5 import QtWidgets
from Widgets.ColumnsListWidget import ColumnsListWidget

from Models.Data import Data

class DataSelectionTab(QtWidgets.QWidget):
    def __init__(self, OnSelection):
        super().__init__()
        outerLayout = QtWidgets.QVBoxLayout()
        innerLayout = QtWidgets.QHBoxLayout()
        self.ConfirmButton = QtWidgets.QPushButton("Далее")
        self.ConfirmButton.clicked.connect(self._getSelection)
        self.ConfirmButton.setFixedHeight(50)

        #QtWidgets.QHBoxLayout(self)
        self._Delegate = OnSelection

        self.xSel = ColumnsListWidget("Выберите независимые переменные", selection=True)
        self.ySel = ColumnsListWidget("Выберите целевую переменную", selection=True, single_selection=True)

        innerLayout.addWidget(self.xSel)
        innerLayout.addWidget(self.ySel)

        outerLayout.addLayout(innerLayout)
        outerLayout.addWidget(self.ConfirmButton)

        self.setLayout(outerLayout)

    def populate(self):
        columns = Data.getColumns().values
        self.xSel.populate(columns)
        self.ySel.populate(columns)

    def _getSelection(self):
        x = self.xSel.getSelections()
        y = self.ySel.getSelections()

        self._Delegate(x, y)
