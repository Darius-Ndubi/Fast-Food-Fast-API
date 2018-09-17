from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

#add a secret key 
app.secret_key = '\xaa\x98\xfb\xf7\xcb?\xce\xd3\xdf\x96'

api = Api(app, version='1.0', title='Fast Food Fast API',
    description='Fast-Food-Fast is a food delivery service app for a restaurant',)


from resources.v1.user_auth import ns as auth
api.add_namespace(auth)

from resources.v1.food_items import ns as foods
api.add_namespace(foods)

from resources.v1.user_orders import ns as orders
api.add_namespace(orders)
