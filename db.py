import sqlite3
DATABASE_NAME = "store.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE if not exists store(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    tax REAL NOT NULL,
    total REAL NOT NULL,
    quantity INTEGER NOT NULL
    )
    """)
    cursor.close()
    db.commit()
