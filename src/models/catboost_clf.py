import os
import mlflow

from .base_model import BaseModel
from catboost import CatBoostClassifier

class CatBoostClf(BaseModel):
    def __init__(self, artifact: str = 'catboost', iterations: int = 100):
        super(CatBoostClf, self).__init__()
        self.model = CatBoostClassifier(iterations)
        self.artifact = artifact

    def log_model(self) -> None:
        mlflow.set_tracking_uri(os.getenv("MLFLOW_URL", ""))

        with mlflow.start_run(run_name=self.run_name) as run:
            mlflow.log_metric('train_accuracy', self.train_accuracy)
            mlflow.log_metric('test_accuracy', self.test_accuracy)
            mlflow.log_metric('train_recall', self.train_recall)
            mlflow.log_metric('test_recall', self.test_recall)
            mlflow.log_metric('train_precision', self.train_precision)
            mlflow.log_metric('test_precision', self.test_precision)

            mlflow.log_param('test_size', self.test_size)
            mlflow.log_params(self.model.get_all_params()) # Log all model's params
            mlflow.catboost.log_model(self.model, artifact_path=self.artifact)