#!/usr/bin/python3

def stream_users():
    """ generator that streams rows from an SQL database one by one """
    seed = __import__('seed')

    connection = seed.connect_to_prodev()

    cursor = connection.cursor()

    query = 'SELECT * FROM user_data'

    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        yield row
