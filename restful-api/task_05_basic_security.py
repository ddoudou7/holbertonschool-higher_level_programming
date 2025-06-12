#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-me-secret"
auth = HTTPBasicAuth()
jwt  = JWTManager(app)

users = {
    "user1":  {"username": "user1",  "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_basic(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    user = users.get(data.get("username"))
    if user and check_password_hash(user["password"], data.get("password", "")):
        token = create_access_token(identity=user["username"], additional_claims={"role": user["role"]})
        return jsonify(access_token=token)
    return jsonify({"error": "Bad credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    role = users[username]["role"]
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def unauthorized(_):
    return jsonify({"error": "Missing or invalid token"}), 401
@jwt.invalid_token_loader
def invalid(_):
    return jsonify({"error": "Invalid token"}), 401
@jwt.expired_token_loader
def expired(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
