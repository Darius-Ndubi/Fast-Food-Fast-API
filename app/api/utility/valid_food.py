"""Module to help in validating user data entered if it meets sites standards
"""

import re

# local imports
from app import API
from app.api.utility.messages import error_messages, success_messages


class FoodDataValidator(object):
    """Class to validate data entered in food item
    """

    def titleValidator(self, title):
        """Method to check data entered as food title"""
        if type(title) != str:
            API.abort(400, error_messages[11]['Int_title'])

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_]+$)", title) or title.isspace():
            API.abort(
                400, error_messages[12]['wrong_format_title'])

        return True

    def descriptionValidator(self, description):
        """Method to check what is entered as description"""
        if type(description) != str:
            API.abort(
                400, error_messages[13]['int_des'])

        # check if the contents of description have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", description) or description.isspace == True:
            API.abort(400, error_messages[14]['wrong_format_des'])

        return True

    def pricevalidator(self, price):
        """Method to check what is entered as price of food item"""
        if type(price) != int:
            API.abort(400, error_messages[15]['str_price'])

        return True

    def typeValidator(self, food_type):
        """Method to check what is entered as food type"""
        if type(food_type) != str:
            API.abort(400, error_messages[16]['int_type'])

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", food_type) or food_type.isspace():
            API.abort(
                400, error_messages[17]['wrong_format_ty'])

        return True
