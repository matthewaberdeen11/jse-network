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
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS shareholders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    name TEXT NOT NULL,
                    percentage REAL,
                    share_count TEXT
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
    cursor.execute("""INSERT OR REPLACE INTO directors (symbol,name,title,director_type)
                   VALUES (?,?,?,?)""", (symbol,name,title,director_type))
    conn.commit()
    conn.close()


def get_graph_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT symbol, company_name, market, closing_price FROM companies""")
    companies = cursor.fetchall()

    cursor.execute("""SELECT d1.symbol, d2.symbol, d1.name
                   FROM directors d1
                   JOIN directors d2 ON d1.name = d2.name
                   WHERE d1.symbol < d2.symbol""")
    connections = cursor.fetchall()

    conn.close()

    nodes = []
    for row in companies:
        symbol, company_name, market, closing_price = row
        nodes.append({"id": symbol, "label": company_name, "market": market, "price": closing_price})
    
    edges = []
    for row in connections:
        symbol1, symbol2, name = row
        edges.append({"from": symbol1, "to": symbol2, "director": name})

    return {"nodes": nodes, "edges": edges}
    
def clear_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM directors")
    cursor.execute("DELETE FROM companies")
    cursor.execute("DELETE FROM shareholders")
    conn.commit()
    conn.close()

def save_shareholder(symbol, name, percentage, share_count):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO shareholders (symbol, name, percentage, share_count)
                      VALUES (?, ?, ?, ?)""", (symbol, name, percentage, share_count))
    conn.commit()
    conn.close()

def get_shareholders(symbol):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, percentage, share_count FROM shareholders WHERE symbol = ?", (symbol,))
    rows = cursor.fetchall()
    conn.close()
    return [{"name": r[0], "percentage": r[1], "shares": r[2]} for r in rows]

def get_directors(symbol):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, title, director_type FROM directors WHERE symbol = ?", (symbol,))
    rows = cursor.fetchall()
    conn.close()
    return [{"name": r[0], "title": r[1], "type": r[2]} for r in rows]