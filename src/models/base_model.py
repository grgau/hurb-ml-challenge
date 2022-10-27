class BaseModel:
    def __init__(self):
        self.accuracy = None

    def train(self, log_to_mlflow: bool = True):
        with mlflow.start_run():
            pass