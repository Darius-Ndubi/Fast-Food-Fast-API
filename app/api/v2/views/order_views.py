"""Module on user order endpoint"""
from flask_restplus import Resource, Namespace
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app.api.v2.models.ordersmodel import ManageOrdersDAO
from app.api.v2.models.usermodel import ManageUserDAO
from app.api.v2.models.foodmodel import ManageFoodDAO

fff = Namespace('orders', description='Orders and their operations')

orderao = ManageOrdersDAO()
foodao = ManageFoodDAO()


"""
    User orders endpoint
"""


@fff.route('/users/orders')
class Order(Resource):
    """
        Class to get all orders and add an order
    """
    @jwt_required
    def get(self):
        """Geting all posted by an individual"""
        user_id = get_jwt_identity()
        return orderao.find_user_orders(ManageUserDAO.get_username(user_id)),
        200

    @jwt_required
    # @fff.marshal_with(order, code=201)
    def post(self):
        """Post an order"""
        user_id = get_jwt_identity()

        new_order = {
            'food_id': request.json['food_id'],
            'quantity': request.json['quantity']
        }
        new_order['username'] = ManageUserDAO.get_username(user_id)

        return orderao.create_new_order(new_order), 201


@fff.route('/orders/')
class OrderList(Resource):
    """
        Class to get all orders orders created by a user
    """
    @jwt_required
    def get(self):
        '''Geting all posted orders'''
        user_id = get_jwt_identity()
        foodao.admin_only(user_id)
        return orderao.find_all_orders(), 200


@fff.route('/orders/<int:order_id>')
class OrderActiofff(Resource):
    """class to retrive a single order as nterd by user"""
    @jwt_required
    def get(self, order_id):
        '''Geting all posted orders'''
        user_id = get_jwt_identity()
        foodao.admin_only(user_id)
        return orderao.find_specific_order(order_id), 200

    @jwt_required
    def put(self, order_id):
        '''Geting all posted orders'''
        user_id = get_jwt_identity()
        foodao.admin_only(user_id)
        new_status = {
            'status': request.json['status']
        }
        return orderao.update_status(new_status, order_id), 200
