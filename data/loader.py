import seaborn as sns
import pandas as pd

def load_titanic_data():
    """
    Charge le dataset Titanic depuis seaborn et nettoie les données
    """
    # Charger les données
    df = sns.load_dataset('titanic')
    
    # Nettoyage des valeurs nulles
    df['age'].fillna(df['age'].median(), inplace=True)
    df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
    df['deck'] = df['deck'].astype(str).fillna('Unknown')
    
    # Ajouter une colonne tranche d'âge
    df['age_group'] = pd.cut(df['age'], 
                             bins=[0, 12, 18, 35, 60, 100],
                             labels=['Enfant', 'Adolescent', 'Adulte', 'Adulte+', 'Senior'])
    
    return df

def get_data_info(df):
    """
    Retourne les statistiques principales
    """
    return {
        'total_passagers': len(df),
        'survie_rate': df['survived'].mean() * 100,
        'age_moyen': df['age'].mean(),
        'hommes': len(df[df['sex'] == 'male']),
        'femmes': len(df[df['sex'] == 'female'])
    }