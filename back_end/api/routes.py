from typing import Any, List
from flask import Blueprint, jsonify, request, abort
from api.models import Role, User, Week, Record
from api import db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

main = Blueprint('main', __name__)

@main.before_request
def before_request() -> None:
    if request.method in ["POST", "PUT", "PATCH"]:
        if "application/json" not in request.content_type:
            abort(400, description=f"Request type must be application/json, type was {request.content_type}")

# User routes

@main.route("/get_all_users", methods=["GET"])
def get_all_users() -> List[dict[str, any]]:
    users: List[User] = User.query.all()
    usersList: List[dict[str, Any]] = [user.as_dict() for user in users]

    return jsonify(usersList)

@jwt_required  
@main.route("/create_user", methods=["POST"])
def create_user() -> tuple[dict[str, str], int]:
    data: dict[str, any] = request.get_json()

    user_name: str | None = data.get("user_name")
    hashed_password: str | None = data.get("hashed_password")
    role: Role | None = data.get("role")

    missing: list[str] = [k for k, v in {"user_name": user_name, "hashed_password": hashed_password, "role": role}.items() if not v]
    if missing:
        return jsonify({"message": f"Missing parameter(s): {', '.join(missing)}"}), 400

    newUser: User = User(user_name = user_name, hashed_password = hashed_password, role = role)

    try:
        db.session.add(newUser)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occured while creating the user: {e}"})
    

    return jsonify({"message": f"User ID: {newUser.user_id} was created successfully!"}), 201

@jwt_required
@main.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int) -> tuple[dict[str, str], int]:
    user: User = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occured while deleting the user: {e}"})

    return jsonify({"message": f"User ID: {user_id} was deleted successfully!"}), 200

@jwt_required  
@main.route("/update_user/<int:user_id>", methods=["PUT"])
def update_user(user_id: int,) -> tuple[dict[str, any], int]:
    user: User = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data: dict[str, any] = request.get_json()

    user.user_name = data["user_name"]
    user.hashed_password = data["hashed_password"]
    user.role = data["role"]

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error occured while updating the user"})
    
    return jsonify(user.as_dict()), 200


# Week Routes
@jwt_required
@main.route("/get_all_weeks", methods=["GET"])
def get_all_weeks() -> list[dict[str, Any]]:
    weeks: List[Week] = Week.query.all()
    weeksList: List[dict[str, Any]] = [week.as_dict() for week in weeks]

    return jsonify(weeksList)

# Record Routes
@jwt_required
@main.route("/get_all_records", methods=["GET"])
def get_all_records() -> list[dict[str, Any]]:
    records: List[Week] = Record.query.all()
    recordsList: List[dict[str, Any]] = [record.as_dict() for record in records]

    return jsonify(recordsList)

