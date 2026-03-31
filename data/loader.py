# import seaborn as sns


# def load_data():
#     df = sns.load_dataset("titanic")

#     # nettoyage simple
#     df = df.drop_duplicates()

#     # gérer valeurs nulles
#     df["age"] = df["age"].fillna(df["age"].median())
#     df["embarked"] = df["embarked"].fillna("Unknown")

#     return df


import seaborn as sns
import pandas as pd

def load_titanic_data():
    df = sns.load_dataset('titanic')
    df = df.copy()
    
    # Nettoyer les données
    df['age'].fillna(df['age'].median(), inplace=True)
    df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
    df['deck'] = df['deck'].astype(str).fillna('Unknown')
    
    # Ajouter tranche d'âge
    df['age_group'] = pd.cut(df['age'], 
                             bins=[0, 12, 18, 35, 60, 100],
                             labels=['Enfant', 'Adolescent', 'Adulte', 'Adulte+', 'Senior'])
    
    return df

def get_data_info(df):
    return {
        'total_passagers': len(df),
        'survie_rate': df['survived'].mean() * 100,
        'age_moyen': df['age'].mean(),
        'hommes': len(df[df['sex'] == 'male']),
        'femmes': len(df[df['sex'] == 'female'])
    }
"@ | Out-File -FilePath data\loader.py -Encoding utf8