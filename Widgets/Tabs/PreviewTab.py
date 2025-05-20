from PyQt5 import QtWidgets
from Models.Data import Data
from Models.TableModel import TableModel

class PreviewTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QVBoxLayout(self)


        self.table = QtWidgets.QTableView()
        #self.model = TableModel(Data.getData())
        #self.table.setModel(self.model)

        self.layout().addWidget(self.table)

    def initialize(self):
        self.model = TableModel(Data.getData())
        self.table.setModel(self.model)
