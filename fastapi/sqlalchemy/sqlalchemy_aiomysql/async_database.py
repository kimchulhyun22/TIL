from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker
from asyncio import current_task
from session_context import get_session_id

Base = declarative_base()

DATABASE_URL = "mysql+aiomysql://root:sdfsdfsdf@localhost:3306/test_db"


class AsyncDatabase:
    def __init__(self) -> None:
        self._engine = create_async_engine(DATABASE_URL, echo=True)

        self._async_session_factory = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )

        self._async_session = async_scoped_session(
            session_factory=self._async_session_factory,
            scopefunc=get_session_id,
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
