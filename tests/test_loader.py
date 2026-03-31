import pytest
from data.loader import load_titanic_data, get_data_info

def test_load_data():
    """Test que le chargement des données fonctionne"""
    df = load_titanic_data()
    assert df is not None
    assert len(df) > 0
    assert len(df) == 891

def test_data_columns():
    """Test que toutes les colonnes attendues sont présentes"""
    df = load_titanic_data()
    expected_columns = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 
                        'fare', 'embarked', 'class', 'who', 'deck', 'age_group']
    
    for col in expected_columns:
        assert col in df.columns, f"Colonne {col} manquante"

def test_no_null_values_in_critical_columns():
    """Test qu'il n'y a pas de valeurs nulles dans les colonnes critiques"""
    df = load_titanic_data()
    critical_columns = ['age', 'embarked', 'deck']
    
    for col in critical_columns:
        assert df[col].isnull().sum() == 0, f"Colonne {col} a des valeurs nulles"

def test_age_groups():
    """Test que les tranches d'âge sont correctement créées"""
    df = load_titanic_data()
    assert 'age_group' in df.columns
    valid_groups = ['Enfant', 'Adolescent', 'Adulte', 'Adulte+', 'Senior']
    assert df['age_group'].dropna().isin(valid_groups).all()

def test_get_data_info():
    """Test que get_data_info retourne les bonnes informations"""
    df = load_titanic_data()
    info = get_data_info(df)
    
    assert 'total_passagers' in info
    assert 'survie_rate' in info
    assert 'age_moyen' in info
    assert info['total_passagers'] == len(df)
    assert 0 <= info['survie_rate'] <= 100

def test_survival_rate_reasonable():
    """Test que le taux de survie est entre 0 et 100%"""
    df = load_titanic_data()
    survival_rate = df['survived'].mean() * 100
    assert 0 <= survival_rate <= 100