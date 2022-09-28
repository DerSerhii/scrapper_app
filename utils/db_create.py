""" DATABASE CREATION UTILITY"""

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = None
try:
    # Connecting to an existing database
    connection = psycopg2.connect(user="postgres",
                                  # the password that was specified
                                  # when installing PostgreSQL
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Cursor to perform database operations
    cursor = connection.cursor()
    sql_create_database = 'CREATE DATABASE KIJIJI'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("ERROR: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed")
