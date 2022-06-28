import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class Database:
    def __init__(self) -> None:
        self._engine = None
        self._seesion = None

        self._user_name = os.getenv("USER_NAME")
        self._password = os.getenv("PASSWORD")
        self._host = os.getenv("HOST")
        self._port = os.getenv("PORT")
        self._db_name = os.getenv("DB_NAME")
        self._rds_pool_recycle = os.getenv("RDS_POOL_RECYCLE", 900)
        self._rds_echo = os.getenv("RDS_ECHO", False)

        self._create_engine()

    def _create_engine(self):
        url = f"mysql+pymysql://{self._user_name}:{self._password}@{self._host}:{self._port}/{self._db_name}"

        self._engine = create_engine(
            url,
            echo=self._rds_echo,
            pool_recycle=self._rds_pool_recycle,
            pool_pre_ping=self._rds_echo,
        )

        self._session = sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine
        )

    @property
    def session(self):
        return self._session()

    def execute_query(self, query: str):
        result = None

        with self._engine.connect() as conn:
            result = conn.execute(query)

        return result


database = Database()
