"""Module to help in validating user data entered if it meets sites standards
"""

import re

# local imports
from app import api


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
            api.abort(400, "Title entered :{} is not a string".format(title))

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", title) or title.isspace() == True:
            api.abort(
                400, "Title entered :{} is not a properly formatted string".format(title))

        return True

    def descriptionValidator(self, description):
        """Method to check what is entered as description"""
        if type(description) != str:
            api.abort(
                400, "Description entered :{} is not an string".format(description))

        # check if the contents of description have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", description) or description.isspace == True:
            api.abort(400, "Description entered :{} is not a properly formatted string".format(
                description))

        return True

    def pricevalidator(self, price):
        """Method to check what is entered as price of food item"""
        if type(price) != int:
            api.abort(400, "Price entered :{} is not an integer".format(price))

        return True

    def typeValidator(self, food_type):
        """Method to check what is entered as food type"""
        if type(food_type) != str:
            api.abort(400, "Type entered :{} is not an string".format(food_type))

        # check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)", food_type) or food_type.isspace() == True:
            api.abort(
                400, "Type entered :{} is not a properly formatted string".format(food_type))

        return True
