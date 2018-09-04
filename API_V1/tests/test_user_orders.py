import pytest
from flask import json
from app import app
from app.models.manOrders import orders

"""
    A test on list of orders endpoint
"""

def test_orders_retrival():
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)
