import pytest
from flask import json

#local imports
from app import app
from app.v1.models.manOrders import ManageOrdersDAO

testorders=ManageOrdersDAO()

"""
    Mock data that is used to test the working of user create order endpoint
"""
mock_order=[{'quantity':'3','food_item':'Burger'},
            {'quantity':3,'food_item':1},
            {'quantity':3,'food_item':'$%^&@!'},
            {'quantity':3,'food_item':'Burger'}]

"""
    Mock answer data to test the working of user edit order
"""
mock_answers=[{'status':123},{'status':'Rejected'}]


"""
    A test on list of orders endpoint
"""

def test_orders_retrival():
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==404)

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
    old_num_orders=len(testorders.orders)
    response= result.post('/api/v1/orders', data=json.dumps(mock_order[3]) ,content_type='application/json')
    data=json.loads(response.data)
    new_num_orders = len (data)    
    assert old_num_orders + 1 == new_num_orders
    assert(response.status_code==201)


""" Test on retrieving a specific order from the list of orders
    Tests-----
        -> Test on trying to retrieve an order of index negative eg -1,-2
        -> Test on trying to retrieve order not created yet
        -> Test getting a specific order successfully
"""

def test_get_order_negative_identifier():
    result=app.test_client()
    response= result.get('/api/v1/orders/-1' ,content_type='application/json')
    assert(response.status_code == 404)


def test_get_order_not_created():
    result=app.test_client()
    response= result.get('/api/v1/orders/100' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_order_successfully():
    result=app.test_client()
    response= result.get('/api/v1/orders/1' ,content_type='application/json')
    assert(response.status_code == 200)


"""
    Test on updating a specific order status from the list of orders
    Tests-----
        -> Test on trying to edit data with status as an integer
        -> Test on editing an order successfully
"""
def test_status_data_type_not_str():
    result=app.test_client()
    response= result.put('/api/v1/orders/1', data=mock_answers[0] ,content_type='application/json')
    assert(response.status_code==400)

def test_status_add_successfully():
    result=app.test_client()
    response= result.put('/api/v1/orders/1', data=json.dumps(mock_answers[1]) ,content_type='application/json')
    assert(response.status_code==200)


"""
    Test on deleting a specific order from the list of orders
    Tests-----
        -> Test on trying to delete order that does not exist
        -> Test on deleting an existing order successfully
"""
def test_delete_not_existing_order():
    result=app.test_client()
    response= result.delete('/api/v1/orders/300' ,content_type='application/json')
    assert(response.status_code==404)

def test_delete_existing_order():
    result=app.test_client()
    response= result.delete('/api/v1/orders/1' ,content_type='application/json')
    assert(response.status_code==204)



    #tear down your tests

    