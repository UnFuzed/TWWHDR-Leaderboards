from typing import Any, List
from flask import Blueprint, jsonify, request, abort, Response
from api.models import Role, User, Week, Record
from api import db
from flask_jwt_extended import create_refresh_token, create_access_token, get_jwt_identity, jwt_required

main = Blueprint('main', __name__)

# Ensure all requests (except get requests) are json data
@main.before_request
def before_request() -> None:
    if request.method in ["POST", "PUT", "PATCH"]:
        if "application/json" not in request.content_type:
            abort(400, description=f"Request type must be application/json, type was {request.content_type}")


@main.route("/login", methods=["POST"])
def login() -> Response:
    data: dict[str, any] = request.get_json()
    user_name: str = data.get("user_name")
    password: str = data.get("password")

    if not user_name or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user: User = User.query.filter_by(user_name=user_name).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token: str = create_access_token(identity=str(user.user_id), additional_claims={"role": user.role.name})
    refresh_token: str = create_refresh_token(identity=str(user.user_id))

    return jsonify(access_token=access_token, refresh_token=refresh_token), 200




@main.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh() -> Response:
    user_id: int = get_jwt_identity()

    user: User = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    new_access_token: str = create_access_token(identity=str(user.user_id), additional_claims={"role": user.role.name})

    return jsonify(access_token=new_access_token), 200


# User routes
@main.route("/get_all_users", methods=["GET"])
def get_all_users() -> Response:
    users: List[User] = User.query.all()
    usersList: List[dict[str, Any]] = [user.as_dict() for user in users]

    return jsonify(usersList)

@main.route("/get_user/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id: int) -> Response:
    user: User = User.query.filter_by(user_id=user_id).first()

    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user.as_dict())

# sign up route
@main.route("/create_user", methods=["POST"])
def create_user() -> Response:
    data: dict[str, any] = request.get_json()

    user_name: str = data.get("user_name")
    password: str = data.get("password")
    role: str = data.get("role")

    missing: list[str] = [k for k, v in {"user_name": user_name, "password": password, "role": role}.items() if not v]
    if missing:
        return jsonify({"message": f"Missing parameter(s): {', '.join(missing)}"}), 400
    
    if User.query.filter_by(user_name=user_name).first():
        return jsonify({"message": "username is already taken"}), 409

    newUser: User = User(user_name = user_name, role = role)
    newUser.set_password(password)

    try:
        db.session.add(newUser)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occured while creating the user: {e}"})
    

    return jsonify({"message": f"User ID: {newUser.user_id} was created successfully!"}), 201

@main.route("/delete_user/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id: int) -> Response:
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

@main.route("/update_user/<int:user_id>", methods=["PUT"])
@jwt_required()  
def update_user(user_id: int) -> Response:
    user: User = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data: dict[str, any] = request.get_json()

    user.user_name = data["user_name"]
    user.password = data["password"]
    user.role = data["role"]

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error occured while updating the user"})
    
    return jsonify(user.as_dict()), 200

@main.route("/get_all_weeks", methods=["GET"])
def get_all_weeks() -> Response:
    try:
        weeks: List[Week] = Week.query.all()
    except:
        return jsonify({"error": "Error occured while querying weeks"})
    else:
        weeksList: List[dict[str, Any]] = [week.as_dict() for week in weeks]

    return jsonify(weeksList)

@main.route("/create_week", methods=["POST"])
@jwt_required()
def create_week() -> Response:
    pass

@main.route("/delete_week<int:week_id>")
@jwt_required()
def delete_week(week_id : int) -> Response:
    pass

@main.route("/update_week<int:week_id>")
@jwt_required()
def update_week(week_id : int,) -> Response:
    pass

# Record Routes
@main.route("/get_all_records", methods=["GET"])
@jwt_required()
def get_all_records() -> Response:
    records: List[Week] = Record.query.all()
    recordsList: List[dict[str, Any]] = [record.as_dict() for record in records]

    return jsonify(recordsList)

