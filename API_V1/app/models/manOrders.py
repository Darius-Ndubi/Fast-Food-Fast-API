from app import api
from app.utility.validOrder import OrderDataValidator


"""
    Food items that can be ordered
"""
food_items=[{'item_id':1,'title':'Burger','description':'Sweeter than the Krubby Paddy','price':450,'type':'snack'},
            {'item_id':2,'title':'Fish','description':'Sweeter than the Krubby Paddy','price':400,'type':'meal'}]

"""
    Examples of orders created
"""
# orders=[{'order_id':1,'food_item':'Burger','price':450,'quantity':2,'total':900},
#         {'order_id':2,'food_item':'Pizza','price':600,'quantity':3,'total':1800}]


"""
    A class to handle Orders
"""
class ManageOrdersDAO(object):

    def __init__(self):
        self.id_counter = 0
        self.orders=[]
    """ 
        Method to find all orders
        Steps:
            -> check if there are any posted orders
            -> If orders have been posted it returns the orders
    """
    
    def find_all_orders (self):
        #check if there is any item in orders
        if len(self.orders)==0:
            api.abort(404, "No orders yet")
        
        return self.orders

    """
        Method to create and add a user order
    """
    def create_new_order(self,data):
        #validate user order data
        orderDataO = OrderDataValidator(data['quantity'],data['food_item'])
        data_check= orderDataO.ordervalid()

        if data_check == True:
            #check that user has entered a quantity greater than 0
            if data['quantity'] <= 0:
                api.abort (400, "Sorry the minimum you can order is 1 you ordered {} ".format(data['quantity']))


            #find food item name in food item list
            for food_item in food_items:
                if food_item.get('title')== data['food_item']:
                    data['price']=food_item['price']

                    #fing the number of orders and increment by 1
                    data['order_id']=len(self.orders) + 1



                    #compute the total amount payable
                    data['total']=data['price']*data['quantity']

                    self.orders.append(data)

                    return self.find_all_orders ()
                
            api.abort (404, "Food Item {} does not Exist, Please order another one".format(data['food_item']))  

        api.abort (500, "An expected error occurred during data Validation")


    """
        Method to retrieve specific order as per its id
    """

    def get_specific_order(self,order_id):

        #check if id entered is valid
        data_check = OrderDataValidator.orderIdValid(order_id)
        
        if data_check == True :    
            #get all orders else error == none
            orders=self.find_all_orders()

            #loop through the orders present and find order whose id matches the one entered
            for order in orders:
                if order.get('order_id') == order_id:
                    #assign order to be returned to order
                    order=order
                    return order
            
                #if id ws not found report back to user
            api.abort (404, "Order: {} does not Exist, Please view the list of available orders then check again".format(order_id))

        api.abort (500, "An expected error occurred during data Validation")



    """
        Method to edit order and give it a status
    """
    def update_order(self,order_id,data):
        #check if id entered is valid
        data_check = OrderDataValidator.orderIdValid(order_id)
        
        #check if status entered is well formated
        data_check2 = OrderDataValidator.statusValid(data['status'])
        
        if data_check and data_check2 == True:

            #locate the specific order
            order=self.get_specific_order(order_id)
            order.update(data)
            return order

        api.abort (500, "An expected error occurred during data Validation")

