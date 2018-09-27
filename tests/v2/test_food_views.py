""" Module to test on food endpoints"""
from flask import json
import pytest

# local imports
from app import app
from tests.v1.test_yfood_views import mock_food
from tests.v2.test_auth_views import tok
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
    response = client.post(
        '/api/v2/foods', data=mock_food[0], content_type='application/json')
    assert(response.status_code == 400)


def test_food_item_empty_description(client):
    """test on empty food title"""
    response = client.post(
        '/api/v2/foods', data=mock_food[1], content_type='application/json')
    assert(response.status_code == 400)


def test_food_item_string_price(client):
    """test on empty food description"""
    response = client.post(
        '/api/v2/foods', data=mock_food[2], content_type='application/json')
    assert(response.status_code == 400)


def test_food_item_empty_type(client):
    """test on empty food type"""
    response = client.post(
        '/api/v2/foods', data=mock_food[3], content_type='application/json')
    assert(response.status_code == 400)


"""
    Test on successfull adding of food item"
"""


def test_create_food_successfully(client):
    """Is the item being successfuly ordered"""
    response = client.post(
        '/api/v2/foods', data=json.dumps(mock_food[4]), content_type='application/json')
    assert(response.status_code == 201)
