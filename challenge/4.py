import secrets

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.model import User

engine = create_engine("postgresql://username:password@localhost:5432/shipay")
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------------------------------------------------- #
# src/routes/route.py -> create_user()

body_data = {
    "name": "Thiago Alexandre",
    "email": "th1alexandre.dev@gmail.com",
    # "password": "0123456789abcdef",
    "role_id": 1,
}

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
