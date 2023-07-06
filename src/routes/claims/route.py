from flasgger import swag_from
from flask import jsonify, request

from database.postgres import engine_postgres
from modules.claims import service
from routes.blueprints import claims_bp

engine = engine_postgres()


@claims_bp.route("/", methods=["POST"])
@swag_from("post.yml")
def post():
    try:
        data = request.get_json()
        response = service.post(data, engine)
        return jsonify(response), 201
    except Exception as e:
        raise e


@claims_bp.route("/<int:claim_id>", methods=["GET"])
@swag_from("get.yml")
def get(claim_id):
    try:
        response = service.get(claim_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@claims_bp.route("/<int:claim_id>", methods=["DELETE"])
@swag_from("delete.yml")
def delete(claim_id):
    try:
        response = service.delete(claim_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e
