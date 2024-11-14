import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile_data.csv')
print(df.head())

def gas():
    df_gas = df[df['fuel-type'] == 'gas']

    gas_counts = df_gas['make'].value_counts()
    plt.pie(gas_counts, labels=gas_counts.index, autopct='%1.1f%%', colors=['pink', 'lightblue', 'lightgreen'],
            textprops={'fontsize': 5})
    plt.axis('equal')
    plt.title('Pie Chart of Car Makes for Gasoline Cars')
    return (plt.show())

def diesel():
    df_diesel = df[df['fuel-type'] == 'diesel']

    diesel_counts = df_diesel['make'].value_counts()
    plt.pie(diesel_counts, labels=diesel_counts.index, autopct='%1.1f%%', colors=['pink', 'lightblue', 'lightgreen'],textprops={'fontsize': 10})
    plt.axis('equal')
    plt.title('Pie Chart of Car Makes for Diesel Cars')
    return (plt.show())

gas()
diesel()
