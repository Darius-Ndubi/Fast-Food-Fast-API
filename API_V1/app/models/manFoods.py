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
        self.food_id_counter = 2

    def create_new_food_item(self,data):
        """
            Method to create a food item
        """
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
    

    def get_all_foods(self):
        """
            Method to get all food items
        """
        #if number of food items is 0 tell user no food item exist else show the items
        if len(food_items) == 0:
            api.abort(404, "No foods created yet yet")

        #return the food items
        return food_items


    def get_specific_food(self,food_id):
        """
            Method to retrieve specific food item
        """
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



    def update_food_item(self,food_id,data):
        """
            Method to update food item data
        """
        #check the data entered
        data_check1 = OrderDataValidator.orderIdValid(food_id)
        food_data = FoodDataValidator(data['title'],data['description'],data['price'],data['type'])
        data_check2 = food_data.foodvalid() 

        #if both checks above are okay find the food item and update it
        if  data_check1 and data_check2 == True:
            #check it the item with name entered already exists
            for food_item in food_items:
                if food_item.get('title') == data['title']:
                    api.abort(409, "food item creation for {} could not be completed due to existance of same item".format(data['title']))
        
            #find the specific food_item
            f_item=self.get_specific_food(food_id)
            data['creator'] = 'fast-food-fast'
            f_item.update(data)

            return f_item
        
        api.abort (500, "An expected error occurred during data Validation")


    def delete_food_item(self,food_id):
        """
            Method to delete a food item
        """
        to_remove=self.get_specific_food(food_id)

        #delete food item
        food_items.remove(to_remove)

