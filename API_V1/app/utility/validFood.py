from app import api
import re

"""
    Class to validate data entered in food item
"""

class FoodDataValidator(object):
    def __init__ (self,title,description,price,food_type):
        self.title = title
        self.description = description
        self.price = price
        self.food_type = food_type

    def foodvalid(self):
        #check that title entered is a str
        if type(self.title) != str:
            api.abort(400, "Title entered :{} is not an string".format(self.title))

        #check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z]+$)",self.title):
            api.abort(400, "Title entered :{} is not a properly formatted string".format(self.title))
        
        #check that description entered is a str
        elif type(self.description) != str:
            api.abort(400, "Description entered :{} is not an string".format(self.description))

        # #check if the contents of description have characters between a-z and A-Z
        # elif not re.match(r"(^[a-zA-Z]+$)",self.description):
        #     api.abort(400, "Description entered :{} is not a properly formatted string".format(self.description))

        #check that price entered is a number
        elif type(self.price) != int:
            api.abort(400, "Price entered :{} is not an integer".format(self.price))

        #check that food type entered is a str
        elif type(self.food_type) != str:
            api.abort(400, "Type entered :{} is not an string".format(self.food_type))

        #check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z]+$)",self.food_type):
            api.abort(400, "Type entered :{} is not a properly formatted string".format(self.food_type))
        
        
        return True
        
        
        