"""Module to check what is entered as order details"""

import re
from werkzeug.exceptions import NotFound
from app.a_p_i.utility.messages import error_messages

# local imports
from app import api


class OrderDataValidator():
    """Class to validate data entered by user in the order
    """

    # def __init__(self,quantity,food_item):
    #     self.quantity = quantity
    #     self.food_item = food_item

    def validQuantity(self, quantity):
        """Method to validate order quantity entered
        """
        # check that quantity entered is a number
        if type(quantity) != int:
            api.abort(
                400, error_messages[21]["invalid_quantity"])
        return True

    def orderIdValid(self, user_order_id):
        """Method to validate the order ID entered by user if it is from 1 or more
        """
        if user_order_id == 0:
            api.abort(404, error_messages[22]["None_zero"])

        elif int(user_order_id) > 0:
            return True

        #api.abort(404, "Order id  :{} cannot be found, Orders are identified from 1 onwards".format(user_order_id))
        e = NotFound(error_messages[20]['item_not_found'])
        e.data = {'custom': 404}
        raise e

    def statusValid(self, order_status):
        """Method to handle the validity checking of status entered """
        # check if the order status is of string type
        if type(order_status) != str:
            api.abort(
                400, "Order status :{} is not an string".format(order_status))

        # check if the contents of order status have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z]+$)", order_status):
            api.abort(
                400, "Order status :{} is not well formatted ".format(order_status))

        return True
