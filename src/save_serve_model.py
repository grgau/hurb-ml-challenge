import bentoml

from sklearn import svm
from sklearn import datasets

def save_serve_model():
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    clf = svm.SVC(gamma='scale')
    clf.fit(X, y)

    saved_model = bentoml.sklearn.save_model("iris_clf", clf)

    print(f"Model saved: {saved_model}")

if __name__ == "__main__":
    train()