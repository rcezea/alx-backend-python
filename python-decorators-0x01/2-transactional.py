#!/usr/bin/python3

from sqlite3 import connect, Error, DatabaseError
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_db_connection(*args, **kwargs):
        # Open Database Connection
        conn = None
        try:
            conn = connect('alx.sqlite')
            return func(conn, *args, **kwargs)
        except Error as e:
            raise Exception(f"Database Connection Failed - {e}")
        finally:
            # Close Database Connection
            if conn is not None:
                conn.close()
    return wrapper_db_connection

def transactional(func):
    @functools.wraps(func)
    def wrapper_transactional(*args, **kwargs):
        conn = args[0]
        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except DatabaseError as e:
            conn.rollback()
            raise Exception(f'Database Error: {e}') from e

    return wrapper_transactional

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    #### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
