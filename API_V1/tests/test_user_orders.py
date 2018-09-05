import pytest
from flask import json
from app import app
from app.models.manOrders import ManageOrdersDAO

testorders=ManageOrdersDAO()

"""
    Mock data that is used to test the working of user create order endpoint
"""
mock_order=[{'quantity':'3','food_item':'Burger'},
            {'quantity':3,'food_item':1},
            {'quantity':3,'food_item':'$%^&@!'},
            {'quantity':3,'food_item':'Burger'}]


"""
    A test on list of orders endpoint
"""

def test_orders_retrival():
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)

"""
    Testing the create new order endpoint
    Tests----
        -> test input of string as quantity
        -> test input if int as food_item
        -> test input of special characters as food_item
        -> test input of correct quantity and food item
""" 

def test_orders_quantity_not_int():
    result=app.test_client()
    response= result.post('/api/v1/orders', data=mock_order[0] ,content_type='application/json')
    assert(response.status_code==400)

def test_orders_food_item_not_str():
    result=app.test_client()
    response= result.post('/api/v1/orders', data=mock_order[1] ,content_type='application/json')
    assert(response.status_code==400)

def test_orders_food_item_special_characters():
    result=app.test_client()
    response= result.post('/api/v1/orders', data=mock_order[2] ,content_type='application/json')
    assert(response.status_code==400)

def test_order_food_item_successfully():
    result=app.test_client()
    old_num_orders=len(testorders.orders) + 2
    response= result.post('/api/v1/orders', data=json.dumps(mock_order[3]) ,content_type='application/json')
    data=json.loads(response.data)
    new_num_orders = len (data)    
    assert old_num_orders + 1 == new_num_orders
    assert(response.status_code==201)