"""Test user authentication endpoints"""
from flask import json

# local imports
from app import app
from app.a_p_i.v1.models.authUsers import ManageUsersDAO, logged_user

testusers = ManageUsersDAO()



"""
    Mock signup data to test the working of user sign up
"""

mock_reg = [{"email": "", "username": "delight", "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelightgmail.com", "username": "delight",
             "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail", "username": "delight",
                "password": "delight", "confirm_password": "delight"},
            {"email": 123454, "username": "delight",
                "password": "delight", "confirm_password": "delight"},

            {"email": "yagamidelight@gmail.com", "username": "delight",
                "password": "string@12", "confirm_password": "string@12"},

            {"email": "yagamidelight@gmail.com", "username": "delight",
                "password": 123, "confirm_password": 123},
            {"email": "yagamidelight@gmail.com", "username": "delight",
                "password": "delight@11", "confirm_password": "delight@1"},
            {"email": "yagamidelight@gmail.com", "username": "delight",
                "password": "delight", "confirm_password": "deli"},

            {"email": "yagamidelight@gmail.com", "username": 12334,
                "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail.com", "username": "",
                "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail.com", "username": "      ",
                "password": "delight", "confirm_password": "delight"},
            {"email": "testfast@food.com", "username": "fast-food-fast", "password": "Admintester", "confirm_password": "Admintester"}]

"""
    Mock Signin data to test the working of user signin
"""

mock_log = [{"email": 123, "password": "delight"},
            {"email": "", "password": "delight"},
            {"email": "yagamidelight.com", "password": "delight"},
            {"email": "yagamidelight@gmail", "password": "delight"},

            {"email": "yagamidelight@gmail.com", "password": 123},
            {"email": "yagamidelight@gmail.com", "password": "deli"},

            {"email": "yagamidelight@gmail.com", "password": "string@12"},
            {"email": "testfast@food.com", "password": "Admintester"}]

"""
    User signUp tests
    -> Email tests
    -> Password tests
    -> user name tests
"""
"""
    Email input checks
"""


def test_signup_empty_email():
    """Tests input of empty string as email"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[0], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_wrong_email1():
    """Tests input of email without @"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[1], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_wrong_email2():
    """Tests input of email without .com"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[2], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_int_email():
    """Test input of int as email"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[3], content_type='application/json')
    assert(response.status_code == 400)


"""
    Password Checks
"""


def test_signup_int_password():
    """Test int input as password"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[5], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_passwords_unmatching():
    """Test input unmatching password and confirm password"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[6], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_poor_passwords():
    """Test input of short password"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[7], content_type='application/json')
    assert(response.status_code == 400)


"""
    Username checks
"""


def test_signup_int_username():
    """Tests int input as username"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[8], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_empty_username():
    """tests input of empty string as username"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[9], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_spaces_username():
    """Tests input of spaces as username"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signup',
                           data=mock_reg[10], content_type='application/json')
    assert(response.status_code == 400)


# def test_signup_correct_data():
#     """Test of sign up with correct data
#     """
#     result = app.test_client()
#     response = result.post('/api/v1/auth/signup', data=json.dumps(mock_reg[4]), content_type='application/json')
#     json.loads(response.data.decode('utf-8'))
#     assert (response.status_code == 201)

def test_signup_test_admin():
    """test to signup an admin user"""
    result = app.test_client()
    response = result.post(
        '/api/v1/auth/signup', data=json.dumps(mock_reg[11]), content_type='application/json')
    assert (response.status_code == 201)


"""
    User Sign In Tests
    -> Email tests
    -> password tests
"""


def test_signin_int_email():
    """Test input of int as email"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[0], content_type='application/json')
    assert(response.status_code == 400)


def test_signin_empty_email():
    """Tests input of empty string as email"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[1], content_type='application/json')
    assert(response.status_code == 400)


def test_signin_wrong_email1():
    """Tests input of email without @ """
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[2], content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 400)


def test_signin_wrong_email2():
    """Tests input of email without .com"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[3], content_type='application/json')
    assert(response.status_code == 400)


"""
    Password Checks
"""


def test_signin_int_password():
    """Test int input as password"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[4], content_type='application/json')
    assert(response.status_code == 400)


def test_signin_poor_password():
    """Test input of short password"""
    result = app.test_client()
    response = result.post('/api/v1/auth/signin',
                           data=mock_log[5], content_type='application/json')
    assert(response.status_code == 400)


# def test_signin_correct_data():
#     """Test of sign in with correct data
#     """
#     result = app.test_client()
#     old_log_users = bool(logged_user)
#     response = result.post('/api/v1/auth/signin', data=json.dumps(mock_log[6]), content_type='application/json')
#     json.loads(response.data)
#     new_log_users = bool(logged_user)
#     print (logged_user)
#     assert old_log_users != new_log_users
#     assert(response.status_code == 200)

def test_signin_admin():
    """Test of admin sign in
    """
    result = app.test_client()
    old_log_users = bool(logged_user)
    response = result.post(
        '/api/v1/auth/signin', data=json.dumps(mock_log[7]), content_type='application/json')
    json.loads(response.data)
    new_log_users = bool(logged_user)
    assert old_log_users != new_log_users
    assert(response.status_code == 200)
