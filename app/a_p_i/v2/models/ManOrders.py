"""Module to run order operations"""

# local imports
from app import api
from app.a_p_i.utility.messages import success_messages, error_messages
from app.a_p_i.utility.validOrder import OrderDataValidator
from app.a_p_i.v2.db.connDB import connDb

orderdataValidatorO = OrderDataValidator()


class ManageOrdersDAO():
    # default order status
    def __init__(self):
        self.status = 'NEW'

    def find_user_orders(self, uname):
        """Method to retrive orders created by a user"""
        connection = connDb()
        curs = connection.cursor()
        curs.execute(
            "SELECT * FROM orders WHERE creator = %(creator)s", {'creator': uname})
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
        return u_orders

    def find_all_orders(self):
        """Method to retrieve all orders"""
        connection = connDb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM orders")
        all_orders = curs.fetchall()
        curs.close()
        connection.close()
        user_orders = []
        for order in all_orders:
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
            user_orders.append(order)
        return user_orders

    def create_new_order(self, data):
        """Method that adds user order data to the db"""
        check_quantity = orderdataValidatorO.validQuantity(data['quantity'])
        check_food_id = orderdataValidatorO.orderIdValid(data['food_id'])
        food_id = data['food_id']

        if check_quantity and check_food_id:
            # find the food item
            connection = connDb()
            curs = connection.cursor()

            curs.execute("SELECT * FROM orders WHERE food_id = %(food_id)s AND status = %(status)s ANd creator = %(creator)s", {
                'food_id': food_id, 'status': self.status, 'creator': data['username']})

            existing = curs.fetchall()

            if existing:
                api.abort(403, success_messages[3]["order_created1"])
            curs.close()
            connection.close()

            connection = connDb()
            curs = connection.cursor()
            curs.execute("SELECT * FROM foods WHERE food_id = %(food_id)s", {
                'food_id': food_id})
            order_food = curs.fetchone()

            total = data['quantity'] * order_food[3]
            quant = data['quantity']
            uname = data['username']
            title = order_food[1]
            price = order_food[3]

            curs.execute("INSERT INTO orders (food_id,title,price,quantity,total,status,creator) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                         [food_id, title, price, quant, total, self.status, uname],)
            curs.close()
            connection.commit()
            connection.close()
            return success_messages[2]['order_created']
        api.abort(500, error_messages[1]['validation_error'])
