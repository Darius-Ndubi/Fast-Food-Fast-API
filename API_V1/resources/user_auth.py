from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from app import api
from app.models.authUsers import ManageUsersDAO

ns = api.namespace('api/v1/auth', description='User authentication operations')

"""
    User model for user signup data to be entered
"""

user_signup = api.model('Sign Up', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='Your Email'),
    'username': fields.String(required=True, description='Your username'),
    'password': fields.String(required=True, description='Your password'),
    'confirm_password':fields.String(required=True, description='Confirm your password'),
})

"""
    create an instance of class ManageUsersDAO
"""
UserAO=ManageUsersDAO()

"""
    User signup enpoint
"""
@ns.route('/signup')
@ns.response(409, 'Email Conflict')
@ns.response(400, 'Incorrect Input')
class SignUp(Resource):
    '''Allows a user to sign up'''
    @ns.doc('New user signup')
    @ns.expect(user_signup)
    @ns.response(201, 'Account created')
    def post(self):
        return UserAO.add_user_details(api.payload)

