import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# dependency
# - pandas
# - sklearn.preprocessing.OneHotEncoder
class OneHotEncoding():
    def __init__(self, train_x, test_x, columns):
        self.train_x = train_x
        self.test_x = test_x
        self.ohe = OneHotEncoder(sparse=False, categories='auto')
        self.columns = columns

    def __fit_transform_and_get_new_df(self, drop):
        new_columns = []
        for i, col in enumerate(self.columns):
            new_columns += [f'{col}_{v}' for v in self.ohe.categories_[i]]
        ndf_train = pd.DataFrame(self.ohe.transform(self.train_x[self.columns]), columns=new_columns, index=self.train_x.index)
        ndf_train = pd.concat([self.train_x, ndf_train], axis=1)
        ndf_test = pd.DataFrame(self.ohe.transform(self.test_x[self.columns]), columns=new_columns, index=self.test_x.index)
        ndf_test = pd.concat([self.test_x, ndf_test], axis=1)
        if drop == True: 
            ndf_train.drop(columns=self.columns, inplace=True)
            ndf_test.drop(columns=self.columns, inplace=True)
        self.train_x = ndf_train
        self.test_x = ndf_test

    def fit(self):
        self.ohe.fit(self.train_x[self.columns])

    def transform(self):
        return self.ohe.transform(self.train_x[self.columns]), self.ohe.transform(self.test_x[self.columns])

    def fit_transform_and_get_new_df(self, drop=True):
        self.ohe.fit(self.train_x[self.columns])
        self.__fit_transform_and_get_new_df(drop)
        return self.train_x, self.test_x

    def transform_and_get_new_df(self, drop=True):
        self.__fit_trainsform_and_get_new_df(drop)
        return self.train_x, self.test_x

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
df["d"] = "s"
df["d"].iloc[0]="a"
df["e"] = "s"
df["f"] = "s"
ds = DataSplit(df)
ds.set_propose_column("num_rides")
train_x, test_x, train_y, train_y = ds.hold_out(seed=0)
ohefd = OneHotEncoding(train_x, test_x, ["d", "e", "f", "holiday"])
train_x, test_x = ohefd.fit_transform_and_get_new_df(drop=False)
train_x.sort_values("date")