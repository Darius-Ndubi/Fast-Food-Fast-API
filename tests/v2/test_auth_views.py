"""Test module on user authentication endpoints"""
import pytest
from flask import json

# local imports
from app import app
from app.a_p_i.v2.db.connDB import connDb
from tests.v1.test_auser_views import mock_reg, mock_log


@pytest.fixture
def client():
    """App's test client"""
    return app.test_client()


def registered():
    """A function helps to validate if a user signup is successfull
    by querrying if data is actually entered into db"""

    connection = connDb()
    curs = connection.cursor()

    curs.execute("SELECT * FROM users")
    all = curs.fetchall()

    # close the connection
    curs.close()
    connection.commit()
    connection.close()
    return len(all)


"""
    Email input checks
"""


def test_signup_empty_email(client):
    """Tests input of empty string as email"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[0], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_wrong_email1(client):
    """Tests input of email without @"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[1], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_wrong_email2(client):
    """Tests input of email without .com"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[2], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_int_email(client):
    """Test input of int as email"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[3], content_type='application/json')
    assert(response.status_code == 400)


"""
    Password Checks
"""


def test_signup_int_password(client):
    """Test int input as password"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[5], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_passwords_unmatching(client):
    """Test input unmatching password and confirm password"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[6], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_poor_passwords(client):
    """Test input of short password"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[7], content_type='application/json')
    assert(response.status_code == 400)


"""
    Username checks
"""


def test_signup_int_username(client):
    """Tests int input as username"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[8], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_empty_username(client):
    """tests input of empty string as username"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[9], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_spaces_username(client):
    """Tests input of spaces as username"""
    response = client.post('/api/v2/auth/signup',
                           data=mock_reg[10], content_type='application/json')
    assert(response.status_code == 400)


def test_signup_correct_data(client):
    """Test of sign up with correct data
    """
    #old_num_users = registered()
    response = client.post(
        '/api/v1/auth/signup', data=json.dumps(mock_reg[4]), content_type='application/json')
    #new_num_users = registered()

    assert (response.status_code == 201)
