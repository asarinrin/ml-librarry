import pandas as pd
import matplotlib.pyplot as plt

def df_visualization(DF, figsize=(20,15), subplot=True, standardization=False):
    df = DF.copy()
    columns_num = len(df.columns)

    if standardization:
        for column in df.columns:
            df[column] = (df[column] - df[column].mean()) / df[column].std()  
    if subplot:
        fig, axes = plt.subplots(columns_num, 1, figsize=figsize)
        for num, ax in enumerate(axes):
            ax.plot(df.iloc[:,num])
    else:
        fig = plt.figure()
        plt.plot(df)

# sample
df = pd.read_csv('https://raw.githubusercontent.com/blue-eagle/estyle_data/master/day1_yc_data.csv',parse_dates=['date'], index_col=0).sort_index()
df_visualization(df)