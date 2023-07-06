from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database.model import Claim
from library.exceptions import NotFoundException


def post(body_data, engine):
    try:
        Session = sessionmaker(bind=engine)

        new_user = Claim(
            description=body_data["description"],
            active=body_data["active"],
        )

        with Session() as session:
            session.add(new_user)
            session.commit()

        return {"response": "Claim created successfully"}
    except Exception as e:
        raise e


def get(claim_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = session.query(Claim).filter(Claim.id == claim_id).one()

        return result.as_dict()
    except NoResultFound:
        raise NotFoundException(f"Claim with id {claim_id} not found")
    except Exception as e:
        raise e


def delete(claim_id, engine):
    try:
        Session = sessionmaker(bind=engine)

        with Session() as session:
            session.query(Claim).filter(Claim.id == claim_id).delete()
            session.commit()

        return {"response": "Claim deleted successfully"}
    except NoResultFound:
        raise NotFoundException(f"Claim with id {claim_id} not found")
    except Exception as e:
        raise e
