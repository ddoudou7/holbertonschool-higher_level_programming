#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    item_list = ['apple', 'banana', 'cherry']
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True)
