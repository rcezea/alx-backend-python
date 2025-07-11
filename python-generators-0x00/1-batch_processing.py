#!/usr/bin/python3

seed = __import__('seed')

connection = seed.connect_to_prodev()

cursor = connection.cursor(dictionary=True)

def stream_users_in_batches(batch_size):
    offset = 0
    while True:
        query = 'SELECT * FROM user_data LIMIT {} OFFSET {}'.format(batch_size, offset)
        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            break

        yield records

        offset += batch_size

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if row['age'] > 25:
                yield row

