"""Module to check what is entered as order details"""

import re
from werkzeug.exceptions import NotFound


# local imports
from app import API
from app.api.utility.messages import error_messages


class OrderDataValidator():
    """Class to validate data entered by user in the order
    """

    def validQuantity(self, quantity):
        """Method to validate order quantity entered
        """
        # check that quantity entered is a number
        if type(quantity) != list:
            API.abort(
                400, error_messages[21]["invalid_quantity"])
        return True

    def orderIdValid(self, user_order_id):
        if type(user_order_id) != list:
            API.abort(404, error_messages[22]["None_zero"])
        return True

    def statusValid(self, order_status):
        """Method to handle the validity checking of status entered """
        # check if the order status is of string type
        if type(order_status) != str:
            API.abort(
                400, error_messages[23]["invalid_status"])

        if not re.match(r"(^[a-zA-Z]+$)", order_status):
            API.abort(
                400, error_messages[24]["incorect_status"])
        elif str(order_status) == 'Processing' or str(order_status) == 'Cancelled' or str(order_status) == 'Complete':
            return True
        API.abort(
            400, error_messages[24]["incorect_status"])
