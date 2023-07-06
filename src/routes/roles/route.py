from flasgger import swag_from
from flask import jsonify, request

from database.postgres import engine_postgres
from modules.roles import service
from routes.blueprints import roles_bp

engine = engine_postgres()


@roles_bp.route("/", methods=["POST"])
@swag_from("post.yml")
def post():
    try:
        data = request.get_json()
        response = service.post(data, engine)
        return jsonify(response), 201
    except Exception as e:
        raise e


@roles_bp.route("/<int:role_id>", methods=["GET"])
@swag_from("get.yml")
def get(role_id):
    try:
        response = service.get(role_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@roles_bp.route("/<int:role_id>", methods=["DELETE"])
@swag_from("delete.yml")
def delete(role_id):
    try:
        response = service.delete(role_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e
