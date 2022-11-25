# パッケージの読み込み
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from machine_learning.preprocessing.split_data import DataSplit

# dependency
# - pandas
# - sklearn.preprocessing.<xxxx> (ex: StandardScaler)

class Transformer():
    def __init__(self, train, test):
        self.train = train
        self.test = test
        self.standard_scaler = StandardScaler()

    def logarithmic_transformation(self, columns, log_type=1):
        assert log_type in [1, 2, 3], '"log_type" must be 1 or 2 or 3'
        func = lambda x: np.log(x)
        if log_type == 2: func = lambda x: np.log1p(x)
        if log_type == 3: func = lambda x: np.sign(x) * np.log(np.abs(x))
        self.train[columns], self.test[columns] = self.train[columns].apply(func), self.test[columns].apply(func)
        return self.train, self.test

    def standardization_fit(self, columns):
        self.standard_scaler.fit(self.train[columns])

    def standardization_transform(self, columns):
        self.train[columns], self.test[columns] = self.standard_scaler.transform(self.train[columns]), self.standard_scaler.transform(self.test[columns])
        return self.train, self.test

    def standardization_fit_transform(self, columns):
        self.standard_scaler.fit(self.train[columns])
        self.train[columns], self.test[columns] = self.standard_scaler.transform(self.train[columns]), self.standard_scaler.transform(self.test[columns])
        return self.train, self.test

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
ds = DataSplit(df)
ds.set_propose_column("num_rides")
train_x, test_x, train_y, train_y = ds.hold_out(seed=0, sort_by_index=True)
ts = Transformer(train_x, test_x)
train_x, test_x = ts.logarithmic_transformation(columns=["Max_Temp", "Min_Temp"], log_type=2)
train_x, test_x = ts.standardization_fit_transform(columns=["Max_Temp", "Min_Temp"])
train_x