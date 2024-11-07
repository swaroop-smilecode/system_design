import sqlite3

def create_database():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS plant_prices (
            id INTEGER PRIMARY KEY,
            name TEXT,
             price INTEGER);
            ''')
    conn.commit()
    conn.close()

data = [(1, "rose", 100), (2, "orchid", 200), (3, "marigold", 300)]
def load_database():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.executemany('INSERT OR REPLACE INTO plant_prices VALUES (?,?,?)', data) 
    conn.commit()
    conn.close()

def setup_database():
    create_database()
    load_database()