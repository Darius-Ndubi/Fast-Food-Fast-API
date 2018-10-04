"""Module on user authentication endpoints"""
from flask_restplus import Resource, Namespace
from flask import request

# local imports
from app import api
from app.api.utility.messages import error_messages
from app.api.v2.models.user_model import ManageUserDAO
from app.api.v1.views.user_views import user_signup, user_signin


fastfood = Namespace('auth', description='User authentication operations')


"""
    User signup enpoint
"""


@fastfood.route('/auth/signup')
@fastfood.response(409, 'Email Conflict')
@fastfood.response(400, 'Incorrect Input')
class SignUp(Resource):
    '''Allows a user to sign up'''
    @fastfood.doc('New user signup')
    @fastfood.expect(user_signup)
    @fastfood.response(201, 'Account created')
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
            api.abort(400, error_messages[25]['invalid_data'])

        userobject = ManageUserDAO(
            new_user['email'], new_user['username'], new_user['password'],
            new_user['confirm_password'])
        return userobject.SignUpNewUser()


@fastfood.route('/auth/login')
@fastfood.response(400, 'Input syntax errors')
@fastfood.response(401, 'Un-authorized user')
@fastfood.response(403, 'Request forbidden')
@fastfood.response(409, 'User already signed in')
class Signin(Resource):
    '''Allows a user to login'''
    @fastfood.doc('Signed Up  user Sign In')
    @fastfood.expect(user_signin)
    @fastfood.response(200, 'Sign In successful')
    def post(self):
        '''Sign In User'''
        try:
            existing_user = {
                'email':  request.json['email'],
                'password': request.json['password']
            }
        except:
            api.abort(400, error_messages[25]['invalid_data'])

        return ManageUserDAO.loginUser(existing_user['email'],
                                       existing_user['password'])
