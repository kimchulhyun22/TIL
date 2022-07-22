from async_database import Base
from sqlalchemy import Column, Integer, String


class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
