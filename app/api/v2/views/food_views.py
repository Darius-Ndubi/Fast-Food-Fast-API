"""Module on  routes for food items"""
from flask import request
from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app.api.v2.models.foodmodel import ManageFoodDAO

fff = Namespace('menu', description='Foods and their operations')

foodao = ManageFoodDAO()


@fff.route('/menu')
class Food(Resource):
    """A class to handle adding a menu item and getting
     all food items on menu"""

    def get(self):
        ''' Show all food items on sell '''
        return foodao.get_all_foods(), 200

    # securing endpoint with token
    @jwt_required
    def post(self):
        ''' Post a food item'''
        user_id = get_jwt_identity()
        foodao.admin_only(user_id)

        new_item = {
            'title':  request.json['title'],
            'description': request.json['description'],
            'price': request.json['price'],
            'type': request.json['type']
        }
        return foodao.create_menu_item(new_item)
