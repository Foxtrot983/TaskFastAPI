from sqlalchemy import Column, Integer, String

from db import Base


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, unique=False, index=True)