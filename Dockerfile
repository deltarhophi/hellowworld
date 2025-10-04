# Dockerfile (renomme le .txt en Dockerfile)
FROM python:3.11-slim

WORKDIR /app

# Copie du fichier de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source (inclut hello_log.py, db_test.py, etc.)
COPY . .

# Commande de lancement – tu peux choisir le script que tu veux exécuter
# Exemple : exécuter db_test.py puis hello_log.py
CMD ["python", "db_test.py"]
