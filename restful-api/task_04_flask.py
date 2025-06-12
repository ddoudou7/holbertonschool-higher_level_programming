#!/usr/bin/env python3
"""Task 04 – Mini REST API with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users: dict[str, dict] = {}   # in-memory store (vide au démarrage)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def list_usernames():
    return jsonify(sorted(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    return (jsonify(user) if user
            else (jsonify({"error": "User not found"}), 404))


@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()           # 127.0.0.1:5000
