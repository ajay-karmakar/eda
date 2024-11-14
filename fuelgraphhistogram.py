import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile_data.csv')
print(df.head())

# Filter the DataFrame for 'gas' fuel type
df_gas = df[df['fuel-type'] == 'gas']

def gas():
    # Histogram for 'gas' fuel type
    plt.hist(df_gas['make'], color='pink', edgecolor='black', bins=20)
    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Histogram of Car Makes for Gasoline Cars')
    plt.xticks(rotation=45, ha='right')
    return(plt.show())

def diesel():
    # Filter the DataFrame for 'diesel' fuel type
    df_diesel = df[df['fuel-type'] == 'diesel']

    # Histogram for 'diesel' fuel type
    plt.hist(df_diesel['make'], color='skyblue', edgecolor='black', bins=20)
    plt.xlabel('Make')
    plt.ylabel('Count')
    plt.title('Histogram of Car Makes for Diesel Cars')
    plt.xticks(rotation=45, ha='right')
    return(plt.show())

gas()
diesel()
