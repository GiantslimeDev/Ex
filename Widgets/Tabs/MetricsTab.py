from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from Models.Data import Data

class MetricsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        titleFont = QFont(None, 14)
        labelFont = QFont(None, 14)


        title = QtWidgets.QLabel("Оценка эффективности выбранной модели с помощью метрик")
        title.setFont(titleFont)
        title.setFixedHeight(50)
        #accuracy_score(cls._Y_test, cls._Y_pred), precision_score(cls._Y_test, cls._Y_pred), f1_score(cls._Y_test, cls._Y_pred), recall_score(cls._Y_test, cls._Y_pred), r2_score(cls._Y_test, cls._Y_pred)
        self.accuracy = QtWidgets.QLabel()
        self.accuracy.setFont(labelFont)

        self.precision = QtWidgets.QLabel()
        self.precision.setFont(labelFont)

        self.recall = QtWidgets.QLabel()
        self.recall.setFont(labelFont)

        self.f1 = QtWidgets.QLabel()
        self.f1.setFont(labelFont)

        self.r2 = QtWidgets.QLabel()
        self.r2.setFont(labelFont)

        QtWidgets.QVBoxLayout(self)
        self.layout().addWidget(title)
        self.layout().addWidget(self.accuracy)
        self.layout().addWidget(self.precision)
        self.layout().addWidget(self.recall)
        self.layout().addWidget(self.f1)
        self.layout().addWidget(self.r2)

    def populate(self):
        a, p, f, r, r2 = Data.getMetrics()
        self.accuracy.setText(f"Accuracy: {a}")
        self.precision.setText(f"Precision: {p}")
        self.recall.setText(f"Recall: {r}")
        self.f1.setText(f"F1: {f}")
        self.r2.setText(f"R^2: {r2}")
