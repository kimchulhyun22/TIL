import asyncio
import unittest
import aiounittest
from uuid import uuid4
from session_context import set_session_context, get_session_id, reset_session_context
from async_database import database
from models import *
from aiounittest import async_test


class AsyncTest(unittest.TestCase):
    def setUp(self) -> None:
        self.session_id = str(uuid4())

        self.context = set_session_context(session_id=self.session_id)

    @async_test
    async def test_create_item(self):

        session = database.get_async_session()

        print("a============================== ", session)
        await asyncio.gather(self.insert_1(session), self.insert_2(session))

        await session.commit()
        await session.remove()
        await session.close()

    @async_test
    async def test_create_item2(self):

        session = database.get_async_session()

        print("a============================== ", session)
        await asyncio.gather(self.insert_1(session), self.insert_2(session))

        await session.commit()
        await session.remove()
        await session.close()

    async def insert_1(self, session):
        print("debug======================", get_session_id())
        session.add(Item(name="test1"))

    async def insert_2(self, session):
        print("debug======================", get_session_id())
        session.add(Item(name="test2"))

    def tearDown(self) -> None:
        reset_session_context(context=self.context)
