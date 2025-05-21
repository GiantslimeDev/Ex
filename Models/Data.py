import pandas
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, r2_score
from random import randint

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

        poly_feat = PolynomialFeatures(degree=degree)
        cls._X_poly_train = poly_feat.fit_transform(cls._X_train)
        cls._X_poly_test = poly_feat.transform(cls._X_test)

        cls._model.fit(cls._X_poly_train, cls._Y_train)

        cls._Y_pred = cls._model.predict(cls._X_poly_test)

        cls.model_type = "Poly"

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
    def getMetrics(cls):
        acc = 0
        prec = 0
        f1 = 0
        rec = 0
        r2 = 0
 
        if cls.model_type == "KNN":
            r2 = "Эту метрику нельзя рассчитать для использованной модели"

            acc = accuracy_score(cls._Y_test, cls._Y_pred)
            prec = precision_score(cls._Y_test, cls._Y_pred)
            f1 = f1_score(cls._Y_test, cls._Y_pred)
            rec = recall_score(cls._Y_test, cls._Y_pred)
        else:
            acc = "Эту метрику нельзя рассчитать для использованной модели"
            prec = "Эту метрику нельзя рассчитать для использованной модели"
            f1 = "Эту метрику нельзя рассчитать для использованной модели"
            rec = "Эту метрику нельзя рассчитать для использованной модели"

            r2 = r2_score(cls._Y_test, cls._Y_pred)
    
        return acc, prec, f1, rec, r2
