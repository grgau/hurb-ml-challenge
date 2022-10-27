import time

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

    def train(self, X, y, log_to_mlflow: bool = True):
        self.model.fit(X, y)

        if log_to_mlflow:
            self.log_model()

    def log_model(self):
        raise NotImplementedError("log_model method needs to be implemented on the child class!")