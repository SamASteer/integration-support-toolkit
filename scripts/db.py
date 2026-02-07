import sqlite3

DB_PATH = "data/integration_results.db"
def save_result(user_id, name, email, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO api_results (user_id, name, email, status)
        VALUES (?, ?, ?, ?)
    """, (user_id, name, email, status))

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            email TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
