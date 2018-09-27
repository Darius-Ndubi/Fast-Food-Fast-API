from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os


# local imports
from app.a_p_i.v2.db.create_tables import create_dtb

"""create the necesarry tables"""
create_dtb()

app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)

api = Api(app, version='2.0', title='Fast Food Fast API',
          description='Fast-Food-Fast is a food delivery service app for a restaurant',)


from app.a_p_i.v2.views.auth_views import ns as auth
api.add_namespace(auth, path='/api/v2')

from app.a_p_i.v2.views.food_views import ns as menu
api.add_namespace(menu, path='/api/v2')

from app.a_p_i.v2.views.order_views import ns as orders
api.add_namespace(orders, path='/api/v2')
