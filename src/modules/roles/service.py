from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database.model import Role
from library.exceptions import NotFoundException


def post(body_data, engine):
    try:
        Session = sessionmaker(bind=engine)

        new_role = Role(description=body_data["description"])

        with Session() as session:
            session.add(new_role)
            session.commit()

        return {"response": "Role created successfully"}
    except Exception as e:
        raise e


def get(role_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = session.query(Role).filter(Role.id == role_id).one()

        return result.as_dict()
    except NoResultFound:
        raise NotFoundException(f"Role with id {role_id} not found")
    except Exception as e:
        raise e


def delete(role_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            session.query(Role).filter(Role.id == role_id).delete()
            session.commit()

        return {"response": "Role deleted successfully"}
    except NoResultFound:
        raise NotFoundException(f"User with id {role_id} not found")
    except Exception as e:
        raise e
