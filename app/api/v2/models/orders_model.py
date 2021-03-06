"""Module to run order operations"""

# local imports
from app import API
from app.api.utility.messages import success_messages, error_messages
from app.api.utility.valid_order import OrderDataValidator
from app.api.v2.db.conndb import connectdb
from app.api.v2.models.user_model import ManageUserDAO
from app.api.v2.models.food_model import ManageFoodDAO

ordervalidatorobject = OrderDataValidator()
foodobject = ManageFoodDAO()


class ManageOrdersDAO():
    """class to manage orders"""
    # default order status

    def __init__(self):
        self.status = 'NEW'

    def find_user_orders(self, uname):
        """Method to retrive orders created by a user"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute(
            "SELECT * FROM orders WHERE creator = %(creator)s",
            {'creator': uname})

        your_orders = curs.fetchall()
        curs.close()
        connection.close()
        u_orders = []
        for order in your_orders:
            order = {
                'order_id': order[0],
                'food_id': order[1],
                'title': order[2],
                'price': order[3],
                'quantity': order[4],
                'total': order[5],
                'status': order[6],
                'creator': order[7]
            }
            u_orders.append(order)
        return {success_messages[6]['user_order']: u_orders}

    def find_all_orders(self):
        """Method to retrieve all orders"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM orders")
        all_orders = curs.fetchall()
        curs.close()
        connection.close()
        user_orders = []
        for order in all_orders:
            order = {
                'order_id': order[0],'food_id': order[1],'title': order[2],'price': order[3],
                'quantity': order[4],'total': order[5],'status': order[6],'creator': order[7]
            }
            user_orders.append(order)
        return {success_messages[5]['user_orders']: user_orders}

    def find_specific_order(self, order_id):
        """Method to retrieve a specific order"""
        for order in self.find_all_orders().values():

            for order_dit in order:
                if order_dit['order_id'] == order_id:
                    return order_dit

            return API.abort(404, error_messages[20]['item_not_found'])

    def create_new_order(self, data):
        """Method that adds user order data to the db"""
        check_quantity = ordervalidatorobject.validQuantity(data['quantity'])
        check_food_id = ordervalidatorobject.orderIdValid(data['food_id'])
        food_id = data['food_id']
        order_price = []
        order_titles = []
        items_to_order = []

        ManageUserDAO.normal_user_only(data['username'])
        #check existance of food id  enterd
        for idee in food_id:
            existance = foodobject.check_food_existance_by_id(idee)
            if not existance:
                API.abort(404,{"Message":error_messages[22]['food_not_found']})

        # find the entered foods
        if check_food_id and check_quantity:
            connection = connectdb()
            curs = connection.cursor()
            for food_ids in data['food_id']:
                curs.execute(
                    "SELECT * FROM foods WHERE food_id = %(food_id)s",
                    {'food_id': food_ids})
                order_food = curs.fetchall()

                items_to_order += order_food

            for food in items_to_order:
                order_price.append(food[3])
                order_titles.append(food[1])

            to_find_price = list(zip(data['quantity'], order_price))

            total = 0
            for i in to_find_price:
                total = total + (i[0] * i[1])

            curs.execute("INSERT INTO orders (food_id,title,price,quantity," +
                            "total,status,creator) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (food_id, order_titles, order_price, data['quantity'],
                            total, self.status, data['username']))

            curs.close()
            connection.commit()
            connection.close()
            created_order = {
                'food id': data['food_id'],
                'ordered foods': order_titles,
                'price per food': order_price,
                'Quantity per food': data['quantity'],
                'Total expenditure': total,
                'Order Status': self.status,
                'Order Creator': data['username']
            }
            return created_order

        API.abort(500, error_messages[1]['validation_error'])

    def update_status(self, data, order_id):
        """Method to update th status of an order"""
        status = data['status'].capitalize()
        status_check = OrderDataValidator()
        status_checkO = status_check.statusValid(status)

        if status_checkO:
            connection = connectdb()
            curs = connection.cursor()
            curs.execute("UPDATE orders SET status = %(status)s" +
                        "WHERE order_id = %(order_id)s", {
                            'status': status, 'order_id': order_id})
            curs.close()
            connection.commit()
            connection.close()

            return{success_messages[4]['edit_success']:
                self.find_specific_order(order_id)}

        API.abort(500, error_messages[1]['validation_error'])
