"""module to handle connections to the diffrent DBs"""

import os
import psycopg2


def connectdb():
    """function to set up connection to either of the dbs
    """
    connectdb = os.getenv('TDB_URL')
    # connectdb = os.getenv('DB_URL')
    try:
        return psycopg2.connect(connectdb)
    except:
        return ("Sorry connection to database failed")


def droptestdb():
    """Method to destroy the test database after testing
    """
    connection = connectdb()
    curs = connection.cursor()
    dropper = ["""DROP TABLE users""",
               """DROP TABLE foods""","""DROP TABLE orders"""]
    for table in dropper:
        curs.execute(table)

    curs.close()
    connection.commit()
    connection.close()
