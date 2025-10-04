# hello_log.py
import time
import sys

def main() -> None:
    # Écrire le message une première fois
    print("Hello, World!", flush=True)          # flush garantit que le texte arrive immédiatement dans les logs

    # Garder le conteneur actif pendant quelques secondes
    # (sinon le conteneur s’arrête immédiatement et les logs disparaissent)
    for i in range(30):                         # 30 itérations → ~30 s
        time.sleep(1)
        print(f"[{i+1}s] Still alive…", flush=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Gestion propre de l’interruption (CTRL+C depuis le dashboard)
        print("\nReceived stop signal – exiting.", flush=True)
        sys.exit(0)
