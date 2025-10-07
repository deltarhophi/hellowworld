# db_test.py
import os
import sys
import time
import psycopg2
from psycopg2 import OperationalError, sql

# ----------------------------------------------------------------------
# Helper – récupère la connexion en utilisant les variables héritées
# ----------------------------------------------------------------------
def get_connection():
    """
    Construit la DSN à partir des variables d’environnement injectées
    par le Secret Group du PostgreSQL addon.
    """
    # On privilégie les variables héritées (préfixées NF_…) ;
    # on fournit un fallback vers les noms courts au cas où tu les aurais
    # ajoutés manuellement.
    conn = psycopg2.connect(
        host=os.getenv("NF_HELLO_ADDON_PSQL_HOST") or os.getenv("DB_HOST"),
        port=os.getenv("NF_HELLO_ADDON_PSQL_PORT") or os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("NF_HELLO_ADDON_PSQLL_DATABASE") or os.getenv("DB_NAME"),
        user=os.getenv("NF_HELLO_ADDON_PSQL_USERNAME") or os.getenv("DB_USER"),
        password=os.getenv("NF_HELLO_ADDON_PSQL_PASSWORD") or os.getenv("DB_PASSWORD"),
        # Si TLS est activé, on demande à psycopg2 d’utiliser SSL.
        sslmode="require" if os.getenv("NF_HELLO_ADDON_PSQL_TLS_ENABLED", "false").lower() == "true"
        else "disable",
    )
    return conn


# ----------------------------------------------------------------------
# Optionnel : attendre que le serveur soit prêt (utile au premier démarrage)
# ----------------------------------------------------------------------
def wait_for_db(retries: int = 12, delay: int = 5):
    """Essaye de se connecter plusieurs fois avant d’abandonner."""
    for attempt in range(1, retries + 1):
        try:
            conn = get_connection()
            conn.close()
            print("✅ PostgreSQL est joignable", flush=True)
            return
        except OperationalError as exc:
            print(
                f"⏳ Tentative {attempt}/{retries} – PostgreSQL pas encore dispo ({exc})",
                flush=True,
            )
            time.sleep(delay)
    raise RuntimeError("Impossible de se connecter à PostgreSQL après plusieurs essais.")


# ----------------------------------------------------------------------
# Main – exécute la requête simple
# ----------------------------------------------------------------------
def main():
    try:
        wait_for_db()                     # <-- attend que le service soit up
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql.SQL("SELECT CURRENT_TIMESTAMP"))
        ts = cur.fetchone()[0]
        print(f"Timestamp actuel depuis PostgreSQL : {ts}", flush=True)

        # Exemple de boucle de vie du conteneur (similaire à ton hello_log.py)
        for i in range(10):
            time.sleep(1)
            print(f"[{i+1}s] still alive…", flush=True)

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Erreur : {e}", file=sys.stderr, flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
