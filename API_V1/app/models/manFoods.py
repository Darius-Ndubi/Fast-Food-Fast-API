from app import api
from app.models.manOrders import food_items
from app.utility.validFood import FoodDataValidator


"""
    A class to handle food operations
"""

class ManageFoodsDAO(object):

    # def __init__ (self):
    #     self.food_items=[]

    """
        Method to create a food item
    """
    def create_new_food_item(self,data):
        food_data = FoodDataValidator(data['title'],data['description'],data['price'],data['type'])
        data_check = food_data.foodvalid()
        
        if data_check == True:
            #check it the item exists
            for food_item in food_items:
                if food_item.get('title') == data['title']:
                    api.abort(409, "food item creation for {} could not be completed due to existance of same item".format(data['title']))
                
                #if the check passes

            data['item_id']= len(food_items) + 1

            data['creator'] = 'fastfoodfast'
            #add the new food item
            food_items.append(data)
            return food_items
        
        api.abort (500, "An expected error occurred during data Validation")    
    
