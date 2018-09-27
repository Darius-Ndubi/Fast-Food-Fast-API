"""Module on user order endpoint"""
from flask_restplus import Resource,Namespace
from flask import request,json
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app import api
from app.a_p_i.v2.models.ManOrders import ManageOrdersDAO
from app.a_p_i.v2.models.UserModel import ManageUserDAO
from app.a_p_i.v1.views.order_views import order

ns = Namespace('orders', description='Orders and their operations')

orderAO = ManageOrdersDAO()


"""
    User orders endpoint
"""

@ns.route('/users/orders')
@ns.response(200, 'This are the orders')
@ns.response(400, 'Bad Request')
@ns.response(404, 'No Orders yet')
@ns.response(401, 'Please sign in First')
class Order(Resource):
    
    @ns.doc('Create food order')
    @ns.expect(order)
    @jwt_required
    #@ns.marshal_with(order, code=201)
    def post(self):
        '''Post an order'''
        user_id = get_jwt_identity()
    
        new_order = {
            'food_id':request.json['food_id'],
            'quantity':request.json['quantity']
        }
        new_order['username'] = ManageUserDAO.get_username(user_id)
        
        return orderAO.create_new_order(new_order), 201