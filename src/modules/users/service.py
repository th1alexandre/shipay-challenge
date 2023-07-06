import secrets

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database.model import User
from library.exceptions import NotFoundException


def post(body_data, engine):
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


def get(user_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = session.query(User).filter(User.id == user_id).one()

        return result.as_dict()
    except NoResultFound:
        raise NotFoundException(f"User with id {user_id} not found")
    except Exception as e:
        raise e


def delete(user_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            session.query(User).filter(User.id == user_id).delete()
            session.commit()

        return {"response": "User deleted successfully"}
    except NoResultFound:
        raise NotFoundException(f"User with id {user_id} not found")
    except Exception as e:
        raise e
