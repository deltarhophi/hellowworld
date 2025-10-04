# Utilise une image légère Python
FROM python:3.11-slim

# Répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers de dépendances d’abord (couche cache)
COPY requirements.txt .

# Installer les paquets
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port attendu par Northflank
EXPOSE 8080

# Commande de lancement en production
# -w 4 : 4 workers (ajuste selon la charge)
# -b 0.0.0.0:8080 : bind sur toutes les interfaces, port 8080
# main:app -> module `main.py`, objet Flask nommé `app`
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
