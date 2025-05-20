from PyQt5 import QtWidgets
from Widgets.Canvas import Canvas

class GraphsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QVBoxLayout(self)

        self.Graph = Canvas()

        self.layout().addWidget(self.Graph)
