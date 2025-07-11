#!/usr/bin/python3

seed = __import__('seed')


def paginate_users(page_size, offset=0):
    """ fetch user data """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """ Lazy loading Paginated Data """
    offset = 0
    while True:
        _ = yield paginate_users(page_size, offset)
        if _ is None:
            break
        offset += page_size
