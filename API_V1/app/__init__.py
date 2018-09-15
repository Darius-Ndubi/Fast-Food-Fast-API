from flask import Flask
from flask_restplus import Api


app = Flask(__name__)


api = Api(app, version='1.0', title='Fast Food Fast API',
    description='Fast-Food-Fast is a food delivery service app for a restaurant',)


from resources.user_orders import ns as orders
api.add_namespace(orders)