"""Module on user authentication endpoints"""
from flask_restplus import Resource, Namespace
from flask import request

# local imports
from app import API
from app.api.utility.messages import error_messages
from app.api.v2.models.user_model import ManageUserDAO
from app.api.v1.views.user_views import user_signup, user_signin


fastfood = Namespace('auth', description='User authentication operations')


"""
    User signup enpoint
"""


@fastfood.route('/auth/signup')
class SignUp(Resource):
    '''Allows a user to sign up'''
    def post(self):
        ''' Sign Up User'''
        try:
            new_user = {
                'email':  request.json['email'],
                'username': request.json['username'],
                'password': request.json['password'],
                'confirm_password': request.json['confirm_password'],
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])

        userobject = ManageUserDAO(
            new_user['email'], new_user['username'], new_user['password'],
            new_user['confirm_password'])
        return userobject.SignUpNewUser()


@fastfood.route('/auth/login')
class Signin(Resource):
    '''Allows a user to login'''
    def post(self):
        '''Sign In User'''
        try:
            existing_user = {
                'email':  request.json['email'],
                'password': request.json['password']
            }
        except:
            API.abort(400, error_messages[25]['invalid_data'])

        return ManageUserDAO.loginUser(existing_user['email'],
                                       existing_user['password'])
