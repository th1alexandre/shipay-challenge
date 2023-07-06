from datetime import datetime as dt

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


class Claim(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(Date, nullable=False, default=dt.utcnow)
    updated_at = Column(Date, onupdate=dt.utcnow)

    role = relationship("Role", backref="users")
    claims = relationship("Claim", secondary="user_claims")


class UserClaim(Base):
    __tablename__ = "user_claims"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), primary_key=True)
