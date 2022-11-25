import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from machine_learning.preprocessing.typechecker import TypeChecker
from machine_learning.preprocessing.null_operation import PreprocessForNull

# dependency
# - sklearn.model_selection.train_test_split
# -pandas

class DataSplit():
    def __init__(self, df):
        self.df = df
        self.X = None
        self.y = None

    def __preprocess_for_null(self):
        type_checker = TypeChecker()
        pfn = PreprocessForNull()
        for column in list(self.df.columns):
            dtype = self.train_x[column].dtype
            if type_checker.is_numeric(dtype): pfn.fill_na_by_mean(column)
            if type_checker.is_boolean(dtype): pfn.drop_na_index([column])
            if type_checker.is_string(dtype): pfn.drop_na_index(column)

    def __sort_by_index(self, train_x, test_x, train_y, test_y):
        train_x = train_x.sort_index()
        test_x = test_x.sort_index()
        train_y = train_y.sort_index()
        test_y = test_y.sort_index()
        return train_x, test_x, train_y, test_y

    def set_propose_column(self, column):
        self.df.dropna(subset=[column])
        self.X = self.df.drop(columns=column)
        self.y = self.df[column]

    def hold_out(self, seed=0, preprocess_for_null=False, sort_by_index=False):
        if preprocess_for_null == True: self.__preprocess_for_null()
        train_x, test_x, train_y, test_y = train_test_split(self.X, self.y, train_size = 0.8 ,test_size = 0.2, shuffle = True, random_state = seed)
        if sort_by_index == True:
            train_x, test_x, train_y, test_y = self.__sort_by_index(train_x, test_x, train_y, test_y)
        return train_x, test_x, train_y, test_y

    def k_fold_cross_validation(self, n_splits, shuffle=True, seed=0, preprocess_for_null=False, sort_by_index=False):
        if preprocess_for_null == True: self.__preprocess_for_null()
        res = []
        kf = KFold(n_splits=n_splits, shuffle=shuffle, random_state=seed)
        for train, test in kf.split(self.X, self.y):
            train_x = self.X.iloc[train]
            train_y = self.y.iloc[train]
            test_x = self.X.iloc[test]
            test_y = self.y.iloc[test]
            if sort_by_index == True:
                train_x, test_x, train_y, test_y = self.__sort_by_index(train_x, test_x, train_y, test_y)
            res.append((train_x, train_y, test_x, test_y))
        return res

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
y = df["num_rides"]
X = df.drop(columns="num_rides")
ds = DataSplit(df)
ds.set_propose_column("num_rides")
# dat = ds.k_fold_cross_validation(n_splits=4)
train_x, test_x, train_y, test_y = ds.hold_out(seed=0, sort_by_index=True)
train_x.sort_values("date")