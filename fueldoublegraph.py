import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile_data.csv')
print(df.head())

columns_to_plot = ['make', 'fuel-type']

def dbarg():
    df[columns_to_plot].value_counts().unstack().plot(kind='bar', stacked=True)

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Graph of Make vs. Fuel Type')
    plt.legend(title='Fuel Type')
    return(plt.show())

dbarg()

