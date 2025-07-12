#!/usr/bin/python3

import sqlite3
import functools

#### decorator to log SQL queries


def log_queries(f):
    """ log the SQL query before executing it. """
    functools.wraps(f)
    def wrapper_log_queries(*args, **kwargs):
        print(kwargs)
        return f(*args, **kwargs)
    return wrapper_log_queries


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
