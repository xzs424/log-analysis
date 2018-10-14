#!/usr/bin/env python3

from psycopg2.pool import ThreadedConnectionPool
from .patterns import Singleton


class ConnectionPool(ThreadedConnectionPool, metaclass=Singleton):

    def __init__(self):
        super().__init__(1, 10, "dbname=news")

    def get_connection(self):
        return super().getconn()

    def release_connection(self, connection):
        return super().putconn(connection)
