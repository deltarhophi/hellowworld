# db_test.py
import os
import sys
import time
import psycopg2
from psycopg2 import sql

def get_connection():
    """Construit la DSN à partir des variables d’environnement."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def main():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql.SQL("SELECT CURRENT_TIMESTAMP"))
        ts = cur.fetchone()[0]
        print(f"Timestamp actuel depuis PostgreSQL : {ts}", flush=True)

        # Optionnel : garder le conteneur vivant comme ton script original
        for i in range(10):
            time.sleep(1)
            print(f"[{i+1}s] still alive…", flush=True)

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erreur : {e}", file=sys.stderr, flush=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
