import json
import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def load_json():
    with open("products.json") as f:
        return json.load(f)

def load_csv():
    products = []
    with open("products.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        data = load_json()
    elif source == "csv":
        data = load_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id is not None:
        product = next((p for p in data if p["id"] == product_id), None)
        if product:
            data = [product]
        else:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
