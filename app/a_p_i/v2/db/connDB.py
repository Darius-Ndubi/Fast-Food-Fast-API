"""module to handle connections to the diffrent DBs"""

import os
import psycopg2


def connDb():
    """function to set up connection to either of the dbs
    """
    connectdb = os.getenv('TDB_URL', 'postgresql:///testfastfoodfast')
    # connectdb = os.getenv('DB_URL')
    try:
        return psycopg2.connect(connectdb)
    except:
        print("Sorry connection to database failed")


def dropTdb():
    """Method to destroy the test database after testing
    """
    connection = connDb()
    curs = connection.cursor()
    dropper = ["""DROP TABLE users""",
               """DROP TABLE orders""", """DROP TABLE foods"""]
    for table in dropper:
        curs.execute(table)

    curs.close()
    connection.commit()
    connection.close()
