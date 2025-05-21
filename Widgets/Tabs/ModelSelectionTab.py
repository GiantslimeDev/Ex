from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont

from Models.Data import Data

class ModelSelectionTab(QtWidgets.QWidget):
    def __init__(self, onModelSelected):
        super().__init__()
        font = QFont(None, 14)

        self._Delegate = onModelSelected
        self.PredictionModelSelection = QtWidgets.QComboBox()
        self.PredictionModelSelection.setVisible(False)
        self.Prediction = QtWidgets.QRadioButton("Регрессионная Модель")

        self.Classification = QtWidgets.QRadioButton("Модель Классификации")
        self.ClassificationModelSelection = QtWidgets.QComboBox()

        title = QtWidgets.QLabel("Выбор модели")
        title.setFont(font)
        title.setFixedHeight(50)
        self.nextButton = QtWidgets.QPushButton("Моделирование")
        self.nextButton.setFixedHeight(50)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.style()

        vert = QtWidgets.QVBoxLayout()
        center = QtWidgets.QHBoxLayout()

        left = QtWidgets.QVBoxLayout()
        self.centerRight = QtWidgets.QVBoxLayout()

        leftLabel = QtWidgets.QLabel()
        leftImage = QPixmap("resources/Classification.png")
        leftLabel.setPixmap(leftImage)
        left.addWidget(leftLabel)
        left.addWidget(self.Classification)

        rightLabel = QtWidgets.QLabel()
        rightImage = QPixmap("resources/Prediction.png")
        rightLabel.setPixmap(rightImage)
        self.centerRight.addWidget(rightLabel)
        self.centerRight.addWidget(self.Prediction)

        center.addLayout(left)
        center.addLayout(self.centerRight)

        vert.addWidget(title)
        vert.addLayout(center)

        self.centerRight.addWidget(self.PredictionModelSelection)
        left.addWidget(self.ClassificationModelSelection)

        vert.addWidget(self.nextButton)

        self.setLayout(vert)

    def populate(self):
        x, y = Data.getMLVars()
        self.PredictionModelSelection.clear()

        self.ClassificationModelSelection.clear()
        self.ClassificationModelSelection.addItem("К - Ближайших соседей")

        # Только одна независимая переменная
        if len(x) == 1:
            self.PredictionModelSelection.addItem("Одиночная линейная регрессия")
            self.PredictionModelSelection.addItem("Одиночная полиномиальная регрессия степени: 3")
            self.PredictionModelSelection.addItem("Одиночная полиномиальная регрессия степени: 5")
            self.PredictionModelSelection.setVisible(True)

            self.Classification.setEnabled(False)
            self.ClassificationModelSelection.setEnabled(False)
        else:
            self.PredictionModelSelection.addItem("Линейная множественная регрессия")
            self.PredictionModelSelection.setVisible(True)

    def onNextButtonClick(self):
        if self.Classification.isChecked():
            text = self.ClassificationModelSelection.currentText()
            if text == "К - Ближайших соседей":
                Data.initModel("KNN")
                self._Delegate()

        elif self.Prediction.isChecked():
            text = self.PredictionModelSelection.currentText()
            if text == "Одиночная линейная регрессия":
                Data.initModel("Linear")
                self._Delegate()

            elif text == "Одиночная полиномиальная регрессия степени: 3":
                Data.initModel("Poly3")
                self._Delegate()

            elif text == "Одиночная полиномиальная регрессия степени: 5":
                Data.initModel("Poly5")
                self._Delegate()
            elif text == "Линейная множественная регрессия":
                Data.initModel("Mult")
                self._Delegate()
        else:
            return
