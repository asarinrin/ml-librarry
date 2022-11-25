import pandas as pd
import numpy as np

class PreprocessForNull():
    def __init__(self, df):
        self.df = df
    def info(self):
        print(self.df.isnull().sum())
    # nanを持つindexを消去
    def drop_na_index(self, columns):
        self.df = self.df.dropna(subset=columns)
    def drop_na_index_all(self):
        self.df = self.df.dropna()
    def drop_na_column_all(self):
        self.df = self.df.dropna(axis=1)
    def fill_na_by_value(self, columns, value=0):
        self.df[columns] = self.df[columns].fillna(value)
    def fill_na_by_mean(self, columns):
        self.df[columns] = self.df[columns].fillna(self.df[columns].mean())
    def fill_na_by_mode(self, columns):
        self.df[columns] = self.df[columns].fillna(self.df[columns].mode().iloc[0])
    def fill_na_by_arbitary_func(self, columns, func):
        self.df[columns] = self.df[columns].fillna(method = func)
    def get_df(self):
        return self.df

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
df["a"] = np.nan
df['a'].iloc[0] = 3
df['a'].iloc[1] = 4
df['a'].iloc[2] = 4
pfn = PreprocessForNull(df)
pfn.fill_na_by_mean(["a"])
df = pfn.get_df()
df.head()