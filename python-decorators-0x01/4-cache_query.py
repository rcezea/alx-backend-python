import inspect
import functools

with_db_connection = __import__('1-with_db_connection').with_db_connection

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper_cache_query(*args, **kwargs):
        # 1. binding the full function call signature
        ## Remove conn from the parameters
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        key_items = [
            (k, v) for k, v in bound.arguments.items()
            if k != 'conn'
        ]
        key = tuple(sorted(key_items))

        #   2. Assume connection object is first in args and exclude it
        ##  key_args = args[1:]
        ### key = key_args + tuple(sorted(kwargs.items()))

        return query_cache.setdefault(key, func(*args, **kwargs))
    return wrapper_cache_query

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
