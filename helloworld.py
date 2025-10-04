print("🚀 HELLO WORLD FROM NORTHFLANK!")
print("🎉 Mon premier déploiement cloud!")

import time
import os

# Affiche l'environnement
print("\n📋 Environnement Northflank:")
for key, value in sorted(os.environ.items()):
    if any(word in key for word in ['HOST', 'PORT', 'USER', 'NAME']):
        print(f"   {key}: {value}")

# Reste actif
print("\n🟢 Application en cours d'exécution...")
counter = 0
while True:
    print(f"❤️  Heartbeat {counter} - Tout fonctionne!")
    counter += 1
    time.sleep(10)
