"""Module on  routes for food items"""
from flask import request
from flask_restplus import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

# local imports
from app import API
from app.api.utility.messages import error_messages
from app.api.v2.models.food_model import ManageFoodDAO
from app.api.v1.views.food_views import food_item

fastfood = Namespace('menu', description='Foods and their operations')

foodobject = ManageFoodDAO()


@fastfood.route('/menu')
class Food(Resource):
    """A class to handle adding a menu item and getting
     all food items on menu"""
    def get(self):
        ''' Show all food items on sell '''
        return foodobject.get_all_foods(), 200

    # securing endpoint with token
    @jwt_required
    def post(self):
        ''' Post a food item'''
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)

        try:
            new_item = {
                'title':  request.json['title'],
                'description': request.json['description'],
                'price': request.json['price'],
                'type': request.json['type']
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])

        return foodobject.create_menu_item(new_item)

@fastfood.route('/menu/<int:food_id>')
class FoodItem(Resource):
    """A class to handle actions to a menu item and getting"""
    @jwt_required
    def put(self,food_id):
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)

        try:
            edit_item = {
                'title':  request.json['title'],
                'description': request.json['description'],
                'price': request.json['price'],
                'type': request.json['type']
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])
            
        return foodobject.edit_menu_item(food_id,edit_item)

    @jwt_required
    def delete(self,food_id):
        """Method to delete food item from menu"""
        user_id = get_jwt_identity()
        foodobject.admin_only(user_id)

        return foodobject.delete_menu_item(food_id)
