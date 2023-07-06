import secrets

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database.model import Claim, Role, User, UserClaim
from library.exceptions import NotFoundException

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


def query_1(user_id, engine):
    """
    2.- Utilizando a mesma estrutura do banco de dados da questão anterior,
    rescreva a consulta anterior utilizando um ORM (Object Relational Mapping) de sua preferência
    utilizando a query language padrão do ORM adotado (ex.: Spring JOOQ, EEF LINQ, SQL Alchemy Expression Language, etc).
    """
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = (
                session.query(
                    User.name,
                    User.email,
                    Role.description.label("role"),
                    Claim.description.label("claim"),
                )
                .join(UserClaim, User.id == UserClaim.user_id, isouter=True)
                .join(Claim, UserClaim.claim_id == Claim.id, isouter=True)
                .join(Role, User.role_id == Role.id)
                .filter(User.id == user_id)
                .one()
            )

        return {"response": result._asdict()}
    except NoResultFound:
        raise NotFoundException(f"User with id {user_id} not found")
    except Exception as e:
        raise e


def role_description(role_id, engine):
    """
    3.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar,
    construa uma API REST que irá listar o papel de um usuário pelo “Id” (role_id).
    """
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = session.query(Role.description).filter(Role.id == role_id).one()

        return result._asdict()
    except NoResultFound:
        raise NotFoundException(f"Role with id {role_id} not found")
    except Exception as e:
        raise e


def create_user(body_data, engine):
    """
    4.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar,
    construa uma API REST que irá criar um usuário. Os campos obrigatórios serão nome, e-mail e papel do usuário.
    A senha será um campo opcional, caso o usuário não informe uma senha o serviço da API deverá gerar essa senha automaticamente.
    """
    try:
        Session = sessionmaker(bind=engine)

        if "password" not in body_data.keys():
            # Generate a random 16 characters alphanumeric password
            body_data["password"] = secrets.token_hex(8)  # 8 bytes = 16 characters

        new_user = User(
            name=body_data["name"],
            email=body_data["email"],
            role_id=body_data["role_id"],
            password=body_data["password"],
        )

        with Session() as session:
            session.add(new_user)
            session.commit()

        return {"response": "User created successfully"}
    except Exception as e:
        raise e
