from app import api
import re
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