"""
This file is a template for a SQLAlchemy table model.
Copy the code below into a new file and change the examples to your needs.

You have two options for storing your models: (if you have only one database and schema)
    1. Create a new file and use the table name as the file name
       Put this file inside src/database/models/"table_name".py
       Each table in your database will be a new file inside models/
    2. Create a new file called models.py or similar
       Put this file inside src/database/models/
       Each table in your database will be a new class inside models.py
       Delete the src/database/models/ package and put the
       "models.py" file inside src/database/

I personally recommend option 2, as it is easier to use because you
don't need to import multiple python modules (files) to use multiple models.
"""
from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TableA(Base):
    __tablename__ = "table_a"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    column_a = Column(String(100), nullable=False)
    column_b = Column(Integer, nullable=False)
