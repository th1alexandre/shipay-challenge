from flasgger import swag_from
from flask import Blueprint, jsonify, request

from database.postgres import engine_postgres
from modules import service

generic_bp = Blueprint("Generic", __name__)
engine = engine_postgres()


"""
    1.- Construa uma consulta SQL que retorne o nome, e-mail, a descrição do papel
        e as descrições das permissões/claims que um usuário possui.

    SELECT
        u.name,
        u.email,
        r.description AS role,
        c.description AS claim
    FROM
        users u
        JOIN roles r ON u.role_id = r.id
        LEFT JOIN user_claims uc ON u.id = uc.user_id
        LEFT JOIN claims c ON uc.claim_id = c.id
    WHERE
        u.id = _INFORMAR_ID_DO_USUARIO_AQUI_;
"""


@generic_bp.route("/<int:user_id>", methods=["GET"])
@swag_from("query_1.yml")
def query_1(user_id):
    """
    2.- Utilizando a mesma estrutura do banco de dados da questão anterior,
    rescreva a consulta anterior utilizando um ORM (Object Relational Mapping) de sua preferência
    utilizando a query language padrão do ORM adotado (ex.: Spring JOOQ, EEF LINQ, SQL Alchemy Expression Language, etc).
    """
    try:
        response = service.query_1(user_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@generic_bp.route("/role/<int:role_id>", methods=["GET"])
@swag_from("role_description.yml")
def role_description(role_id):
    """
    3.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar,
    construa uma API REST que irá listar o papel de um usuário pelo “Id” (role_id).
    """
    try:
        response = service.role_description(role_id, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e


@generic_bp.route("/user", methods=["POST"])
@swag_from("create_user.yml")
def create_user():
    """
    4.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar,
    construa uma API REST que irá criar um usuário. Os campos obrigatórios serão nome, e-mail e papel do usuário.
    A senha será um campo opcional, caso o usuário não informe uma senha o serviço da API deverá gerar essa senha automaticamente.
    """
    try:
        data = request.get_json()
        response = service.create_user(data, engine)
        return jsonify(response), 200
    except Exception as e:
        raise e
