from db import get_db


def calculate_tax(category, price, quantity):
    total = price * quantity
    tax = 0.0
    if category in ("Medicine", "Food"):
        tax = 0.05 * total
    elif category in ("Clothes"):
        if total > 1000.0:
            tax = 0.12 * total
        else:
            tax = 0.05 * total
    elif category in ("Music"):
        tax = 0.03 * total
    elif category in ("Imported"):
        tax = 0.18 * total
    return tax


def insert_item(name, category, price, quantity):
    tax = calculate_tax(category, price, quantity)
    total = price + tax
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO store(name, category, price, tax, total, quantity) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [name, category, price, tax, total, quantity])
    db.commit()
    return True


def get_items():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM store"
    cursor.execute(query)
    return cursor.fetchall()
