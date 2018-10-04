from flask_restplus import Resource, fields, Namespace

# local imports
from app import API
from app.api.v1.models.authUsers import ManageUsersDAO

ns = Namespace('auth', description='User authentication operations')

"""
    User model for user signup data to be entered
"""
# 'id': fields.Integer(readOnly=True, description='The user unique identifier'),

user_signup = API.model('Sign Up', {
    'email': fields.String(required=True, description='Your Email'),
    'username': fields.String(required=True, description='Your username'),
    'password': fields.String(required=True, description='Your password'),
    'confirm_password': fields.String(required=True, description='Confirm your password')
})

"""Model for signin data to be entered by user
"""
user_signin = API.model('Sign In', {
    'email': fields.String(required=True, description='Your Email'),
    'password': fields.String(required=True, description='Your password')
})

"""
    create an instance of class ManageUsersDAO
"""
UserAO = ManageUsersDAO()

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

        return UserAO.add_user_details(API.payload)


"""
    User signin endpoint
"""


@ns.route('/auth/signin')
@ns.response(403, 'Email unknown')
@ns.response(409, 'User already signed in')
class Signin(Resource):
    '''Allows a user to sign in'''
    @ns.doc('Signed Up  user Sign In')
    @ns.expect(user_signin)
    @ns.response(200, 'Sign In successful')
    def post(self):
        '''Sign In User'''

        return UserAO.user_signin(API.payload), 200
