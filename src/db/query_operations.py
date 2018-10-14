from .connection_pool import ConnectionPool

conn_pool = ConnectionPool()


def fetchall(query, *query_args):

    connection = conn_pool.get_connection()

    cursor = connection.cursor()

    if (len(query_args) > 0):
        query = cursor.mogrify(query, query_args)

    cursor.execute(query)

    result = cursor.fetchall()

    conn_pool.release_connection(connection)

    return result
