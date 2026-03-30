# data/loader.py
import seaborn as sns
import pandas as pd

def load_data():
    df = sns.load_dataset("titanic")

    # nettoyage simple
    df = df.drop_duplicates()

    # gérer valeurs nulles
    df["age"] = df["age"].fillna(df["age"].median())
    df["embarked"] = df["embarked"].fillna("Unknown")

    return df