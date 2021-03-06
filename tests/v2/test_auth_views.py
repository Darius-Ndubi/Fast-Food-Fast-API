"""Test module on user authentication endpoints"""
from flask import json
from flask_jwt_extended import create_access_token

# local imports
from app import app
from app.api.v2.db.conndb import connectdb
from app.api.utility.messages import error_messages, success_messages
from tests.v1.test_auser_views import mock_reg, mock_log


def registered():
    """A function helps to validate if a user signup is successfull
    by querrying if data is actually entered into db"""

    connection = connectdb()
    curs = connection.cursor()

    curs.execute("SELECT * FROM users")
    all_users = curs.fetchall()

    # close the connection
    curs.close()
    connection.close()
    return len(all_users)


def id_picker(email):
    """Function to pick the users id from db that will be used to
     create the access token"""
    connection = connectdb()
    curs = connection.cursor()
    curs.execute(
        "SELECT * FROM users WHERE email = %(email)s", {'email': email})
    user_data = curs.fetchall()
    curs.close()
    connection.close()
    return user_data[0][0]


def user_token_creator():
    """function to generate normal user token"""
    return create_access_token(id_picker(mock_log[6].get('email')))


def admin_token_creator():
    """Function to generate admin token"""
    return create_access_token(id_picker(mock_log[7].get('email')))


def test_signup_empty_email(client):
    """Tests input of empty string as email"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[0]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_signup_wrong_email1(client):
    """Tests input of email without @"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[1]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_signup_wrong_email2(client):
    """Tests input of email without .com"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[2]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_signup_int_email(client):
    """Test input of int as email"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[3]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[3]['Incorrect_email']}
    assert response.status_code == 400


def test_signup_int_password(client):
    """Test int input as password"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[5]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[4]['incorrect_passwd']}
    assert response.status_code == 400


def test_signup_passwords_unmatching(client):
    """Test input unmatching password and confirm password"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[6]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[5]['unmatching']}
    assert response.status_code == 400


def test_signup_poor_passwords(client):
    """Test input of short password"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[7]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[6]['poor_pass']}
    assert response.status_code == 400


def test_signup_int_username(client):
    """Tests int input as username"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[8]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[7]['invalid_uname']}
    assert response.status_code == 400


def test_signup_empty_username(client):
    """tests input of empty string as username"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[9]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[8]['poor_uname']}
    assert response.status_code == 400


def test_signup_spaces_username(client):
    """Tests input of spaces as username"""
    response = client.post('/api/v2/auth/signup',
                           data=json.dumps(mock_reg[10]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[8]['poor_uname']}
    assert response.status_code == 400


def test_signup_empty_json(client):
    """A test on input of an empty json when signup"""
    response = client.post(
        '/api/v2/auth/signup', data=json.dumps(mock_reg[12]),
        content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[25]['invalid_data']}
    assert response.status_code == 400


def test_signup_correct_data(client):
    """Test of sign up with correct data
    """
    old_num_users = registered()
    response = client.post(
        '/api/v2/auth/signup', data=json.dumps(mock_reg[4]),
        content_type='application/json')
    new_num_users = registered()
    assert old_num_users + 1 == new_num_users
    assert response.get_json() == success_messages[0]['account_created']
    assert response.status_code == 201

def test_signup_repeatedly(client):
    """Test of sign up repeatedly with credentials already used
    """
    response = client.post(
        '/api/v2/auth/signup', data=json.dumps(mock_reg[4]),
        content_type='application/json')
    assert response.get_json() == {'message': error_messages[0]['email_conflict']}
    assert response.status_code == 409


def test_signup_test_admin(client):
    """Test of sign up of test admin
    """
    old_num_users = registered()
    response = client.post(
        '/api/v2/auth/signup', data=json.dumps(mock_reg[11]),
        content_type='application/json')
    new_num_users = registered()
    assert old_num_users + 1 == new_num_users
    assert response.get_json() == success_messages[0]['account_created']
    assert response.status_code == 201


def test_login_int_email(client):
    """Test input of int as email"""
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[0]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[3]['Incorrect_email']}
    assert response.status_code == 400


def test_login_empty_email(client):
    """Tests input of empty string as email"""
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[1]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_login_wrong_email1(client):
    """Tests input of email without @ """
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[2]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_login_wrong_email2(client):
    """Tests input of email without .com"""
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[3]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[2]['Invalid_email']}
    assert response.status_code == 400


def test_login_int_password(client):
    """Test int input as password"""
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[4]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[4]['incorrect_passwd']}
    assert response.status_code == 400


def test_login_poor_password(client):
    """Test input of short password"""
    response = client.post('/api/v2/auth/login',
                           data=json.dumps(mock_log[5]),
                           content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[6]['poor_pass']}
    assert response.status_code == 400


def test_login_empty_json(client):
    """A test on input of an empty json when logining in"""
    response = client.post(
        '/api/v2/auth/login', data=json.dumps(mock_log[8]),
        content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[25]['invalid_data']}
    assert response.status_code == 400

def test_login_invalid_password(client):
    """A test on input of a password that does not match the one stored for the user"""
    response = client.post(
        '/api/v2/auth/login', data=json.dumps(mock_log[9]),
        content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[9]['invalid_password']}
    assert response.status_code == 403

def test_login_with_unknown_email_password(client):
    """A test on input of a password and email not in the system"""
    response = client.post(
        '/api/v2/auth/login', data=json.dumps(mock_log[10]),
        content_type='application/json')
    json.loads(response.data.decode('utf-8'))
    assert response.json == {'message': error_messages[10]['not_signed_up']}
    assert response.status_code == 401


def test_login_known_user(client):
    """Test on user login
    """
    with app.app_context():
        response = client.post(
            '/api/v2/auth/login', data=json.dumps(mock_log[6]),
            content_type='application/json')
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert response.json !={"Your access token": user_token_creator()} 


def test_login_admin_user(client):
    """Test on user test admin login
    """
    with app.app_context():
        response = client.post(
            '/api/v2/auth/login', data=json.dumps(mock_log[7]), content_type='application/json')
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert response.json != {"Your access token": admin_token_creator()}
