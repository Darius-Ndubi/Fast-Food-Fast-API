"""Module to handle food items routes for admin"""
from flask import jsonify

# local imports
from app import API
from app.api.utility.valid_food import FoodDataValidator
from app.api.utility.messages import success_messages, error_messages
from app.api.v2.db.conndb import connectdb

""" instance of validation class"""
foodvalidatorobject = FoodDataValidator()


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
            API.abort(403, error_messages[19]['unmet_priv'])

        else:
            return self.admin_user

    def check_food_existance_by_id(self,food_id):
        """Method to checkif a food item exists if queried by its id"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM foods WHERE food_id=%(food_id)s",
                     {'food_id': food_id})
        existance = curs.fetchone()
        return existance

    def check_items_existance(self, title):
        """Method to validation it the food item exists"""
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
        title_validation = foodvalidatorobject.titleValidator(data['title'])
        description_validation = foodvalidatorobject.descriptionValidator(
            data['description'])
        price_validation = foodvalidatorobject.pricevalidator(data['price'])
        type_validation = foodvalidatorobject.typeValidator(data['type'])
        title = data['title'].cAPItalize()
        food_exist = self.check_items_existance(title)

        # if all validations pass
        if title_validation and description_validation and price_validation and type_validation:
            # validation if title exists
            if food_exist is not None:
                API.abort(409, error_messages[18]['food_exist'])
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
            return {"Message":success_messages[1]['food_created'],"Food Item":created_food_item}, 201
        API.abort(500, error_messages[1]['validation_error'])

    def get_all_foods(self):
        """Method to retrieve all food menu item"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM foods")
        menu = curs.fetchall()
        foods = []
        if len(menu) == 0:
            API.abort(404, error_messages[20]['item_not_found'])
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
