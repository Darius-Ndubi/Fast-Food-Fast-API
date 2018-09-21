"""Module on operations done on order
    -> geting all orders
    -> creating and order
    -> getting a specific order
    -> adding order status
    -> deleting an order
"""

#local imports
from app import api
from app.a_p_i.utility.validOrder import OrderDataValidator


"""
    Food items that can be ordered
"""
food_items = [{'item_id':1, 'title':'Burger', 'description':'Sweeter than the Krubby Paddy', 'price':450, 'type':'snack'},
              {'item_id':2, 'title':'Fish', 'description':'Sweeter than the Krubby Paddy', 'price':400, 'type':'meal'}]



class ManageOrdersDAO(object):
    """A class to handle Orders
    """
    def __init__(self):
        self.id_counter = 0
        self.orders = []

    def find_all_orders(self):
        """ Method to find all orders
        Steps:
            -> check if there are any posted orders
            -> If orders have been posted it returns the orders
        """
        #check if there is any item in orders
        if len(self.orders) == 0:
            api.abort(404, "No orders yet, create soem then check them here")

        return self.orders

    def create_new_order(self, data):
        """Method to create and add a user order
        """
        #validate user order data
        orderDataO = OrderDataValidator(data['quantity'], data['food_item'])
        data_check = orderDataO.ordervalid()

        if data_check:
            #check that user has entered a quantity greater than 0
            if data['quantity'] <= 0:
                api.abort(400, "Sorry the minimum you can order is 1 you ordered {} ".format(data['quantity']))

            #find food item name in food item list
            for food_item in food_items:
                if food_item.get('title') == data['food_item']:
                    data['price'] = food_item['price']

                    #fing the number of orders and increment by 1
                    self.id_counter = self.id_counter +1
                    data['order_id'] = self.id_counter

                    #compute the total amount payable
                    data['total'] = data['price']*data['quantity']
                    self.orders.append(data)
                    return self.find_all_orders()

            api.abort(404, "Food Item {} does not Exist, Please order another one".format(data['food_item']))  

        api.abort(500, "An expected error occurred during data Validation")


    def get_specific_order(self, order_id):
        """Method to retrieve specific order as per its id
        """
        #check if id entered is valid
        data_check = OrderDataValidator.orderIdValid(order_id)
        if data_check:    
            #get all orders else error == none
            orders = self.find_all_orders()

            #loop through the orders present and find order whose id matches the one entered
            for order in orders:
                if order.get('order_id') == order_id:
                    #assign order to be returned to order
                    order = order
                    return order
            
                #if id ws not found report back to user
            api.abort(404, "Order: {} does not Exist, Please view the list of available orders then check again".format(order_id))

        api.abort(500, "An expected error occurred during data Validation")


    def update_order(self, order_id, data):
        """Method to edit order and give it a status
        """
        #check if status entered is well formated
        data_check = OrderDataValidator.statusValid(data['status'])
        
        if data_check:

            #locate the specific order
            order = self.get_specific_order(order_id)
            order.update(data)
            return order

        api.abort(500, "An expected error occurred during data Validation")


    def delete_order(self, order_id):
        """Method to delete a food order
        """
        to_delete = self.get_specific_order(order_id)

        #delete the order
        self.orders.remove(to_delete)
