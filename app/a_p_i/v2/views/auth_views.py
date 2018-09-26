"""Module on user authentication endpoints"""
from flask_restplus import Resource, fields, Namespace
from flask import request, json

# local imports
from app import api
# reusing signup model from v1
from app.a_p_i.v1.views.user_views import user_signup, user_signin
from app.a_p_i.v2.models.UserModel import ManageUserDAO

ns = Namespace('auth', description='User authentication operations')


"""
    User signup enpoint
"""


@ns.route('/auth/signup')
@ns.response(409, 'Email Conflict')
@ns.response(400, 'Incorrect Input')
class SignUp(Resource):
    '''Allows a user to sign up'''
    @ns.doc('New user signup')
    @ns.expect(user_signup)
    @ns.response(201, 'Account created')
    def post(self):
        ''' Sign Up User'''
        new_user = {
            'email':  request.json['email'],
            'username': request.json['username'],
            'password': request.json['password'],
            'confirm_password': request.json['confirm_password'],
        }
        #print (new_user)
        UserAO = ManageUserDAO(
            new_user['email'], new_user['username'], new_user['password'], new_user['confirm_password'])
        return UserAO.SignUpNewUser()


"""
    User login endpoint
"""


@ns.route('/auth/login')
@ns.response(403, 'Email unknown')
@ns.response(409, 'User already signed in')
class Signin(Resource):
    '''Allows a user to login'''
    @ns.doc('Signed Up  user login')
    @ns.expect(user_signin)
    @ns.response(200, 'Login successful')
    def post(self):
        '''Sign In User'''
        existing_user = {
            'email':  request.json['email'],
            'password': request.json['password']
        }
        return ManageUserDAO.loginUser(existing_user['email'], existing_user['password'])
