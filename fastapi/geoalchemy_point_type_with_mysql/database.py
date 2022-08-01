from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import func
from sqlalchemy.types import UserDefinedType


Base = declarative_base()

DATABASE_URL = "mysql+pymysql://root:sdfsdfsdf@localhost:3306/test_db"


session = sessionmaker()

Base = declarative_base()

engine = create_engine(DATABASE_URL)

Base.metadata.bind = engine


class Point(UserDefinedType):
    def get_col_spec(self):
        return "POINT SRID 4326"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, 4326, type_=self)

    def column_expression(self, col):
        print(col)
        return func.ST_AsWKB(col, type_=self)


class TestGeometry(Base):
    __tablename__ = "test_geometry"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    point = Column(Point, nullable=False)


Base.metadata.create_all(engine, checkfirst=True)
