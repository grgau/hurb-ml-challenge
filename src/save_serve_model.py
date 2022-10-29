import bentoml
from prepare_data import Preprocess
from models.catboost_clf import CatBoostClf

def save_serve_model() -> None:
    X_train, X_test, y_train, y_test = Preprocess.perform()

    clf = CatBoostClf()
    clf.train_test(X_train, y_train, X_test, y_test)

    saved_model = bentoml.catboost.save_model("hotel_reservation_clf", clf.model)

    print(f"Model saved: {saved_model}")

if __name__ == "__main__":
    save_serve_model()