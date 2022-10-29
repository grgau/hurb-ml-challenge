import bentoml
import numpy as np
import pandas as pd
from bentoml.io import JSON
from .prepare_data import Preprocess

hotel_reservation_clf_runner = bentoml.catboost.get("hotel_reservation_clf:latest").to_runner()

svc = bentoml.Service("hotel_reservation_classifier", runners=[hotel_reservation_clf_runner])

@svc.api(input=JSON(), output=JSON())
def classify(input_series: np.ndarray) -> np.ndarray:
    try:
        X, _ = Preprocess.preprocess_data(pd.json_normalize(input_series))
        result = hotel_reservation_clf_runner.predict.run(X)

        print("Result", X, result)
        if result[0] == 1:
            return { "will_cancel": True }
        else:
            return{ "will_cancel": False }
    except Exception as e:
        return { "error": str(e) }