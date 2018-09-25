"""Module to handle operations on order endpoints only"""

# local imports
from app import api
from app.a_p_i.utility.validOrder import OrderDataValidator
from app.a_p_i.v1.models.authUsers import ManageUsersDAO

# instance onf class MAnageUSersDAO,OrderDataValidator
usersAO = ManageUsersDAO()
orderIdO = OrderDataValidator()

"""
    Food items that can be ordered
"""
food_items = [{'item_id': 1, 'title': 'Burger', 'description': 'Sweeter than the Krubby Paddy', 'price': 450, 'type': 'snack'},
              {'item_id': 2, 'title': 'Fish', 'description': 'Sweeter than the Krubby Paddy', 'price': 400, 'type': 'meal'}]

"""
    Examples of orders created
"""
# orders=[{'order_id':1,'food_item':'Burger','price':450,'quantity':2,'total':900},
#         {'order_id':2,'food_item':'Pizza','price':600,'quantity':3,'total':1800}]


class ManageOrdersDAO():
    """A class to handle Orders"""

    def __init__(self):
        self.id_counter = 0
        self.orders = []

    def find_all_orders(self):
        """ Method to find all orders
        Steps:
            -> check if there are any posted orders
            -> If orders have been posted it returns the orders
        """
        if len(self.orders) == 0:
            api.abort(404, "No orders yet")

        return self.orders

    def order_data_validator(self, order_data):
        """Method to validate user order data"""
        orderdataO = OrderDataValidator()
        check_food_id = orderdataO.orderIdValid(order_data['food_id'])
        check_quantity = orderdataO.validQuantity(order_data['quantity'])

        if check_quantity and check_food_id == True:
            return True
        return False

    def order_id_validator(self, order_id):
        """Method to check validity of id entered"""
        check_id = orderIdO.orderIdValid(order_id)

        if check_id == True:
            return True
        return False

    def create_new_order(self, data):
        """Method to create and add a user order"""
        uname = usersAO.are_you_signed_in()
        data_check = self.order_data_validator(data)

        if data_check:
            # check that user has entered a quantity greater than 0
            if data['quantity'] <= 0:
                api.abort(400, "Sorry the minimum you can order is 1 you ordered {} ".format(
                    data['quantity']))

            # find food item name in food item list
            for food_item in food_items:
                if food_item.get('item_id') == data['food_id']:
                    data['price'] = food_item['price']

                    # fing the number of orders and increment by 1
                    self.id_counter = self.id_counter + 1
                    data['order_id'] = self.id_counter
                    data['food_item'] = food_item['title']

                    data['creator'] = uname
                    data['status'] = 'Pending'

                    # compute the total amount payable
                    data['total'] = data['price']*data['quantity']
                    self.orders.append(data)
                    return data

            api.abort(404, "Food Item {} does not Exist, Please order another one".format(
                data['food_id']))

        api.abort(500, "An expected error occurred during data Validation")

    def get_specific_order(self, order_id):
        """Method to retrieve specific order as per its id"""
        # check if id entered is valid
        data_check = self.order_id_validator(order_id)

        if data_check == True:
            # loop through the orders present and find order whose id matches the one entered
            for order in self.orders:
                if order.get('order_id') == order_id:
                    # assign order to be returned to order
                    order = order
                    return order

                # if id ws not found report back to user
            api.abort(
                404, "Order: {} does not Exist, Please view the list of available orders then check again".format(order_id))

        api.abort(500, "An expected error occurred during data Validation")

    def update_order(self, order_id, data):
        """Method to edit order and give it a status"""
        # check if status entered is well formated
        status_check = OrderDataValidator()
        usersAO.are_you_signed_in()
        usersAO.restraunt_actions()
        data_check = status_check.statusValid(data['status'])

        if data_check == True:

            # locate the specific order
            order = self.get_specific_order(order_id)
            order.update(data)
            return order

        api.abort(500, "An expected error occurred during data Validation")

    def delete_order(self, order_id):
        """Method to delete a food order"""

        to_delete = self.get_specific_order(order_id)

        # delete the order
        self.orders.remove(to_delete)
