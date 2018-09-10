from flask_restplus import Api, Resource,fields
from werkzeug.contrib.fixers import ProxyFix
from app import api
from app.models.manFoods import ManageFoodsDAO

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
    @ns.doc('Create a new food item')
    @ns.expect(food_item)
    @ns.marshal_with(food_item, code = 201)
    def post(self):
        ''' Post a food item'''
        return foodAO.create_new_food_item(api.payload),201