"""Module on user authentication endpoints"""
from flask_restplus import Resource, Namespace
from flask import request

# local imports
from app.a_p_i.v2.models.UserModel import ManageUserDAO

ns = Namespace('auth', description='User authentication operations')


"""
    User signup enpoint
"""


@ns.route('/auth/signup')
class SignUp(Resource):
    '''Allows a user to sign up'''

    def post(self):
        ''' Sign Up User'''
        new_user = {
            'email':  request.json['email'],
            'username': request.json['username'],
            'password': request.json['password'],
            'confirm_password': request.json['confirm_password'],
        }
        # print (new_user)
        UserAO = ManageUserDAO(
            new_user['email'], new_user['username'], new_user['password'],
            new_user['confirm_password'])
        return UserAO.SignUpNewUser()


@ns.route('/auth/login')
class Signin(Resource):
    '''Allows a user to login'''

    def post(self):
        '''Sign In User'''
        existing_user = {
            'email':  request.json['email'],
            'password': request.json['password']
        }
        return ManageUserDAO.loginUser(existing_user['email'],
                                       existing_user['password'])
