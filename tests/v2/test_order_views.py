"""Test module on user order endpoints"""
from flask import json

# local imports
from app import app
from app.api.v2.db.conndb import connectdb
from app.api.utility.messages import error_messages, success_messages
from tests.v1.test_order_views import mock_order, mock_answers
from tests.v2.test_auth_views import user_token_creator, admin_token_creator


def are_orders_added():
    """function to find if order is successfully ordered"""
    connection = connectdb()
    curs = connection.cursor()
    curs.execute("SELECT * FROM orders")
    all_orders = curs.fetchall()
    curs.close()
    connection.close()
    return len(all_orders)


def test_orders_quantity_not_int(client):
    """test input of string as quantity"""
    with app.app_context():
        user_token = user_token_creator()
        response = client.post(
            '/api/v2/users/orders', data=json.dumps(mock_order[0]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + user_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[21]["invalid_quantity"]}
        assert response.status_code == 400

def test_order_empty_json_object(client):
    """A test on input of an empty json when ordering food"""
    with app.app_context():
        user_token = user_token_creator()
        response = client.post(
            '/api/v2/users/orders', data=json.dumps(mock_order[4]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + user_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {'message': error_messages[25]['invalid_data']}
        assert response.status_code == 400


def test_order_food_item_successfully(client):
    """test input of correct quantity and food item"""
    with app.app_context():
        user_token = user_token_creator()
        old_num_orders = are_orders_added()
        response = client.post(
            '/api/v2/users/orders', data=json.dumps(mock_order[3]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + user_token})
        json.loads(response.data)
        new_num_orders = are_orders_added()
        assert old_num_orders + 1 == new_num_orders
        assert response.status_code == 201
        assert response.json == ({
            "food id": [1],
            "Total expenditure": 1500,
            "Order Creator": "delight",
            "Order Status": "NEW",
            "price per food": [500],
            "ordered foods": ["Mokimo"],
            "Quantity per food": [3]
        })


def test_orders_retrieval(client):
    """test on user getting orders to them"""
    with app.app_context():
        user_token = user_token_creator()
        response = client.get(
            '/api/v2/users/orders', content_type='application/json',
            headers={'Authorization': 'Bearer ' + user_token})
        assert response.status_code == 200


def test_admin_get_all_orders(client):
    """test on retrival of all endpoints by admin"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.get(
            '/api/v2/orders/', content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 200
        assert response.json == {'All user orders': [{
            "food_id": ['1'],
            "order_id": 1,
            "total": 1500,
            "creator": "delight",
            "status": "NEW",
            "price": ['500'],
            "title": ["Mokimo"],
            "quantity": ['3']
        }]}


def test_admin_get_specific_order(client):
    """test on retrival of a specific order"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.get(
            '/api/v2/orders/1', content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 200
        assert response.json == ({
            "food_id": ['1'],
            "order_id": 1,
            "total": 1500,
            "creator": "delight",
            "status": "NEW",
            "price": ['500'],
            "title": ["Mokimo"],
            "quantity": ['3']
        })


def test_admin_get_specific_order_not_existing(client):
    """test on retrival of a specific order"""
    with app.app_context():
        admin_token= admin_token_creator()
        response = client.get(
            '/api/v2/orders/1000', content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 404


def test_admin_edit_order_status_with_id(client):
    """test on retrival of a specific order"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/orders/1', data=json.dumps(mock_answers[0]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 400
        assert response.json == {
            'message': error_messages[24]["incorect_status"]}

def test_put_empty_json_object(client):
    """A test on input of an empty json when editing food status"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/orders/1', data=json.dumps(mock_answers[2]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {'message': error_messages[25]['invalid_data']}
        assert response.status_code == 400


def test_admin_edit_order_status_successfully(client):
    """test on retrival of a specific order"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/orders/1', data=json.dumps(mock_answers[1]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 200
        assert response.json == {success_messages[4]['edit_success']: {
            "food_id": ['1'],
            "order_id": 1,
            "total": 1500,
            "creator": "delight",
            "status": "Complete",
            "price": ['500'],
            "title": ["Mokimo"],
            "quantity": ['3']
        }}
