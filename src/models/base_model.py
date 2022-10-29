import time
from sklearn.metrics import accuracy_score, recall_score, precision_score

class BaseModel:
    def __init__(self, artifact: str = 'base-model'):
        self.model = None
        self.artifact = artifact
        self.run_name = f'{self.artifact}_{str(int(time.time() * 1000))}'

        self.train_accuracy = None
        self.test_accuracy = None
        self.train_recall = None
        self.test_recall = None
        self.train_precision = None
        self.test_precision = None

    def train_test(self, X_train, y_train, X_test, y_test, log_to_mlflow: bool = True):
        self.model.fit(X_train, y_train)

        y_train_pred = self.model.predict(X_train)

        self.train_accuracy = accuracy_score(y_train, y_train_pred)
        self.train_recall = recall_score(y_train, y_train_pred)
        self.train_precision = precision_score(y_train, y_train_pred)

        y_test_pred = self.model.predict(X_test)

        self.test_accuracy = accuracy_score(y_test, y_test_pred)
        self.test_recall = recall_score(y_test, y_test_pred)
        self.test_precision = precision_score(y_test, y_test_pred)

        if log_to_mlflow:
            self.log_model()

    def log_model(self):
        raise NotImplementedError("log_model method needs to be implemented on the child class!")