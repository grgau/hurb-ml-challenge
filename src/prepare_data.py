import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocess:
    @staticmethod
    def get_data() -> pd.DataFrame:
        df = pd.read_csv(os.getenv("DATASET_URL", ""))
        return df

    @staticmethod
    def preprocess_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
        # dropping columns that are not useful
        useless_col = ['days_in_waiting_list', 'arrival_date_year', 'arrival_date_year', 'assigned_room_type', 'booking_changes',
                    'reservation_status', 'country', 'days_in_waiting_list']
        df.drop(useless_col, axis = 1, inplace = True)

        # creating numerical and categorical dataframes
        cat_cols = [col for col in df.columns if df[col].dtype == 'O']
        cat_df = df[cat_cols]
        cat_df['reservation_status_date'] = pd.to_datetime(cat_df['reservation_status_date'])
        cat_df['year'] = cat_df['reservation_status_date'].dt.year
        cat_df['month'] = cat_df['reservation_status_date'].dt.month
        cat_df['day'] = cat_df['reservation_status_date'].dt.day
        cat_df.drop(['reservation_status_date','arrival_date_month'] , axis = 1, inplace = True)

        # encoding categorical variables
        cat_df['hotel'] = cat_df['hotel'].map({'Resort Hotel' : 0, 'City Hotel' : 1})
        cat_df['meal'] = cat_df['meal'].map({'BB' : 0, 'FB': 1, 'HB': 2, 'SC': 3, 'Undefined': 4})
        cat_df['market_segment'] = cat_df['market_segment'].map({'Direct': 0, 'Corporate': 1, 'Online TA': 2, 'Offline TA/TO': 3,
                                                                'Complementary': 4, 'Groups': 5, 'Undefined': 6, 'Aviation': 7})
        cat_df['distribution_channel'] = cat_df['distribution_channel'].map({'Direct': 0, 'Corporate': 1, 'TA/TO': 2, 'Undefined': 3,
                                                                            'GDS': 4})
        cat_df['reserved_room_type'] = cat_df['reserved_room_type'].map({'C': 0, 'A': 1, 'D': 2, 'E': 3, 'G': 4, 'F': 5, 'H': 6,
                                                                        'L': 7, 'B': 8})
        cat_df['deposit_type'] = cat_df['deposit_type'].map({'No Deposit': 0, 'Refundable': 1, 'Non Refund': 3})
        cat_df['customer_type'] = cat_df['customer_type'].map({'Transient': 0, 'Contract': 1, 'Transient-Party': 2, 'Group': 3})
        cat_df['year'] = cat_df['year'].map({2015: 0, 2014: 1, 2016: 2, 2017: 3})

        num_df = df.drop(columns = cat_cols, axis = 1)
        num_df.drop('is_canceled', axis = 1, inplace = True, errors='ignore')

        # normalizing numerical variables
        num_df['lead_time'] = np.log(num_df['lead_time'] + 1)
        num_df['arrival_date_week_number'] = np.log(num_df['arrival_date_week_number'] + 1)
        num_df['arrival_date_day_of_month'] = np.log(num_df['arrival_date_day_of_month'] + 1)
        num_df['agent'] = np.log(num_df['agent'] + 1)
        num_df['company'] = np.log(num_df['company'] + 1)
        num_df['adr'] = np.log(num_df['adr'] + 1)
        num_df['adr'] = num_df['adr'].fillna(value = num_df['adr'].mean())

        X = pd.concat([cat_df, num_df], axis = 1)
        y = df['is_canceled'] if 'is_canceled' in df.columns else None

        return X, y

    @staticmethod
    def split_train_test(X: pd.DataFrame, y: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(os.environ.get('TEST_SIZE')))
        return X_train, X_test, y_train, y_test

    @staticmethod
    def perform() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        df = Preprocess.get_data()
        X, y = Preprocess.preprocess_data(df)
        X_train, X_test, y_train, y_test = Preprocess.split_train_test(X, y)

        return X_train, X_test, y_train, y_test