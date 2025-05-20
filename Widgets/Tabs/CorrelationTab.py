from PyQt5 import QtWidgets
from Widgets.Canvas import Canvas
from Models.Data import Data
from PyQt5.QtGui import QFont
from seaborn import heatmap

from matplotlib.figure import Figure

class CorrelationTab(QtWidgets.QWidget):
    def __init__(self, onDataConfirm):
        super().__init__()
        QtWidgets.QVBoxLayout(self)

        self._delegate = onDataConfirm
        font = QFont(None, 14)

        title = QtWidgets.QLabel("Проверка с применением матрицы корреляций")
        title.setFixedHeight(50)
        title.setFont(font)
        self.confirmButton = QtWidgets.QPushButton("Подтверждение")
        self.confirmButton.setFixedHeight(50)
        self.confirmButton.clicked.connect(self.onConfirmButtonClick)

        self.CorrelationMatrix = Canvas()

        self.layout().addWidget(title)
        self.layout().addWidget(self.CorrelationMatrix)
        self.layout().addWidget(self.confirmButton)

    def drawCorrelationMatrix(self):
        fig = Figure()
        ax = fig.subplots()

        cm = Data.getCorrelationMatrix()
        heatmap(
            ax=ax,
            data=cm,
            cmap="coolwarm",
            annot=True,
            vmin=-1,
            vmax=1,
            center=0,
            linewidths=1,
            linecolor='black',
            square=True
        )

        ax.set_title("Матрица Корреляций")
        self.CorrelationMatrix.setFigure(fig)

    def onConfirmButtonClick(self):
        self._delegate()
