import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\AJAY KARMAKAR\PycharmProjects\PR391\Automobile_data.csv')
print(df.head())

columns_to_plot = ['make', 'engine-location']

def enginefront():
    df_front = df[df['engine-location'] == 'front']
    front_counts = df_front[columns_to_plot[0]].value_counts()

    plt.pie(front_counts, labels=front_counts.index, autopct='%1.1f%%', colors=['orange', 'lightblue', 'lightgreen'],
            textprops={'fontsize': 5})
    plt.axis('equal')
    plt.title('Pie Chart of Car Makes for Front Engine Cars')
    return(plt.show())

def enginerear():
    df_rear = df[df['engine-location'] == 'rear']
    rear_counts = df_rear[columns_to_plot[0]].value_counts()

    plt.pie(rear_counts, labels=rear_counts.index, autopct='%1.1f%%', colors=['purple', 'lightblue', 'lightgreen'])
    plt.axis('equal')
    plt.title('Pie Chart of Car Makes for Rear Engine Cars')
    return(plt.show())

enginerear()
enginefront()
