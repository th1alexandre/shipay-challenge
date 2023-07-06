from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.model import Claim, Role, User, UserClaim

engine = create_engine("postgresql://username:password@localhost:5432/shipay")
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------------------------------------------------- #
# src/routes/route.py -> query_1()

user_id = 123456789
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

# return result._asdict()
