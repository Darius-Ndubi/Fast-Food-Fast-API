"""Module to handle operations on Foods only"""

# local imports
from app import API
from app.api.v1.models.manOrders import food_items
from app.api.v1.models.authUsers import ManageUsersDAO
from app.api.utility.valid_food import FoodDataValidator
from app.api.utility.valid_order import OrderDataValidator

usersAO = ManageUsersDAO()
foodAO = OrderDataValidator()


class ManageFoodsDAO():
    """A class to handle food operations"""

    def __init__(self):
        # food item_id assigner
        self.food_id_counter = 2

    def check_foods_existance(self, heading):
        """Method to check existance of food item"""
        for food_item in food_items:
            if food_item.get('title') == heading:
                API.abort(
                    409, "food item creation for {} could not be completed due to existance of same item".format(heading))

            return True

    def food_data_validator(self, data_entered):
        """Method tho check food data entered by user"""
        data_validate = FoodDataValidator()
        title_check = data_validate.titleValidator(data_entered['title'])
        description_check = data_validate.descriptionValidator(
            data_entered['description'])
        price_check = data_validate.pricevalidator(data_entered['price'])
        type_check = data_validate.typeValidator(data_entered['type'])

        if title_check & description_check & price_check & type_check == True:
            return True
        return False

    def create_new_food_item(self, data):
        """
            Method to create a food item
        """
        data_check = self.food_data_validator(data)

        food_existance = self.check_foods_existance(data['title'])

        uname = usersAO.are_you_signed_in()

        usersAO.restraunt_actions()

        if data_check & food_existance == True:
            # if the check passes assign food id to item
            self.food_id_counter = self.food_id_counter + 1
            data['item_id'] = self.food_id_counter

            # let food item creator to be always fast food fast restraunt name
            data['creator'] = uname

            # add the new food item
            food_items.append(data)
            return data

        API.abort(500, "Un expected error occurred during data Validation")

    def get_all_foods(self):
        """
            Method to get all food items
        """
        # if number of food items is 0 tell user no food item exist else show the items
        if len(food_items) == 0:
            API.abort(404, "No foods created yet yet")

        # return the food items
        return food_items

    def get_specific_food(self, food_id):
        """Method to return a specific food item as searched ny its id"""
        # check if id entered is valid
        data_check = foodAO.orderIdValid(food_id)

        if data_check == True:
            # loop through the foods present and find food whose id matches the one entered
            for food in food_items:
                if food.get('item_id') == food_id:
                    # assign food to be returned to food
                    food = food
                    return food

                # if id ws not found report back to user
            API.abort(
                404, "Food: {} does not Exist, Please view the list of available foods then check again".format(food_id))

        API.abort(500, "Un expected error occurred during data Validation")

    def update_food_item(self, food_id, data):
        """Method to update food item data"""
        # check the data entered
        food_data = self.food_data_validator(data)
        uname = usersAO.are_you_signed_in()
        usersAO.restraunt_actions()
        food_existance = self.check_foods_existance(data['title'])

        # if both checks above are okay find the food item and update it
        if food_data and food_existance == True:
            # find the specific food_item
            f_item = self.get_specific_food(food_id)
            data['creator'] = uname
            f_item.update(data)

            return f_item

        API.abort(500, "Un expected error occurred during data Validation")

    def delete_food_item(self, food_id):
        """Method to delete a food item"""
        usersAO.restraunt_actions()

        to_remove = self.get_specific_food(food_id)

        # delete food item
        food_items.remove(to_remove)
