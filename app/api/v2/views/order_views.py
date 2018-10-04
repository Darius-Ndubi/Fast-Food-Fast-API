"""Module on user order endpoint"""
from flask_restplus import Resource, Namespace, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app import API
from app.api.v2.models.orders_model import ManageOrdersDAO
from app.api.v2.models.user_model import ManageUserDAO
from app.api.v2.models.food_model import ManageFoodDAO
from app.api.utility.messages import error_messages
from app.api.v1.views.order_views import order,status

fastfood = Namespace('orders', description='Orders and their operations')

orderobject = ManageOrdersDAO()
foodobject = ManageFoodDAO()



"""User orders endpoint
"""


@fastfood.route('/users/orders')
class Order(Resource):
    """
        Class to get all orders and add an order
    """
    @jwt_required
    def get(self):
        """Geting all posted by an individual"""
        user_id = get_jwt_identity()
        return orderobject.find_user_orders(
            ManageUserDAO.get_username(user_id)), 200

    @jwt_required
    def post(self):
        """Post an order"""
        user_id = get_jwt_identity()
        try:
            new_order = {
                'food_id': request.json['food_id'],
                'quantity': request.json['quantity']
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])

        new_order['username'] = ManageUserDAO.get_username(user_id)

        return orderobject.create_new_order(new_order), 201


@fastfood.route('/orders/')
class OrderList(Resource):
    """
        Class to get all orders orders created by a user
    """
    @jwt_required
    def get(self):
        '''Geting all posted orders'''
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)
        return orderobject.find_all_orders(), 200


@fastfood.route('/orders/<int:order_id>')
class OrderActiofastfood(Resource):
    """class to retrive a single order as nterd by user"""
    @jwt_required
    def get(self, order_id):
        '''Geting all posted orders'''
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)
        return orderobject.find_specific_order(order_id), 200

    @jwt_required
    def put(self, order_id):
        '''Editing order satus'''
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)
        try:
            new_status = {
                'status': request.json['status']
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])

        return orderobject.update_status(new_status, order_id), 200
