#!/usr/bin/python3

import asyncio
import aiosqlite


async def async_execute(query, params=()):
    async with aiosqlite.connect('alx.sqlite') as db:
        async with db.execute(query, params) as cursor:
            return await cursor.fetchall()


async def async_fetch_users():
    return await async_execute('SELECT * FROM users')


async def async_fetch_older_users():
    return await async_execute('SELECT * FROM users WHERE age > ?', (40,))


async def fetch_concurrently():
    users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    # print('All Users:')
    # for row in users:
    #     print(row)
    #
    # print('All Users older than 40:')
    # for row in older_users:
    #     print(row)

asyncio.run(fetch_concurrently())
