import pytest
from flask import json

#local imports
from app import app
from app.a_p_i.v1.models.authUsers import  ManageUsersDAO,logged_user

testusers = ManageUsersDAO()

"""
    Mock signup data to test the working of user sign up
"""

mock_reg=[{"email":"","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelightgmail.com","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail","username":"delight","password":"delight","confirm_password":"delight"},
          {"email":123454,"username":"delight","password":"delight","confirm_password":"delight"},

          {"email":"yagamidelight@gmail.com","username":"delight","password":"string@12","confirm_password":"string@12"},

          {"email":"yagamidelight@gmail.com","username":"delight","password":123,"confirm_password":123},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight@11","confirm_password":"delight@1"},
          {"email":"yagamidelight@gmail.com","username":"delight","password":"delight","confirm_password":"deli"},

          {"email":"yagamidelight@gmail.com","username":12334,"password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"","password":"delight","confirm_password":"delight"},
          {"email":"yagamidelight@gmail.com","username":"      ","password":"delight","confirm_password":"delight"}
]

"""
    Mock Signin data to test the working of user signin
"""

mock_log=[{"email":123,"password":"delight"},
          {"email":"","password":"delight"},
          {"email":"yagamidelight.com","password":"delight"},
          {"email":"yagamidelight@gmail","password":"delight"},

          {"email":"yagamidelight@gmail.com","password":123},
          {"email":"yagamidelight@gmail.com","password":"deli"},

          {"email":"yagamidelight@gmail.com","password":"string@12"}            
]
"""
    User signUp tests
    -> Email tests
    -> Password tests
    -> user name tests
"""
"""
    Email input checks
        -> Tests input of empty string as email
        -> Tests input of email without @ 
        -> Tests input of email without .com
        -> Test input of int as email
"""
def test_signup_empty_email():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[0],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_wrong_email1():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[1],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_wrong_email2():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[2],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_int_email():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[3],content_type='application/json')
    assert(response.status_code == 400)


"""
    Password Checks
        -> Test int input as password
        -> Test input unmatching password and confirm password
        -> Test input of short password
"""
def test_signup_int_password():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[5],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_passwords_unmatching():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[6],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_poor_passwords():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[7],content_type='application/json')
    assert(response.status_code == 400)


"""
    Username checks
        -> Tests int input as username
        -> tests input of empty string as username
        -> Tests input of spaces as username
"""
def test_signup_int_username():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[8],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_empty_username():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[9],content_type='application/json')
    assert(response.status_code == 400)

def test_signup_spaces_username():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=mock_reg[10],content_type='application/json')
    assert(response.status_code == 400)


"""
    Test of sign up with correct data
"""
def test_signup_correct_data():
    result = app.test_client()
    response = result.post('/api/v1/auth/signup', data=json.dumps(mock_reg[4]),content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert (response.status_code == 201)


"""
    User Sign In Tests
    -> Email tests
    -> password tests
"""


"""
    Email input checks
        -> Test input of int as email
        -> Tests input of empty string as email
        -> Tests input of email without @ 
        -> Tests input of email without .com
"""

def test_signin_int_email():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[0],content_type='application/json')
    assert(response.status_code == 400)

def test_signin_empty_email():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[1],content_type='application/json')
    assert(response.status_code == 400)

def test_signin_wrong_email1():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[2],content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)

def test_signin_wrong_email2():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[3],content_type='application/json')
    assert(response.status_code == 400)


"""
    Password Checks
        -> Test int input as password
        -> Test input of short password
"""
def test_signin_int_password():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[4],content_type='application/json')
    assert(response.status_code == 400)

def test_signin_poor_password():
    result = app.test_client()
    response = result.post('/api/v1/auth/signin', data=mock_log[5],content_type='application/json')
    assert(response.status_code == 400)


"""
    Test of sign in with correct data
"""
def test_signin_correct_data():
    result = app.test_client()
    old_log_users = len(logged_user)
    response = result.post('/api/v1/auth/signin', data=json.dumps(mock_log[6]) ,content_type='application/json')
    json.loads(response.data)
    new_log_users=len(logged_user)
    assert old_log_users + 1 == new_log_users
    assert(response.status_code == 200)