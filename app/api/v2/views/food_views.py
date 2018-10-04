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


def auth_required(func):
    func = API.doc(security='apikey')(func)
    def check_auth(*args, **kwargs):
        if 'X-API-KEY' not in request.headers:
            API.abort('401', 'API key required')
        key = request.headers['X-API-KEY']
        #Check key validity
        return func(*args, **kwargs)
    return check_auth


foodobject = ManageFoodDAO()


@fastfood.route('/menu')
@fastfood.response(409, 'Conflict, Same Title')
@fastfood.response(401, 'Please sign in First')
class Food(Resource):
    """A class to handle adding a menu item and getting
     all food items on menu"""
    @fastfood.doc('Retrieve all food items')
    def get(self):
        ''' Show all food items on sell '''
        return foodobject.get_all_foods(), 200

    # securing endpoint with token
    @jwt_required
    @fastfood.doc('Create a new food item')
    @fastfood.doc(security='apikey')
    @auth_required
    @fastfood.expect(food_item)
    def post(self):
        ''' Post a food item'''
        user_id = get_jwt_identity()
        print(user_id)
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
