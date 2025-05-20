from PyQt5 import QtWidgets

class ColumnsListWidget(QtWidgets.QWidget):
    def __init__(self, title: str, selection: bool = True, single_selection: bool = False):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self._elements = list()
        self._single_selection = single_selection
        self._selection = selection
        self.vboxlayout = QtWidgets.QVBoxLayout()

        self.groupbox = QtWidgets.QGroupBox(title)
        layout.addWidget(self.groupbox, 0, 0)

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.groupbox.setLayout(self.vboxlayout)

    def populate(self, data) -> None:
        columnNames = data

        if not self._selection:
            for i in columnNames:
                element = QtWidgets.QLabel(str(i))
                element.setFixedHeight(50)
                self.vboxlayout.addWidget(element)
                self._elements.append(element)
            return

        for i in columnNames:
            if not self._single_selection:
                element = QtWidgets.QCheckBox(str(i))
            else:
                element = QtWidgets.QRadioButton(str(i))
            element.setFixedHeight(50)
            self.vboxlayout.addWidget(element)
            self._elements.append(element)

    def getSelections(self) -> list:
        result = list()
        if self._single_selection:
            for i in self._elements:
                if i.isChecked():
                    return i.text()

        for i in self._elements:
            if i.isChecked():
                result.append(i.text())

        return result
