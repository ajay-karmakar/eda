import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile_data.csv')
print(df.head())

# Specify the columns for plotting
columns_to_plot = ['make', 'engine-location']

def frontengine():
    # Filter the DataFrame for 'front' engine location
    df_front = df[df['engine-location'] == 'front']
    df_front[columns_to_plot[0]].value_counts().plot(kind='bar', color='orange')

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Graph of Make for Front Engine Cars')
    return (plt.show())


def rearengine():
    # Filter the DataFrame for 'rear' engine location
    df_rear = df[df['engine-location'] == 'rear']
    df_rear[columns_to_plot[0]].value_counts().plot(kind='bar', color='purple')

    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Bar Graph of Make for Rear Engine Cars')
    return(plt.show())
