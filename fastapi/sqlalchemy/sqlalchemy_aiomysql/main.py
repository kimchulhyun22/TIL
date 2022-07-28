from async_database import database
from session_context import get_session_id
from models import *
from asyncio import current_task
from uuid import uuid4
from session_context import set_session_context, reset_session_context
import asyncio


async def create_db():
    await database.create_database()


async def drop_db():
    await database.drop_database()


async def async_db_test():
    print(current_task())
    session_id = str(uuid4())

    context = set_session_context(session_id=session_id)

    await create_db()

    session = database.async_session

    await asyncio.gather(test1(session), test2(session))

    await asyncio.gather(test1(session), test2(session))

    await session.commit()
    await session.close()

    reset_session_context(context=context)

    # await drop_db()


async def test1(session):
    print("debug======================", get_session_id())
    session.add(Item(name="test1"))


async def test2(session):
    print("debug======================", get_session_id())
    session.add(Item(name="test2"))


if __name__ == "__main__":
    asyncio.run(async_db_test())
    asyncio.run(async_db_test())
