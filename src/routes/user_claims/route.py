from flasgger import swag_from
from flask import jsonify, request

from database.postgres import engine_postgres
from modules.user_claims import service
from routes.blueprints import user_claims_bp

engine = engine_postgres()


@user_claims_bp.route("/", methods=["POST"])
@swag_from("post.yml")
def post():
    try:
        data = request.get_json()
        response = service.post(data, engine)
        return jsonify(response), 201
    except Exception as e:
        raise e


@user_claims_bp.route("/", methods=["GET"])
@swag_from("get.yml")
def get():
    try:
        data = request.get_json()
        response = service.get(data, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@user_claims_bp.route("/", methods=["DELETE"])
@swag_from("delete.yml")
def delete():
    try:
        data = request.get_json()
        response = service.delete(data, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e
