"""Module to handle food items routes for admin"""

# local imports
from app import api
from app.a_p_i.utility.validFood import FoodDataValidator
from app.a_p_i.utility.messages import success_messages, error_messages
from app.a_p_i.v2.db.connDB import connDb

""" instance of validation class"""
foodvalidatorO = FoodDataValidator()


class ManageFoodDAO():

    """A class to handle food operations"""

    def __init__(self):
        self.admin_user = None

    def admin_only(self, user_id):
        """ Method the restrict route to admin only"""
        connection = connDb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE user_id=%(user_id)s",
                     {'user_id': user_id})
        self.admin_user = curs.fetchone()
        curs.close()
        connection.close()
        if self.admin_user[3] != True:
            api.abort(401, error_messages[19]['unmet_priv'])

        else:
            return self.admin_user

    def check_items_existance(self, title):
        """Method to check it the food item exists"""
        connection = connDb()
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
        food_exist = self.check_items_existance(data['title'])

        # if all checks pass
        if title_check and desc_check and price_check and type_check:
            # check if title exists
            if food_exist != None:
                api.abort(409, error_messages[18]['food_exist'])
            data['creator'] = self.admin_user[2]
            connection = connDb()
            curs = connection.cursor()
            curs.execute("INSERT INTO foods (title,description,price,type,creator) VALUES(%s,%s,%s,%s,%s)",
                         (data['title'], data['description'], data['price'], data['type'], data['creator']))
            curs.close()
            connection.commit()
            connection.close()
            return success_messages[1]['food_created'], 201
        api.abort(500, error_messages[1]['validation_error'])

    def get_all_foods(self):
        """Method to retrieve all food menu item"""
        connection = connDb()
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
