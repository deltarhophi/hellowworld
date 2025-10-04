#!/usr/bin/env python3
print("🚀 HELLO WORLD FROM NORTHFLANK!")
print("🎉 Mon application Python fonctionne!")

import os
import time

# Affiche les variables d'environnement pour le débogage
print("\n📋 Variables d'environnement:")
for key, value in sorted(os.environ.items()):
    if any(term in key for term in ['HOST', 'PORT', 'MYSQL']):
        print(f"   {key}: {value}")

print("\n🟢 Application en cours d'exécution...")

# Boucle pour garder le conteneur actif
counter = 0
try:
    while True:
        print(f"❤️  Heartbeat {counter} - Tout fonctionne!")
        counter += 1
        time.sleep(30)  # Affiche un message toutes les 30 secondes
except KeyboardInterrupt:
    print("\n🛑 Arrêt de l'application")
