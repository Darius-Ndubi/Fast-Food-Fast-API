"""Module on  routes for food items"""

from flask_restplus import Resource, fields, Namespace

# local imports
from app import API
from app.api.v1.models.manFoods import ManageFoodsDAO

ns = Namespace('foods', description='Foods and their operations')


"""
    Model for creating a food item
"""
food_item = API.model('Food', {
    'title': fields.String(required=True, description='Food Title'),
    'description': fields.String(required=True, description='Food item description'),
    'price': fields.Integer(required=True, description='Food item price'),
    'type': fields.String(required=True, description='The type of food you just added')
})

"""
    Create an instance of class ManageFoodsDAO
"""
foodAO = ManageFoodsDAO()

# Create a few foods
#foodAO.create_new_food_item({'title':'Fries','description':'Crunchier than ever','price':100,'creator':'','type':'Snack'})

"""
    user-food endpoints
"""


@ns.route('/foods')
@ns.response(409, 'Conflict, Same Title')
@ns.response(401, 'Please sign in First')
class Food(Resource):
    """A class to handle adding a food item and getting all fooditems endpoints"""
    @ns.doc('Retrieve all food items')
    def get(self):
        ''' Show all food items on sell '''
        return foodAO.get_all_foods(), 200

    @ns.doc('Create a new food item')
    @ns.expect(food_item)
    @ns.marshal_with(food_item, code=201)
    def post(self):
        ''' Post a food item'''
        return foodAO.create_new_food_item(API.payload), 201


@ns.route('/foods/<int:food_id>')
@ns.response(200, 'Search was successful')
@ns.response(404, 'Food not Found')
@ns.response(401, 'Please sign in First')
@ns.param('food_id', 'Food item unique identifier')
class SpecificFood(Resource):
    """A class to handle updatingfood item details
        getting a single item as per its id
        deleting a single food item per its id"""
    @ns.doc('Retrieve specific food item')
    def get(self, food_id):
        ''' Get the specific food searched'''
        return foodAO.get_specific_food(food_id), 200

    @ns.doc('Edit food item')
    @ns.expect(food_item)
    @ns.marshal_with(food_item, code=200)
    def put(self, food_id):
        '''Updates the contents of a food item given its id and the data needed'''
        return foodAO.update_food_item(food_id, API.payload), 200

    @ns.doc('Delete food item')
    @ns.response(204, 'Item deleted')
    @ns.response(404, 'Food Item not found')
    def delete(self, food_id):
        '''Delete an item given its identifier'''
        foodAO.delete_food_item(food_id)
        return '', 204
