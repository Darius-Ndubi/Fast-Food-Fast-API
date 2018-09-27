"""Test module on user order endpoints"""
import pytest
from flask import json

# local imports
from app import app
from app.a_p_i.v2.db.connDB import connDb
from tests.v1.test_order_views import mock_order, mock_answers
from tests.v2.test_auth_views import user_token_creator, admin_token_creator
from app.a_p_i.utility.messages import error_messages, success_messages


def are_orders_added():
    connection = connDb()
    curs = connection.cursor()
    curs.execute("SELECT * FROM orders")
    all_orders = curs.fetchall()
    curs.close()
    connection.close()
    return len(all_orders)


@pytest.fixture
def client():
    """App's test client"""
    return app.test_client()


def test_orders_quantity_not_int(client):
    """test input of string as quantity"""
    with app.app_context():
        tok = user_token_creator()
        response = client.post(
            '/api/v2/users/orders', data=json.dumps(mock_order[0]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[21]["invalid_quantity"]}
        assert(response.status_code == 400)


def test_order_food_item_successfully(client):
    """test input of correct quantity and food item"""
    with app.app_context():
        tok = user_token_creator()
        old_num_orders = are_orders_added()
        response = client.post(
            '/api/v2/users/orders', data=json.dumps(mock_order[3]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        data = json.loads(response.data)
        new_num_orders = are_orders_added()
        assert old_num_orders + 1 == new_num_orders
        response.json == {
            'message': success_messages[3]["order_created1"]
        }
        assert(response.status_code == 201)


def test_orders_retrieval(client):
    """test input of correct quantity and food item"""
    with app.app_context():
        tok = user_token_creator()
        response = client.get(
            '/api/v2/users/orders', content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 200)


def test_admin_get_all_orders(client):
    """test on retrival of all endpoints by admin"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.get(
            '/api/v2/orders/', content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 200)
        assert response.json == [{'creator': 'delight',
                                  'food_id': 1,
                                  'order_id': 1,
                                  'price': 500,
                                  'quantity': 3,
                                  'status': 'NEW',
                                  'title': 'Mokimo',
                                  'total': 1500}]


def test_admin_get_specific_order(client):
    """test on retrival of a specific order"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.get(
            '/api/v2/orders/1', content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 200)
        assert response.json == {'creator': 'delight',
                                 'food_id': 1,
                                 'order_id': 1,
                                 'price': 500,
                                 'quantity': 3,
                                 'status': 'NEW',
                                 'title': 'Mokimo',
                                 'total': 1500}


def test_admin_get_specific_order_not_existing(client):
    """test on retrival of a specific order"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.get(
            '/api/v2/orders/1000', content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 404)
        #assert response.json == {'message':error_messages[20]['item_not_found']}


def test_admin_edit_order_status_with_id(client):
    """test on retrival of a specific order"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.put(
            '/api/v2/orders/1', data=json.dumps(mock_answers[0]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 400)
        assert response.json == {
            'message': error_messages[20]['item_not_found']}


def test_admin_edit_order_status_successfully(client):
    """test on retrival of a specific order"""
    with app.app_context():
        tok = admin_token_creator()
        response = client.put(
            '/api/v2/orders/1', data=json.dumps(mock_answers[0]), content_type='application/json', headers={'Authorization': 'Bearer ' + tok})
        assert(response.status_code == 400)
        assert response.json == {
            'message': error_messages[20]['item_not_found']}
