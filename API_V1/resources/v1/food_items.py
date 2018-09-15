from flask_restplus import Api, Resource,fields
from app import api
from app.v1.models.manFoods import ManageFoodsDAO

ns = api.namespace('api/v1/foods', description='Foods and their operations')


"""
    Model for creating a food item
"""
food_item = api.model('Food',{
    'item_id': fields.Integer(readOnly = True, description = 'Food unique identifier'),
    'title' : fields.String(required = True, description = 'Food Title'),
    'description' : fields.String(required = True, description = 'Food item description'),
    'price' : fields.Integer(required = True, description = 'Food item price'),
    'creator' : fields.String(readOnly = True, description = 'name of restraunt'),
    'type' : fields.String(required = True, description = 'The type of food you just added')
})

"""
    Create an instance of class ManageFoodsDAO
"""
foodAO=ManageFoodsDAO()

#Create a few foods
foodAO.create_new_food_item({'title':'Fries','description':'Crunchier than ever','price':100,'creator':'','type':'Snack'})

"""
    user-food endpoints
"""
@ns.route('')
@ns.response(409, 'Conflict, Same Title')
class Food(Resource):
    @ns.doc('Retrieve all food items')
    def get (self):
        ''' Show all food items on sell '''
        return foodAO.get_all_foods(),200


    @ns.doc('Create a new food item')
    @ns.expect(food_item)
    @ns.marshal_with(food_item, code = 201)
    def post(self):
        ''' Post a food item'''
        return foodAO.create_new_food_item(api.payload),201


@ns.route('/<int:food_id>')
@ns.response(200, 'Search was successful')
@ns.response(404, 'Food not Found')
@ns.param('food_id', 'Food item unique identifier')
class SpecificFood(Resource):
    @ns.doc('Retrieve specific food item')
    def get(self,food_id):
        ''' Get the specific food searched'''
        return foodAO.get_specific_food(food_id),200


    @ns.doc('Edit food item')
    @ns.expect(food_item)
    @ns.marshal_with(food_item, code = 200)
    def put(self, food_id):
        '''Updates the contents of a food item given its id and the data needed'''
        return foodAO.update_food_item(food_id, api.payload),200


    @ns.doc('Delete food item')
    @ns.response(204, 'Item deleted')
    @ns.response(404, 'Food Item not found')
    def delete(self, food_id):
        '''Delete an item given its identifier'''
        foodAO.delete_food_item (food_id)
        return '', 204