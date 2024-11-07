import sqlite3

def read_database():
    result = []
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM plant_prices;')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result