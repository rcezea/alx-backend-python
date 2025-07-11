#!/usr/bin/python3
"""
To use a generator to compute a memory-efficient
aggregate function i.e average age for a large dataset
"""

seed = __import__('seed')
connection = seed.connect_to_prodev()
cursor = connection.cursor(dictionary=True)

def stream_user_ages():
    """ Get user ages """
    query = 'SELECT age FROM user_data';
    cursor.execute(query)
    for row in cursor:
        yield row


def calculate_average():
    """ Compute the average age of users. """
    average = 0
    num = 0
    for num, row in enumerate(stream_user_ages(), start=1):
        average += row["age"]
    return average/num
