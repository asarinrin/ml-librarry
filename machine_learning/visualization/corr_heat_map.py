import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 相関行列とヒートマップ
def corr_matrix(DF: pd.DataFrame, figsize=(20,15), standardization=False):
    df = DF.copy()
    if standardization:
        for column in df.columns:
            if df[column].dtype == 'int64' or df[column].dtype == 'float64':
                df[column] = (df[column] - df[column].mean()) / df[column].std()  
    corr = df.corr()
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, annot=True, fmt='.2g', ax=ax, linecolor="w", linewidths=1, vmin=-1, vmax=1, center=0)
    plt.show()
    return

df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
corr_matrix(df, figsize=(20,15), standardization=True)