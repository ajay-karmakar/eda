import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\AJAY KARMAKAR\PycharmProjects\PR391\Automobile_data.csv")


def histogram():
    df["horsepower"].value_counts().plot.hist(bins=6)
    plt.title("Horse Power Graph")
    plt.ylabel("Number of vehicles")
    plt.xlabel("HP")
    return(plt.show())


def barg():
    df["num-of-doors"].value_counts().plot.bar()
    plt.title("Number of doors")
    return(plt.show())


def piechart():
    df["drive-wheels"].value_counts().plot.pie(autopct="%.2f")
    plt.title("Horse Power Graph")
    return(plt.show())


