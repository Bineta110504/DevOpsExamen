# tests/conftest.py
import sys
import os

# Ajouter le dossier parent au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))