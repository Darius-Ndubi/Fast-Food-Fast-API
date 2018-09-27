"""Module on  routes for food items"""
from flask import request, json
from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app import api
from app.a_p_i.v1.views.food_views import food_item
from app.a_p_i.v2.models.FoodModel import ManageFoodDAO

ns = Namespace('menu', description='Foods and their operations')

foodAO = ManageFoodDAO()


@ns.route('/menu')
@ns.response(409, 'Conflict, Same Title')
@ns.response(401, 'Please sign in First')
@ns.response(500, 'Expired token')
@ns.response(201, 'Food added successfuly')
@ns.response(404, 'No menu items yet')
class Food(Resource):
    """A class to handle adding a menu item and getting all food items on menu"""
    @ns.doc('Retrieve all food items')
    def get(self):
        ''' Show all food items on sell '''
        return foodAO.get_all_foods(), 200

    @ns.doc('Create a new food item')
    @ns.expect(food_item)
    # securing endpoint with token
    @jwt_required
    def post(self):
        ''' Post a food item'''
        user_id = get_jwt_identity()
        foodAO.admin_only(user_id)

        new_item = {
            'title':  request.json['title'],
            'description': request.json['description'],
            'price': request.json['price'],
            'type': request.json['type']
        }
        return foodAO.create_menu_item(new_item)
