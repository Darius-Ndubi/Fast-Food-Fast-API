from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os


# local imports
from app.api.v2.db.create_tables import create_dtb

"""create the necesarry tables"""
create_dtb()

app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)


API = Api(app, version='2.0', title='Fast Food Fast API',
          description='Fast-Food-Fast is a food delivery service app for a restaurant')


# catching the token expired message
jwt._set_error_handler_callbacks(API)


from app.api.v2.views.auth_views import fastfood as auth
API.add_namespace(auth, path='/api/v2')

from app.api.v2.views.food_views import fastfood as menu
API.add_namespace(menu, path='/api/v2')

from app.api.v2.views.order_views import fastfood as orders
API.add_namespace(orders, path='/api/v2')
