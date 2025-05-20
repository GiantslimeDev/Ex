from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas

class Canvas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QVBoxLayout(self)

    def clear(self):
        current = self.layout().takeAt(0)
        del current

    def setFigure(self, fig):
        self.clear()
        self.layout().addWidget(FigureCanvas(fig))