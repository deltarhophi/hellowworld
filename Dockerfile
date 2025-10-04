# -------------------------------------------------
# Image de base légère contenant Python 3.11
# -------------------------------------------------
FROM python:3.11-slim

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Python
COPY hello_log.py .

# Aucun paquet supplémentaire n’est requis
# (si tu veux ajouter des dépendances, utilise un requirements.txt)

# Exposer un port même si on n’en a pas besoin – cela évite les warnings de Northflank
EXPOSE 8080

# Commande de lancement : le script restera actif quelques dizaines de secondes
CMD ["python", "hello_log.py"]
