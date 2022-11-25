# パッケージの読み込み
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from ml_template.machine_learning.preprocessing.onehotencoding import OneHotEncoding
from ml_template.machine_learning.preprocessing.typechecker import TypeChecker
from ml_template.machine_learning.preprocessing.split_data import DataSplit

# dependency
# - pandas
# - OneHotEncoding <- 自作
# - TypeChecker <- 自作
# - sklearn.decomposition.PCA
# - sklearn.preprocessing.SandardScaler
# - matplotlib.pyplot

class PrincipalComponentAnalysis():
    def __init__(self, train_x, test_x, column_number):
        self.train_x = train_x
        self.test_x = test_x
        self.column_number = column_number
        self.pca = PCA(n_components=column_number)

    def __one_hot_encoding(self):
        type_checker = TypeChecker()
        category_columns = []
        for column in list(self.train_x.columns):
            dtype = self.train_x[column].dtype
            if type_checker.is_boolean(dtype): category_columns.append(column)
            if type_checker.is_string(dtype): category_columns.append(column)
        ohe = OneHotEncoding(self.train_x, self.test_x, category_columns)
        self.train_x, self.test_x = ohe.fit_transform_and_get_new_df()

    def fit(self, one_hot_encoding=False):
        if one_hot_encoding == True: self.__one_hot_encoding()
        self.pca.fit(self.train_x)

    def transform(self):
        self.train_x, self.test_x = self.pca.transform(self.train_x), self.pca.transform(self.test_x)
        return self.train_x, self.test_x

    def fit_transform(self, one_hot_encoding=False):
        if one_hot_encoding == True: self.__one_hot_encoding()
        self.pca.fit(self.train_x)
        self.train_x, self.test_x = self.pca.transform(self.train_x), self.pca.transform(self.test_x)
        return self.train_x, self.test_x

    # fitしている必要がある
    def show_bar(self):
        plt.bar([n for n in range(1, len(self.pca.explained_variance_ratio_)+1)], self.pca.explained_variance_ratio_)

    def two_dimentional_plot(self):
        plt.figure(figsize=(10,10))
        train_x_pca, test_x_pca = self.transform()
        plt.scatter(train_x_pca[:,0], train_x_pca[:, 1])
        plt.gca().set_aspect('equal')
        plt.xlabel('First principal component')
        plt.ylabel('Second principal component')

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
ds = DataSplit(df)
ds.set_propose_column("num_rides")
train_x, test_x, train_y, train_y = ds.hold_out(seed=0)
pca = PrincipalComponentAnalysis(train_x, test_x, 4)
pca.fit(one_hot_encoding=True)
pca.show_bar()
pca.two_dimentional_plot()  