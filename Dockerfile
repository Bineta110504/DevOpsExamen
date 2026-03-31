# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8501

# CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]


FROM python:3.11-slim

# Évite les buffers de Python pour les logs en temps réel
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source
COPY . .

# Créer le dossier logs pour l'application
RUN mkdir -p logs

# Exposer le port Streamlit
EXPOSE 8501

# Lancer l'application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]