from PyQt5 import QtWidgets
from Widgets.Canvas import Canvas
from Models.Data import Data

import numpy as np

from matplotlib.figure import Figure

class GraphsTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QVBoxLayout(self)

        top_bar = QtWidgets.QHBoxLayout()
        bottom_bar = QtWidgets.QHBoxLayout()

        self.first_var_selection = QtWidgets.QComboBox()
        self.first_var_selection.setFixedHeight(25)
        self.second_var_selection = QtWidgets.QComboBox()
        self.second_var_selection.setFixedHeight(25)

        self.first_var_input = QtWidgets.QLineEdit()
        self.first_var_input.setFixedHeight(25)
        self.second_var_input = QtWidgets.QLineEdit()
        self.second_var_input.setFixedHeight(25)

        draw_button = QtWidgets.QPushButton("Draw")
        draw_button.setFixedHeight(25)
        draw_button.clicked.connect(self.onDrawButtonClicked)

        top_bar.addWidget(self.first_var_selection)
        top_bar.addWidget(self.second_var_selection)
        top_bar.addWidget(draw_button)

        bottom_bar.addWidget(self.first_var_input)
        bottom_bar.addWidget(self.second_var_input)

        self.Graph = Canvas()
        self.layout().addLayout(top_bar)
        self.layout().addWidget(self.Graph)
        self.layout().addLayout(bottom_bar)

    def populate(self):
        self.first_var_selection.clear()
        self.second_var_selection.clear()
        
        x, y = Data.getMLVars()
        m_type = Data.model_type
        if m_type == "KNN":
            for val in x:
                self.first_var_selection.addItem(val)
                self.second_var_selection.addItem(val)
    
    def onDrawButtonClicked(self):
        p_x = None
        p_y = None
        f = self.first_var_selection.currentText()
        s = self.second_var_selection.currentText()

        if self.first_var_input.text() != "":
            try:
                p_x = float(self.first_var_input.text())
                p_y = float(self.second_var_input.text())
            except:
                self.first_var_input.setText("")
                self.second_var_input.setText("")
        if f == s:
            return
        self.__draw(f, s, p_x, p_y)
        

    def __draw(self, graph_x, graph_y, p_x, p_y):
        m_type = Data.model_type
        x, y = Data.getMLVars()
        df = Data.getData()


        fig = Figure()
        ax = fig.add_subplot()

        if m_type == "KNN":
            ax.scatter(df[graph_x], df[graph_y], c=Data.encodeLabels(y))

            if not (p_x == None or p_y == None):
                point = np.array([np.array(Data.makeDataPointKNN(graph_x, graph_y, p_x, p_y))])
                pred = Data.predict(point)
                ax.scatter(p_x, p_y, marker='*', label=f'{y}: {pred[0]}')
                ax.legend()
        
        self.Graph.setFigure(fig)

