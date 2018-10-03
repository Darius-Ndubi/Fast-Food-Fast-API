"""Module to handle food items routes for admin"""
from flask import jsonify

# local imports
from app import api
from app.api.utility.validFood import FoodDataValidator
from app.api.utility.messages import success_messages, error_messages
from app.api.v2.db.conndb import connectdb

""" instance of validation class"""
foodvalidatorO = FoodDataValidator()


class ManageFoodDAO():

    """A class to handle food operations"""

    def __init__(self):
        self.admin_user = None

    def admin_only(self, user_id):
        """ Method the restrict route to admin only"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE user_id=%(user_id)s",
                     {'user_id': user_id})
        self.admin_user = curs.fetchone()
        curs.close()
        connection.close()
        if self.admin_user[3] is not True:
            api.abort(401, error_messages[19]['unmet_priv'])

        else:
            return self.admin_user

    def check_items_existance(self, title):
        """Method to check it the food item exists"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM foods WHERE title=%(title)s",
                     {'title': title})
        existance = curs.fetchone()
        curs.close()
        connection.close()
        return existance

    def create_menu_item(self, data):
        """method to create menu item"""
        title_check = foodvalidatorO.titleValidator(data['title'])
        desc_check = foodvalidatorO.descriptionValidator(data['description'])
        price_check = foodvalidatorO.pricevalidator(data['price'])
        type_check = foodvalidatorO.typeValidator(data['type'])
        title = data['title'].capitalize()
        food_exist = self.check_items_existance(title)

        # if all checks pass
        if title_check and desc_check and price_check and type_check:
            # check if title exists
            if food_exist is not None:
                api.abort(409, error_messages[18]['food_exist'])
            data['creator'] = self.admin_user[2]
            connection = connectdb()
            curs = connection.cursor()
            curs.execute("INSERT INTO foods (title,description,price,type," +
                         "creator) VALUES(%s,%s,%s,%s,%s)",
                         (title, data['description'], data['price'],
                          data['type'], data['creator']))

            curs.close()
            connection.commit()
            connection.close()
            created_food_item = {
                'Title': title,
                'Food Description': data['description'],
                'Food Price': data['price'],
                'Food Type': data['type']
            }
            return {success_messages[1]['food_created']: created_food_item}, 201
        api.abort(500, error_messages[1]['validation_error'])

    def get_all_foods(self):
        """Method to retrieve all food menu item"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM foods")
        menu = curs.fetchall()
        foods = []
        if len(menu) == 0:
            api.abort(404, error_messages[20]['item_not_found'])
        for item in menu:
            food_item = {
                'food_id': item[0],
                'title': item[1],
                'description': item[2],
                'price': item[3],
                'type': item[4]
            }
            foods.append(food_item)
        return (foods)
