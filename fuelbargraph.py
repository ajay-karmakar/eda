import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile_data.csv')
print(df.head())

columns_to_plot = ['make', 'fuel-type']

def gas():
    df_gas = df[df['fuel-type'] == 'gas']
    df_gas[columns_to_plot[0]].value_counts().plot(kind='bar', color='blue')

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Graph of Make for Gasoline Cars')
    return(plt.show())


def diesel():
    df_diesel = df[df['fuel-type'] == 'diesel']
    df_diesel[columns_to_plot[0]].value_counts().plot(kind='bar', color='green')

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Graph of Make for Diesel Cars')
    return(plt.show())

gas()
diesel()
