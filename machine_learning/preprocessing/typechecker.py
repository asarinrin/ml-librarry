# パッケージの読み込み
import pandas as pd

class TypeChecker():
    def __init__(self):
        self.numeric_columns = ["int8","int16","int32","int64","uint8","uint16","uint32","uint64","float8","float16","float32","float64", "int", "uint", "float"]
        self.boolean_columns = ["bool"]
        self.string_columns = ["object", "str"]
        self.date_columns = ["datetime64[ns]"]
    def is_numeric(self, column):
        return column in self.numeric_columns
    def is_boolean(self, column):
        return column in self.boolean_columns
    def is_string(self, column):
        return column in self.date_columns

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
df["a"] = "a"

tc = TypeChecker()
tc.is_string(df["a"].dtype)
tc.is_boolean(df["holiday"].dtype)