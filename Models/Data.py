import pandas
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, r2_score
from random import randint
import numpy as np

class Data:
    _dataFrame: pandas.DataFrame = pandas.DataFrame()
    _dataX = None
    _dataY = None
    _model = None

    _X_train = None
    _X_test = None
    _Y_train = None
    _Y_test = None

    _X_poly_train = None
    _X_poly_test = None

    _Y_pred = None

    _scaler = None

    model_type = None

    is_empty: bool = True

    poly_feat = None


    @classmethod
    def initDataFrame(cls, filePath: str, sep: str = ',') -> None:
        cls._dataFrame = pandas.read_csv(filePath, sep=sep)
        cls.is_empty = False

    @classmethod
    def getCorrelationMatrix(cls) -> pandas.DataFrame:
        return cls._dataFrame.corr(numeric_only=True)

    @classmethod
    def getData(cls) -> pandas.DataFrame:
        return cls._dataFrame

    @classmethod
    def getColumns(cls):
        return cls._dataFrame.columns

    @classmethod
    def setMLVars(cls, x, y):
        cls._dataX = x
        cls._dataY = y

    @classmethod
    def getMLVars(cls) -> tuple:
        return cls._dataX, cls._dataY

    @classmethod
    def dropNa(cls) -> None:
        cls._dataFrame = cls._dataFrame.dropna(how='any')

    @classmethod
    def dropDuplicates(cls) -> None:
        cls._dataFrame = cls._dataFrame.drop_duplicates()

    @classmethod
    def initModel(cls, model_name: str) -> None:
        if model_name == "KNN":
            cls._KNNModel()
        elif model_name == "Linear":
            cls._LinearModel()
        elif model_name == "Poly3":
            cls._PolyModel(3)
        elif model_name == "Poly5":
            cls._PolyModel(5)
        elif model_name == "Multi":
            cls._MultiModel()
        else:
            print(f"Critical error when initializing model: {model_name}")

    @classmethod
    def _KNNModel(cls):
        cls._model = KNeighborsClassifier(n_neighbors=3)

        X = cls._dataFrame[cls._dataX]
        Y = cls._dataFrame[cls._dataY]

        cls._X_train, cls._X_test, cls._Y_train, cls._Y_test = train_test_split(X, Y, test_size=0.2, random_state=randint(0, 1000))

        cls._scaler = StandardScaler()

        cls._X_train = cls._scaler.fit_transform(cls._X_train)
        cls._X_test = cls._scaler.transform(cls._X_test)

        cls._model.fit(cls._X_train, cls._Y_train)

        cls._Y_pred = cls._model.predict(cls._X_test)

        cls.model_type = "KNN"

    @classmethod
    def _LinearModel(cls):
        cls._model = LinearRegression()

        X = cls._dataFrame[cls._dataX]
        Y = cls._dataFrame[cls._dataY]

        cls._X_train, cls._X_test, cls._Y_train, cls._Y_test = train_test_split(X, Y, test_size=0.2, random_state=randint(0, 1000))

        cls._model.fit(cls._X_train, cls._Y_train)
        cls._Y_pred = cls._model.predict(cls._X_test)

        cls.model_type = "Lin"

    @classmethod
    def _PolyModel(cls, degree: int):
        cls._model = LinearRegression()

        X = cls._dataFrame[cls._dataX]
        Y = cls._dataFrame[cls._dataY]

        cls._X_train, cls._X_test, cls._Y_train, cls._Y_test = train_test_split(X, Y, test_size=0.2, random_state=randint(0, 1000))

        cls.poly_feat = PolynomialFeatures(degree=degree)
        cls._X_poly_train = cls.poly_feat.fit_transform(cls._X_train)
        cls._X_poly_test = cls.poly_feat.transform(cls._X_test)

        cls._model.fit(cls._X_poly_train, cls._Y_train)

        cls._Y_pred = cls._model.predict(cls._X_poly_test)

        if degree == 3:
            cls.model_type = "Poly3"
        elif degree == 5:
            cls.model_type = "Poly5"

    @classmethod
    def _MultiModel(cls):
        cls._model = LinearRegression()

        X = cls._dataFrame[cls._dataX]
        Y = cls._dataFrame[cls._dataY]

        cls._X_train, cls._X_test, cls._Y_train, cls._Y_test = train_test_split(X, Y, test_size=0.2, random_state=randint(0, 1000))

        cls._model.fit(cls._X_train, cls._Y_train)
        cls._Y_pred = cls._model.predict(cls._X_test)

        cls.model_type = "Multi"

    @classmethod
    def makeDataPointKNN(cls, f_name, s_name, f_val, s_val):
        X = cls._dataX
        res = list()
        for el in X:
            if el == f_name:
                res.append(f_val)
            elif el == s_name:
                res.append(s_val)
            else:
                #res.append(0)
                res.append(cls._dataFrame[el].mean())
        return res

    
    @classmethod
    def predict(cls, x):
        if cls.model_type == "KNN":
            x = cls._scaler.transform(x)
            return cls._model.predict(x)
        else:
            return cls._model.predict(x)
        
    @classmethod
    def getModelEquation(cls):
        if cls.model_type == "Lin":
            coef = cls._model.coef_[0]
            return f"X * {coef:.5} + ({cls._model.intercept_:.5})"
        elif cls.model_type == "Poly3":
            coef = cls._model.coef_
            return f"X^3 * {coef[3]:.5} + X^2 * {coef[2]:.5} + X * {coef[1]:.5} + ({cls._model.intercept_:.5})"
        elif cls.model_type == "Poly5":
            coef = cls._model.coef_
            return f"X^5 * {coef[5]:.7} + X^4 * {coef[4]:.7} + X^3 * {coef[3]:.7} + X^2 * {coef[2]:.5} + X * {coef[1]:.5} + ({cls._model.intercept_:.5})"
            

    @classmethod
    def encodeLabels(cls, column):
        encoder = LabelEncoder()
        Y = cls._dataFrame[column]
        return encoder.fit_transform(Y)

    @classmethod
    def getMetrics(cls):
        acc = 0
        prec = 0
        f1 = 0
        rec = 0
        r2 = 0
 
        if cls.model_type == "KNN":
            r2 = "Эту метрику нельзя рассчитать для использованной модели"

            acc = accuracy_score(cls._Y_test, cls._Y_pred)
            prec = precision_score(cls._Y_test, cls._Y_pred, average='weighted')
            f1 = f1_score(cls._Y_test, cls._Y_pred, average='weighted')
            rec = recall_score(cls._Y_test, cls._Y_pred, average='weighted')
        else:
            acc = "Эту метрику нельзя рассчитать для использованной модели"
            prec = "Эту метрику нельзя рассчитать для использованной модели"
            f1 = "Эту метрику нельзя рассчитать для использованной модели"
            rec = "Эту метрику нельзя рассчитать для использованной модели"

            r2 = r2_score(cls._Y_test, cls._Y_pred)
    
        return acc, prec, f1, rec, r2
