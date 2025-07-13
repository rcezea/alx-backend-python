import time
from sqlite3 import Error
import functools

#### paste your with_db_decorator here

with_db_connection = __import__('1-with_db_connection').with_db_connection

def retry_on_failure(_func=None, retries=3, delay=1):
    def decorator_retry_on_failure(func):
        @functools.wraps(func)
        def wrapper_retry_on_failure(*args, **kwargs):
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Error:
                    if attempt == retries:
                        raise
                    # print('retrying in 1s') #It works!
                    time.sleep(delay)
        return wrapper_retry_on_failure
    if _func is None:
        return decorator_retry_on_failure
    else:
        return decorator_retry_on_failure(_func)


@with_db_connection
@retry_on_failure()
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
