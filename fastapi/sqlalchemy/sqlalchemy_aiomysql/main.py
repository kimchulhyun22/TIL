from async_database import database
from models import *

import asyncio


async def test():
    await database.create_database()

    async with database.async_session() as session:

        session.add(Item(name="test"))

        await session.commit()

    await database.drop_database()


if __name__ == "__main__":
    asyncio.run(test())
