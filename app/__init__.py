from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='Fast Food Fast API',
    description='Fast-Food-Fast is a food delivery service app for a restaurant',)


from app.a_p_i.v1.views.user_views import ns as auth
api.add_namespace(auth, path = '/api/v1')

from app.a_p_i.v1.views.food_views import ns as foods
api.add_namespace(foods, path = '/api/v1')

from app.a_p_i.v1.views.order_views import ns as orders
api.add_namespace(orders, path = '/api/v1')


#whats your expefctation for us
#