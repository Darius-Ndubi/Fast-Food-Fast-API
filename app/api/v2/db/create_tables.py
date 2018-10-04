"""Module to create the required tables in database"""

# local imports
from app.api.v2.db.conndb import connectdb


def create_dtb():
    """Function to create tablels into db"""
    tables = [
        """CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY NOT NULL,
        email VARCHAR NOT NULL,
        username VARCHAR(20) NOT NULL UNIQUE,
        priv BOOL DEFAULT FALSE,
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
        food_id TEXT [],
        title TEXT [],
        price TEXT [],
        quantity TEXT [],
        total INT NOT NULL,
        status VARCHAR NOT NULL,
        creator VARCHAR REFERENCES users(username)
        )
        """
    ]
    connection = connectdb()
    curs = connection.cursor()
    # food_id INT NOT NULL REFERENCES foods(food_id)

    for table in tables:
        curs.execute(table)

    curs.close()
    connection.commit()
    connection.close()
