#!/usr/bin/python3

from sqlite3 import connect, Error
import functools

def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper_db_connection(*args, **kwargs):
        # Open Database Connection
        conn = None
        try:
            conn = connect('users.db')
            return func(conn, *args, **kwargs)
        except Error as e:
            raise Exception(f"Database Connection Failed - {e}")
        finally:
            # Close Database Connection
            if conn is not None:
                conn.close()
    return wrapper_db_connection
if __name__ == "__main__":
    @with_db_connection
    def get_user_by_id(conn, user_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    #### Fetch user by ID with automatic connection handling

    user = get_user_by_id(user_id=1)
    print(user)
