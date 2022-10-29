import sys
sys.path.append("..")

import os
import pandas as pd

from src.prepare_data import Preprocess
from pandas.util.testing import assert_frame_equal

class TestPreprocess:
    df = Preprocess.get_data()
    saved_features = pd.read_csv('tests/data/features.csv')
    saved_target = pd.read_csv('tests/data/target.csv')

    def test_get_data(self):
        assert self.df.empty == False

    def test_preprocess_data(self):

        X, y = Preprocess.preprocess_data(self.df)
        assert_frame_equal(X, self.saved_features, check_dtype=False)
        assert_frame_equal(y.to_frame(), self.saved_target, check_dtype=False)

    def test_split_train_test(self):
        X_train, X_test, y_train, y_test = Preprocess.split_train_test(self.saved_features, self.saved_target)

        assert len(X_train) == len(self.saved_features) * (1.0 - float(os.environ.get('TEST_SIZE'))) 
        assert len(X_test) == len(self.saved_features) * float(os.environ.get('TEST_SIZE'))
        assert len(y_train) == len(self.saved_target) * (1.0 - float(os.environ.get('TEST_SIZE'))) 
        assert len(y_test) == len(self.saved_target) * float(os.environ.get('TEST_SIZE'))
