from app import api
import re

"""
    Class to validate data entered in food item
"""

class FoodDataValidator(object):
    # def __init__ (self,title,description,price,food_type):
    #     self.title = title
    #     self.description = description
    #     self.price = price
    #     self.food_type = food_type

         
    def titleValidator(self,title):
        #check that title entered is a str
        if type(title) != str:
            api.abort(400, "Title entered :{} is not an string".format(title))

        #check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)",title) or title.isspace() == True:
            api.abort(400, "Title entered :{} is not a properly formatted string".format(title))
        
        return True

    def descriptionValidator(self,description):
        #check that description entered is a str
        if type(description) != str:
            api.abort(400, "Description entered :{} is not an string".format(description))

        #check if the contents of description have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)",description) or description.isspace == True:
            api.abort(400, "Description entered :{} is not a properly formatted string".format(description))

        return True
    
    def pricevalidator(self,price):
        #check that price entered is a number
        if type(price) != int:
            api.abort(400, "Price entered :{} is not an integer".format(price))

        return True

    def typeValidator(self,food_type):
        #check that food type entered is a str
        if type(food_type) != str:
            api.abort(400, "Type entered :{} is not an string".format(food_type))

        #check if the contents of title have characters between a-z and A-Z
        elif not re.match(r"(^[a-zA-Z_ ]+$)",food_type) or food_type.isspace() == True:
            api.abort(400, "Type entered :{} is not a properly formatted string".format(food_type))
        
        return True


        
        