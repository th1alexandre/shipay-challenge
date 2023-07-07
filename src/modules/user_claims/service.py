from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from database.model import UserClaim
from library.exceptions import NotFoundException


def post(body_data, engine):
    try:
        Session = sessionmaker(bind=engine)

        new_user_claim = UserClaim(
            user_id=body_data["user_id"],
            claim_id=body_data["claim_id"],
        )

        with Session() as session:
            session.add(new_user_claim)
            session.commit()

        return {"response": "UserClaim created successfully"}
    except Exception as e:
        raise e


def get(body_data, engine):
    try:
        user_id = body_data["user_id"]
        claim_id = body_data["claim_id"]

        Session = sessionmaker(bind=engine)

        with Session() as session:
            result = (
                session.query(UserClaim)
                .filter(UserClaim.claim_id == claim_id)
                .filter(UserClaim.user_id == user_id)
                .one()
            )

        return result.as_dict()
    except NoResultFound:
        raise NotFoundException("UserClaim not found")
    except Exception as e:
        raise e


def delete(body_data, engine):
    try:
        user_id = body_data["user_id"]
        claim_id = body_data["claim_id"]

        Session = sessionmaker(bind=engine)

        with Session() as session:
            session.query(UserClaim).filter(UserClaim.claim_id == claim_id).filter(
                UserClaim.user_id == user_id
            ).delete()
            session.commit()

        return {"response": "UserClaim deleted successfully"}
    except NoResultFound:
        raise NotFoundException("UserClaim not found")
    except Exception as e:
        raise e
