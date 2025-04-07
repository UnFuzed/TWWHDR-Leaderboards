from flask import Blueprint, request, abort

main = Blueprint('main', __name__)

@main.before_request
def before_request() -> None:
    if request.method in ["POST", "PUT", "PATCH"]:
        if "application/json" not in request.content_type:
            abort(400, description=f"Request type must be application/json, type was {request.content_type}")
       
@main.route('/', methods=["POST"])
def create_user() -> tuple[int, str]:
    return 'Hello World'
