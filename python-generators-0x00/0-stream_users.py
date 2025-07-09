#!/usr/bin/python3

def stream_users():
    """ generator that streams rows from an SQL database one by one """
    seed = __import__('seed')

    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM user_data')

    for row in cursor:
        yield row
