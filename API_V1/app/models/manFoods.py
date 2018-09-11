from app import api
from app.models.manOrders import food_items
from app.utility.validFood import FoodDataValidator
from app.utility.validOrder import OrderDataValidator


"""
    A class to handle food operations
"""

class ManageFoodsDAO(object):

    def __init__ (self):
        #food item_id assigner
        self.food_id_counter = 0

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
                
            #if the check passes assign food id to item
            self.food_id_counter =self.food_id_counter +1
            data['item_id']= self.food_id_counter

            #let food item creator to be always fast food fast restraunt name
            data['creator'] = 'fast-food-fast'

            #add the new food item
            food_items.append(data)
            return food_items
        
        api.abort (500, "Un expected error occurred during data Validation")    
    

    """
        Method to get all food items
    """
    def get_all_foods(self):
        #if number of food items is 0 tell user no food item exist else show the items
        if len(food_items) == 0:
            api.abort(404, "No foods created yet yet")

        #return the food items
        return food_items


    """
        Method to retrieve specific food item
    """
    def get_specific_food(self,food_id):
        #check if id entered is valid
        data_check = OrderDataValidator.orderIdValid(food_id)
        
        if data_check == True :    
            #get all foods else error == none
            foods=self.get_all_foods()

            #loop through the foods present and find food whose id matches the one entered
            for food in foods:
                if food.get('item_id') == food_id:
                    #assign order to be returned to order
                    food=food
                    return food
            
                #if id ws not found report back to user
            api.abort (404, "Food: {} does not Exist, Please view the list of available foods then check again".format(food_id))

        api.abort (500, "Un expected error occurred during data Validation")