import sqlite3

DB_NAME = "jse_network.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS companies (
                   symbol TEXT PRIMARY KEY,
                   company_name TEXT NOT NULL,
                   market TEXT,
                   sector TEXT,
                   closing_price REAL,
                   pe_ratio REAL
                )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS directors(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   symbol TEXT NOT NULL,
                   name TEXT NOT NULL,
                   title TEXT,
                   director_type TEXT
                )""")
    
    conn.commit()
    conn.close()
    
