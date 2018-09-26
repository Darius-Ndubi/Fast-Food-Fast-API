"""Module to create the required tables in database"""

# local imports
from app.a_p_i.v2.db.connDB import connDb


def create_dtb():
    tables = [
        """ 
        CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY NOT NULL,
        email VARCHAR NOT NULL,
        username VARCHAR(10) NOT NULL,
        password VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS foods(
        food_id SERIAL PRIMARY KEY NOT NULL,
        title VARCHAR(20) NOT NULL,
        description VARCHAR NOT NULL,
        price INT NOT NULL,
        type VARCHAR NOT NULL,
        creator VARCHAR(20) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders(
        order_id SERIAL PRIMARY KEY NOT NULL,
        food_id INT NOT NULL REFERENCES foods(food_id),
        title VARCHAR(20) NOT NULL,
        price INT NOT NULL,
        quantity INT NOT NULL,
        total INT NOT NULL,
        status VARCHAR NOT NULL,
        creator VARCHAR(20) NOT NULL
        )
        """
    ]
    connection = connDb()
    curs = connection.cursor()

    for table in tables:
        curs.execute(table)

    curs.close()
    connection.commit()
    connection.close()
