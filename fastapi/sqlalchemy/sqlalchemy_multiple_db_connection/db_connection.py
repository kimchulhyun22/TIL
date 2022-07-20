from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Session = sessionmaker()

Base = declarative_base()

engine = create_engine(
    "mysql+pymysql://neubility:neubility@monitoring-database-dev.cfpdcop7a57p.ap-northeast-2.rds.amazonaws.com:3306"
)

Base.metadata.bind = engine


class Store(Base):
    __tablename__ = "store"
    __table_args__ = {"schema": "connection_test1", "extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)


class Item(Base):
    __tablename__ = "item"
    __table_args__ = {"schema": "connection_test2", "extend_existing": True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    store_id = Column(
        Integer,
        ForeignKey(
            "connection_test1.store.id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
    )
    store = relationship("Store", foreign_keys=[store_id])


Base.metadata.drop_all(engine, checkfirst=True)
Base.metadata.create_all(engine, checkfirst=True)

session = Session()

session.add(Store(id=1, name="카페"))
session.add(Store(id=2, name="편의점"))
session.add(Item(id=1, name="커피", store_id=1))

session.commit()

store = session.query(Store).first()

print("store = ", store.id, store.name)


item = session.query(Item).first()

print("item = ", item.id, item.name, "store = ", item.store.id, item.store.name)

session.close()
