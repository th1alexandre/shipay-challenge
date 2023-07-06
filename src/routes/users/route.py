from flasgger import swag_from
from flask import jsonify, request

from database.postgres import engine_postgres
from modules.users import service
from routes.blueprints import users_bp

engine = engine_postgres()


@users_bp.route("/", methods=["POST"])
@swag_from("post.yml")
def post():
    try:
        data = request.get_json()
        response = service.post(data, engine)
        return jsonify(response), 201
    except Exception as e:
        raise e


@users_bp.route("/<int:user_id>", methods=["GET"])
@swag_from("get.yml")
def get(user_id):
    try:
        response = service.get(user_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@users_bp.route("/<int:user_id>", methods=["DELETE"])
@swag_from("delete.yml")
def delete(user_id):
    try:
        response = service.delete(user_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e
