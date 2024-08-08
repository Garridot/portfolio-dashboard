from flask import Blueprint, request, jsonify
from flaskr import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from .models import User
from .helpers import validate_password

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    valid, message = validate_password(password)
    if not valid:
        return jsonify({"error": message}), 400

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify({"error": "Username already exists"}), 400

    user = User(username, password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt_identity()
    return jsonify({"message": "Logged out successfully"}), 200

@auth_bp.route("/hello", methods=["GET"])
@jwt_required()
def hello_user():
    username = get_jwt_identity()
    return jsonify({"message": f"Hello, {username}!"}), 200

  
