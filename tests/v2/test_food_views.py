""" Module to test on food endpoints"""
from flask import json
import pytest

# local imports
from app import app
from tests.v1.test_yfood_views import mock_food
from tests.v2.test_auth_views import admin_token_creator, user_token_creator
from app.a_p_i.utility.messages import error_messages, success_messages

"""
    Tests on food creation endpoint on data validation tests
"""


@pytest.fixture
def client():
    """App's test client"""
    return app.test_client()


def test_food_item_empty_title(client):
    """test on empty food title"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.post('/api/v2/menu', data=json.dumps(
            mock_food[0]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[12]['wrong_format_title']}
        assert(response.status_code == 400)


def test_food_item_empty_description(client):
    """test on empty food title"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[1]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[14]['wrong_format_des']}
        assert(response.status_code == 400)


def test_food_item_string_price(client):
    """test on empty food description"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[2]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {'message': error_messages[15]['str_price']}
        assert(response.status_code == 400)


def test_food_item_empty_type(client):
    """test on empty food type"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[3]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[17]['wrong_format_ty']}
        assert(response.status_code == 400)


"""
    Test on successfull adding of food item"
"""


def test_create_food_successfully(client):
    """Is the item being successfuly ordered"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[4]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert(response.status_code == 201)
