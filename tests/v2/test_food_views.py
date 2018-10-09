""" Module to test on food endpoints"""
from flask import json

# local imports
from app import app
from app.api.v2.db.conndb import connectdb
from app.api.utility.messages import error_messages,success_messages
from tests.v1.test_yfood_views import mock_food,mock_up_food
from tests.v2.test_auth_views import admin_token_creator


def food_items():
    connection = connectdb()
    curs = connection.cursor()
    curs.execute("SELECT * FROM foods")
    all_foods = curs.fetchall()
    return len(all_foods)


def test_food_item_empty_title(client):
    """test on empty food title"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[0]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[12]['wrong_format_title']}
        assert response.status_code == 400


def test_food_item_empty_description(client):
    """test on empty food title"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[1]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[14]['wrong_format_des']}
        assert response.status_code == 400


def test_food_item_string_price(client):
    """test on empty food description"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[2]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {'message': error_messages[15]['str_price']}
        assert response.status_code == 400


def test_food_item_empty_type(client):
    """test on empty food type"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[3]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {
            'message': error_messages[17]['wrong_format_ty']}
        assert response.status_code == 400

def test_food_empty_json_object(client):
    """A test on input of an empty json when creating a menu item"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[5]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.json == {'message': error_messages[25]['invalid_data']}
        assert response.status_code == 400

def test_on_retrieving_all_menu_items_before_any_is_created(client):
    """Test on retrieving all menu items"""
    response = client.get(
        '/api/v2/menu', content_type='application/json')
    assert response.status_code == 404

def test_create_food_successfully(client):
    """Test on if food item id being created successfully"""
    with app.app_context():
        old_num_items = food_items()
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[4]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        new_num_items = food_items()
        assert old_num_items + 1 == new_num_items
        assert response.status_code == 201


def test_try_to_create_food_again(client):
    """test on trying to add food repeatatively"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[4]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 409


def test_create_food_successfully2(client):
    """Test to create a second food item to test editing a food item"""
    with app.app_context():
        old_num_items = food_items()
        admin_token = admin_token_creator()
        response = client.post(
            '/api/v2/menu', data=json.dumps(mock_food[6]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        new_num_items = food_items()
        assert old_num_items + 1 == new_num_items
        assert response.status_code == 201

def test_edit_food_item_not_existing(client):
    """test to edit a food item that does not exist"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/menu/100', data=json.dumps(mock_up_food[4]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 404

def test_edit_food_item_existing_title(client):
    """test to edit a food item with existing title"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/menu/2', data=json.dumps(mock_food[6]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 409


def test_edit_food_item(client):
    """test to edit a food item"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.put(
            '/api/v2/menu/2', data=json.dumps(mock_up_food[4]),
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200



def test_on_retrieving_all_menu_items(client):
    """Test on retrieving all menu items"""
    response = client.get(
        '/api/v2/menu', content_type='application/json')
    assert response.status_code == 200

def test_on_deleting_an_item_not_existing(client):
    """Test on deleting a food item that doesnot exist"""
    with app.app_context():
        admin_token = admin_token_creator()
        response = client.delete(
            '/api/v2/menu/20000', content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        assert response.status_code == 404

def test_on_deleting_an_item(client):
    """Test on deleting a food item"""
    with app.app_context():
        admin_token = admin_token_creator()
        old_num_items = food_items()
        response = client.delete(
            '/api/v2/menu/2', content_type='application/json',
            headers={'Authorization': 'Bearer ' + admin_token})
        new_num_items = food_items()
        assert new_num_items +1 == old_num_items
        assert response.json == {'Message': success_messages[7]['Delete']}
        assert response.status_code == 200