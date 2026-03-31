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
import numpy as np
import logging

# Configuration du logger
logger = logging.getLogger(__name__)

def load_titanic_data():
    """
    Charge le dataset Titanic depuis seaborn et nettoie les données
    
    Returns:
        pd.DataFrame: DataFrame nettoyé du dataset Titanic
    """
    try:
        # Charger les données
        logger.info("Chargement du dataset Titanic...")
        df = sns.load_dataset('titanic')
        logger.info(f"Dataset chargé: {len(df)} lignes, {len(df.columns)} colonnes")
        
        # Créer une copie pour éviter les warnings
        df = df.copy()
        
        # 1. Nettoyage de la colonne 'age'
        age_median = df['age'].median()
        df['age'] = df['age'].fillna(age_median)
        logger.info(f"Âge médian utilisé: {age_median:.1f} ans")
        
        # 2. Nettoyage de la colonne 'embarked'
        embarked_mode = df['embarked'].mode()[0]
        df['embarked'] = df['embarked'].fillna(embarked_mode)
        logger.info(f"Port d'embarquement majoritaire: {embarked_mode}")
        
        # 3. CORRECTION: Gestion de la colonne 'deck' (Categorical)
        df['deck'] = df['deck'].astype('object').fillna('Unknown')
        logger.info(f"Decks disponibles: {df['deck'].unique()}")
        
        # 4. Ajouter la colonne tranche d'âge
        df['age_group'] = pd.cut(
            df['age'], 
            bins=[0, 12, 18, 35, 60, 100],
            labels=['Enfant', 'Adolescent', 'Adulte', 'Adulte+', 'Senior'],
            include_lowest=True
        )
        
        # 5. Ajouter une colonne de prix par classe (pour analyse)
        df['fare_category'] = pd.qcut(
            df['fare'].fillna(df['fare'].median()),
            q=4,
            labels=['Économique', 'Modéré', 'Élevé', 'Luxe']
        )
        
        logger.info("✅ Nettoyage terminé avec succès!")
        
        return df
        
    except Exception as e:
        logger.error(f"❌ Erreur lors du chargement: {e}")
        raise

def get_data_info(df):
    """
    Retourne les statistiques principales
    
    Args:
        df (pd.DataFrame): DataFrame Titanic
        
    Returns:
        dict: Dictionnaire des statistiques
    """
    if df is None or len(df) == 0:
        return {
            'total_passagers': 0,
            'survie_rate': 0,
            'age_moyen': 0,
            'hommes': 0,
            'femmes': 0
        }
    
    return {
        'total_passagers': len(df),
        'survie_rate': round(df['survived'].mean() * 100, 2),
        'age_moyen': round(df['age'].mean(), 1),
        'hommes': len(df[df['sex'] == 'male']),
        'femmes': len(df[df['sex'] == 'female']),
        'prix_moyen': round(df['fare'].mean(), 2),
        'enfants': len(df[df['age'] < 18])
    }

def get_survival_stats(df):
    """
    Calcule les statistiques de survie détaillées
    
    Args:
        df (pd.DataFrame): DataFrame Titanic
        
    Returns:
        dict: Statistiques de survie
    """
    stats = {
        'par_sexe': df.groupby('sex')['survived'].mean().to_dict(),
        'par_classe': df.groupby('class')['survived'].mean().to_dict(),
        'par_age_group': df.groupby('age_group')['survived'].mean().to_dict(),
        'global_rate': round(df['survived'].mean() * 100, 2)
    }
    
    # Convertir les valeurs en pourcentages
    for key in stats:
        if key != 'global_rate':
            stats[key] = {k: round(v * 100, 2) for k, v in stats[key].items()}
    
    return stats

# Test du module
if __name__ == "__main__":
    # Configuration du logging pour le test
    logging.basicConfig(level=logging.INFO)
    
    print("=" * 50)
    print("Test du module loader.py")
    print("=" * 50)
    
    # Tester le chargement
    df = load_titanic_data()
    print(f"\n✅ Dataset chargé: {len(df)} passagers")
    
    # Tester get_data_info
    info = get_data_info(df)
    print("\n📊 Statistiques générales:")
    for key, value in info.items():
        print(f"  - {key}: {value}")
    
    # Tester get_survival_stats
    stats = get_survival_stats(df)
    print("\n💀 Statistiques de survie:")
    print(f"  - Global: {stats['global_rate']}%")
    print(f"  - Par sexe: {stats['par_sexe']}")
    print(f"  - Par classe: {stats['par_classe']}")
    
    print("\n✅ Tous les tests passés!")