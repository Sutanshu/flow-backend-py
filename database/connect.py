import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from database.classes import Base

engine = create_engine(
    os.environ['DB_HOST'], echo=True)

session = sessionmaker(engine)

Base.metadata.create_all(engine)
