import os
import time
import sys

def main() -> None:
    # Nom de la variable telle qu’elle apparaît dans Northflank
    VAR_NAME = "NF_PLAN_ID"          # ← remplacez par le vrai nom

    # Récupération de la valeur (ou d’une valeur de secours si elle n’est pas définie)
    valeur = os.getenv(VAR_NAME, "<non définie>")
    print(f"Valeur de {VAR_NAME} : {valeur}", flush=True)

    # Le reste de votre logique
    print("Hello, World!", flush=True)
    for i in range(60):
        time.sleep(1)
        print(f"[{i+1}s] Still alive…", flush=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nReceived stop signal – exiting.", flush=True)
        sys.exit(0)
