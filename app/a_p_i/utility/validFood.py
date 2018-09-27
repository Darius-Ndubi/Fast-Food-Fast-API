"""Module to help in validating user data entered if it meets sites standards
"""

import re

# local imports
from app import api
from app.a_p_i.utility.messages import error_messages, success_messages


class FoodDataValidator(object):
    """Class to validate data entered in food item
    """
    # def __init__ (self,title,description,price,food_type):
    #     self.title = title
    #     self.description = description
    #     self.price = price
    #     self.food_type = food_type

    def titleValidator(self, title):
        """Method to check data entered as food title"""
        if type(title) != str:
            api.abort(400, error_messages[11]['Int_title'])

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", title) or title.isspace() == True:
            api.abort(
                400, error_messages[12]['wrong_format_title'])

        return True

    def descriptionValidator(self, description):
        """Method to check what is entered as description"""
        if type(description) != str:
            api.abort(
                400, error_messages[13]['int_des'])

        # check if the contents of description have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", description) or description.isspace == True:
            api.abort(400, error_messages[14]['wrong_format_des'])

        return True

    def pricevalidator(self, price):
        """Method to check what is entered as price of food item"""
        if type(price) != int:
            api.abort(400, error_messages[15]['str_price'])

        return True

    def typeValidator(self, food_type):
        """Method to check what is entered as food type"""
        if type(food_type) != str:
            api.abort(400, error_messages[16]['int_type'])

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", food_type) or food_type.isspace() == True:
            api.abort(
                400, error_messages[17]['wrong_format_ty'])

        return True
