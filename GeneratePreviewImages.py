from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def makeClassificationImage(rand) -> None:
    X, y_true = make_blobs(n_samples=500, centers=3, cluster_std=0.5, random_state=rand)

    X = X[:, ::-1]

    # Plot init seeds along side sample data
    plt.figure(1)
    colors = ["#4EACC5", "#FF9C34", "#4E9A06"]

    for k, col in enumerate(colors):
        cluster_data = y_true == k
        plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, s=10)

    plt.title("Классификация")
    plt.xticks([])
    plt.yticks([])
    plt.show()

def makePredictionImage(rand) -> None:
    np.random.seed(rand)
    X = np.sort(5 * np.random.rand(80, 1), axis=0)
    Y = np.sin(X) + np.random.normal(0, 0.2, X.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=rand)

    degree = 3
    poly_feat = PolynomialFeatures(degree=degree)
    X_poly_train = poly_feat.fit_transform(X_train)
    X_poly_test = poly_feat.transform(X_test)

    model = LinearRegression()
    model.fit(X_poly_train, Y_train)

    plt.figure(1)

    plt.scatter(X_train, Y_train, color='lightblue')
    plt.scatter(X_test, Y_test, color='red')

    X_grid = np.arange(0, 5, 0.01).reshape(-1, 1)
    Y_grid = model.predict(poly_feat.transform(X_grid))

    plt.plot(X_grid, Y_grid, color='green', label='Линия регрессии')
    plt.title("Регрессия")
    plt.show()

if __name__ == "__main__":
    randomSeed = 1564
    makeClassificationImage(randomSeed)
    makePredictionImage(randomSeed)
