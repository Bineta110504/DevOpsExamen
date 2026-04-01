import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.loader import load_titanic_data, get_data_info

def test_load_data():
    """Test que le chargement des données fonctionne"""
    df = load_titanic_data()
    assert df is not None
    assert len(df) == 891

def test_columns():
    """Test que toutes les colonnes attendues sont présentes"""
    df = load_titanic_data()
    assert 'survived' in df.columns
    assert 'age_group' in df.columns
    assert 'deck' in df.columns

def test_no_nulls():
    """Test qu'il n'y a pas de valeurs nulles"""
    df = load_titanic_data()
    assert df['age'].isnull().sum() == 0
    assert df['embarked'].isnull().sum() == 0
    assert df['deck'].isnull().sum() == 0

def test_age_groups():
    """Test que les tranches d'âge sont correctes"""
    df = load_titanic_data()
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