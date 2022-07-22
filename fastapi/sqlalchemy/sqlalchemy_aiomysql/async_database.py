from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "mysql+aiomysql://root:sdfsdfsdf@localhost:3306/test_db"


class AsyncDatabase:
    def __init__(self) -> None:
        self._engine = create_async_engine(DATABASE_URL, echo=True)

        self._async_session = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_database(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_database(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    @property
    def async_session(self):
        return self._async_session


database = AsyncDatabase()
