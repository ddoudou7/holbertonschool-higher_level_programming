import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f), None
    except Exception as e:
        return [], f"Error reading JSON: {e}"

def read_csv():
    try:
        with open("products.csv", newline='') as f:
            reader = csv.DictReader(f)
            return list(reader), None
    except Exception as e:
        return [], f"Error reading CSV: {e}"

def read_sqlite():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        conn.close()
        return products, None
    except Exception as e:
        return [], f"Database error: {e}"

@app.route('/products')
def products():
    source = request.args.get("source")
    id_filter = request.args.get("id")
    error = None

    if source == "json":
        data, error = read_json()
    elif source == "csv":
        data, error = read_csv()
    elif source == "sql":
        data, error = read_sqlite()
    else:
        data = []
        error = "Wrong source"

    if id_filter and not error:
        try:
            id_int = int(id_filter)
            data = [p for p in data if int(p["id"]) == id_int]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template("product_display.html", products=data, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
