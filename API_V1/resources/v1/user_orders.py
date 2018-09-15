from flask_restplus import Api, Resource,fields
from app import api
from app.v1.models.manOrders import ManageOrdersDAO

ns = api.namespace('api/v1/orders', description='Orders and their operations')

"""
    Model for adding status to an order
"""
status = api.model('Status',{
    'status': fields.String(required = True, description = 'Add order Status')
})

"""
    Model for placing on food item
"""
order = api.model('Orders',{
    'order_id': fields.Integer(readOnly = True, description = 'An orders unique identifier'),
    'food_item' : fields.String(readOnly = True, description = 'Food Title'),
    'price' : fields.Integer(readOnly = True, description = 'Food item price'),
    'quantity' : fields.Integer(required = True, description = 'Number of food item ordered'),
    'total' : fields.Integer(readOnly = True, description = 'Total amount payable'),
})

"""
    create an instance of class manageOrdersDAO
"""
orderAO=ManageOrdersDAO()

orderAO.create_new_order({'food_item':'Burger','quantity':2})
orderAO.create_new_order({'food_item':'Fish','quantity':3})

"""
    User orders endpoint
"""
@ns.route('')
@ns.response(200, 'This are the orders')
@ns.response(400, 'Bad Request')
@ns.response(404, 'No Orders yet')
class Order(Resource):
    @ns.doc('List all orders made')
    def get(self):
        '''Geting all posted orders'''
        return orderAO.find_all_orders (),200


    @ns.doc('Create food order')
    @ns.expect(order)
    @ns.marshal_with(order, code = 201)
    def post(self):
        '''Post an order'''
        return orderAO.create_new_order(api.payload),201


@ns.route('/<int:order_id>')
@ns.response(200, 'Search was successful')
@ns.response(404, 'Order not Found')
@ns.param('order_id', 'The order unique identifier')
class OrderSpecific(Resource):
    @ns.doc('Retrieve specific order')
    def get(self,order_id):
        ''' Get the specific order searched'''
        return orderAO.get_specific_order(order_id),200



    @ns.doc('Add status to an order')
    @ns.expect(status)
    @ns.marshal_with(status, code = 200)
    def put(self, order_id):
        '''Update the status of order given its identifier'''

        return orderAO.update_order(order_id, api.payload),200

    
    @ns.doc('Delete an Order')
    @ns.response(204, 'Order deleted')
    @ns.response(404, 'Order not found')
    def delete(self, order_id):
        '''Delete a order given its identifier'''

        orderAO.delete_order (order_id)
        return '', 204
