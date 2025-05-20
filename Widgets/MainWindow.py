from PyQt5 import QtWidgets

from Widgets.Tabs.HomeTab import HomeTab
from Widgets.Tabs.PreviewTab import PreviewTab
from Widgets.Tabs.DataPrepTab import DataPrepTab
from Widgets.Tabs.CorrelationTab import CorrelationTab
from Widgets.Tabs.GraphsTab import GraphsTab
from Widgets.Tabs.DataSelectionTab import DataSelectionTab
from Widgets.Tabs.ModelSelectionTab import ModelSelectionTab
from Widgets.Tabs.MetricsTab import MetricsTab

from Models.Data import Data

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = QtWidgets.QTabWidget()

        self.Home = HomeTab(self.onDataLoad)
        self.Preview = PreviewTab()
        self.Prep = DataPrepTab(self.onDataPreparation)
        self.Corr = CorrelationTab(self.onCorrConfirm)
        self.Select = DataSelectionTab(self.onColumnSelection)
        self.Model = ModelSelectionTab(self.onModelSelection)
        self.Graphs = GraphsTab()
        self.Metrics = MetricsTab()

        self.tabsConfig()

        self.style()

        self.setWindowTitle("Data App")
        self.setCentralWidget(self.tabs)

    def tabsConfig(self):
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setMovable(False)

        self.tabs.addTab(self.Home, "Загрузка")
        self.tabs.setTabEnabled(0, True)

        self.tabs.addTab(self.Preview, "Предпросмотр")
        self.tabs.setTabEnabled(1, False)

        self.tabs.addTab(self.Corr, "Корреляция")
        self.tabs.setTabEnabled(2, False)

        self.tabs.addTab(self.Select, "Выбор данных")
        self.tabs.setTabEnabled(3, False)

        self.tabs.addTab(self.Prep, "Подготовка данных")
        self.tabs.setTabEnabled(4, False)

        self.tabs.addTab(self.Model, "Выбор Модели")
        self.tabs.setTabEnabled(5, False)

        self.tabs.addTab(self.Metrics, "Метрики")
        self.tabs.setTabEnabled(6, False)

        self.tabs.addTab(self.Graphs, "Graphs")
        self.tabs.setTabEnabled(7, False)

    def onDataLoad(self):
        self.Preview.initialize()
        self.Corr.drawCorrelationMatrix()

        if not self.tabs.isTabEnabled(1):
            self.tabs.setTabEnabled(1, True)
            self.tabs.setTabEnabled(2, True)


    def onCorrConfirm(self):
        self.Select.populate()
        self.tabs.setTabEnabled(3, True)
        self.Home.SelectDataButton.setEnabled(False)
        self.Corr.confirmButton.setEnabled(False)

    def onColumnSelection(self, x, y):
        if y in x:
            self.tabs.setTabEnabled(4, False)
            self._dialogWarnSelection(y)
            return
        Data.setMLVars(x, y)
        self.Prep.populate()
        self.tabs.setTabEnabled(4, True)
        self.Select.ConfirmButton.setEnabled(False)

    def _dialogWarnSelection(self, value):
        dialog = QtWidgets.QMessageBox.critical(
            self,
            "Ошибка",
            f"Целеввая переменная не может быть одновременно и независимой: {value}",
            buttons=QtWidgets.QMessageBox.Ok,
            defaultButton=QtWidgets.QMessageBox.Ok,
        )

        if dialog == QtWidgets.QMessageBox.Ok:
            return

    def onDataPreparation(self):
        self.Model.populate()
        self.tabs.setTabEnabled(5, True)

    def onModelSelection(self):
        self.tabs.setTabEnabled(6, True)
        self.Metrics.populate()

    def style(self):
        self.setStyleSheet(
            """QPushButton {
                color: black;
                background-color: white;
                font-family: "Times New Roman"
                font-style: bold;
                font-size: 12px;
                margin: 2px;
            }
            """
        )
