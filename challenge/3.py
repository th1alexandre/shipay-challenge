from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.model import Role

engine = create_engine("postgresql://username:password@localhost:5432/shipay")
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------------------------------------------------- #
# src/routes/route.py -> role_description()

role_id = 123456789
result = session.query(Role.description).filter(Role.id == role_id).one()

# return result._asdict()
