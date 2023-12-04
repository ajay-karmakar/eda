import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\AJAY KARMAKAR\PycharmProjects\PR391\Automobile_data.csv')
print(df.head())

columns_to_plot = ['make', 'engine-location']

def enginefront():
    df_front = df[df['engine-location'] == 'front']
    plt.hist(df_front[columns_to_plot[0]], color='orange', edgecolor='black', bins=20)

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Histogram of Car Makes for Front Engine Cars')
    plt.xticks(rotation=45, ha='right')
    return(plt.show())

def enginerear():
    df_rear = df[df['engine-location'] == 'rear']
    plt.hist(df_rear[columns_to_plot[0]], color='purple', edgecolor='black', bins=20)

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Histogram of Car Makes for Rear Engine Cars')
    plt.xticks(rotation=45, ha='right')
    return(plt.show())

enginefront()
enginerear()
