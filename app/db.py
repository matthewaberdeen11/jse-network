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
    
def save_company(symbol, company_name, market, sector, closing_price, pe_ratio):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""INSERT OR REPLACE INTO companies (symbol, company_name, market, sector, closing_price, pe_ratio) 
                   VALUES (?,?,?,?,?,?)""",(symbol, company_name, market, sector, closing_price, pe_ratio))
    conn.commit()
    conn.close()

def save_director(symbol,name,title,director_type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO OR REPLACE directors (symbol,name.title,director_type)
                   VALUES (?,?,?,?)""", (symbol,name,title,director_type))
    conn.commit()
    conn.close()