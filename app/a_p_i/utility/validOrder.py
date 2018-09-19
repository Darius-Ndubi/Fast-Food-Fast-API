import re
from werkzeug.exceptions import NotFound

#local imports
from app import api

"""
    class to validate data entered by user in the order
"""

class OrderDataValidator(object):

    def __init__(self,quantity,food_item):
        self.quantity = quantity
        self.food_item = food_item

    def ordervalid(self):
        #check that quantity entered is a number
        if type(self.quantity) != int:
            api.abort(400, "Quantity entered :{} is not an integer".format(self.quantity))
        
        #check if the food item is of string type
        elif  type(self.food_item) != str:
            api.abort(400, "Food Item entered :{} is not an string".format(self.food_item))
    
        #check if the contents of food_item have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z]+$)",self.food_item):
            api.abort(400, "Food Item entered :{} is not an string".format(self.food_item))
        
        return True
     
    """
        Method to validate the order ID entered by user if it is from 1 or more
    """
    @staticmethod
    def orderIdValid(user_order_id):
        if user_order_id == 0:
            api.abort(404, "Order id  :{} cannot be found, Orders are identified from 1 onwards".format(user_order_id))
        
        elif user_order_id > 0:
            return True
        
        #api.abort(404, "Order id  :{} cannot be found, Orders are identified from 1 onwards".format(user_order_id))
        e=NotFound("Seached Fast Food order not found")
        e.data={'custom':404}
        raise e
    
    """
        Method to handle the validity checking of status entered 
    """
    @staticmethod
    def statusValid(order_status):

        #check if the order status is of string type
        if  type(order_status) != str:
            api.abort(400, "Order status :{} is not an string".format(order_status))
    
        #check if the contents of order status have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z]+$)",order_status):
            api.abort(400, "Order status :{} is not well formatted ".format(order_status))

        return True
        