import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    with open("items.json", "r") as f:
        data = json.load(f)
    item_list = data.get("items", [])
    return render_template("items.html", items=item_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
