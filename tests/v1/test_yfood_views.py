"""Module to test endpoints related to food only"""
from flask import json

# local imports
from app import app
from app.a_p_i.v1.models.manFoods import ManageFoodsDAO
from app.a_p_i.v1.models.manOrders import food_items

testfoods = ManageFoodsDAO()

"""
    mock data on food items data to be entered
"""

mock_food = [{'title': "", 'description': 'Better than moms way', 'price': 500, 'creator': '', 'type': 'meal'},
             {'title': "Mokimo", 'description': '',
                 'price': 500, 'creator': '', 'type': 'meal'},
             {'title': "Mokimo", 'description': 'Better than moms way',
                 'price': '', 'creator': '', 'type': 'meal'},
             {'title': "Mokimo", 'description': 'Better than moms way',
                 'price': 500, 'creator': '', 'type': ''},
             {'title': "Mokimo", 'description': 'Better than moms way', 'price': 500, 'creator': '', 'type': 'meal'}]

""" 
    Mock data to edit existing food item
"""
mock_up_food = [{'title': "", 'description': 'The best you will ever eat East of Victoria', 'price': 200, 'creator': '', 'type': 'meal'},
                {'title': "Omena", 'description': '',
                    'price': 500, 'creator': '', 'type': 'meal'},
                {'title': "Omena", 'description': 'The best you will ever eat East of Victoria',
                    'price': '', 'creator': '', 'type': 'meal'},
                {'title': "Omena", 'description': 'The best you will ever eat East of Victoria',
                 'price': 200, 'creator': '', 'type': ''},
                {'title': "Omena", 'description': 'The best you will ever eat East of Victoria', 'price': 200, 'creator': '', 'type': 'meal'}]

# """
#     Tests on food creation endpoint on data validation tests
# """


# def test_food_item_empty_title():
#     """test on empty food title"""
#     result = app.test_client()
#     response = result.post(
#         '/api/v1/foods', data=mock_food[0], content_type='application/json')
#     assert(response.status_code == 400)


# def test_food_item_empty_description():
#     """test on empty food title"""
#     result = app.test_client()
#     response = result.post(
#         '/api/v1/foods', data=mock_food[1], content_type='application/json')
#     assert(response.status_code == 400)


# def test_food_item_string_price():
#     """test on empty food description"""
#     result = app.test_client()
#     response = result.post(
#         '/api/v1/foods', data=mock_food[2], content_type='application/json')
#     assert(response.status_code == 400)


# def test_food_item_empty_type():
#     """test on empty food type"""
#     result = app.test_client()
#     response = result.post(
#         '/api/v1/foods', data=mock_food[3], content_type='application/json')
#     assert(response.status_code == 400)


# """
#     Test on successfull adding of food item"
# """


# def test_create_food_successfully():
#     """Is the item being successfuly ordered"""
#     result = app.test_client()
#     old_num_items = len(food_items)
#     response = result.post(
#         '/api/v1/foods', data=json.dumps(mock_food[4]), content_type='application/json')
#     json.loads(response.data)
#     new_num_items = len(food_items)
#     assert old_num_items + 1 == new_num_items
#     assert(response.status_code == 201)


# def test_retreving_all_food_items():
#     """Test on retrieviving food items"""
#     result = app.test_client()
#     response = result.get('/api/v1/foods', content_type='application/json')
#     assert response.status_code == 200


# def test_retreving_specific_food_order():
#     """Test on specific food item Retrival"""
#     result = app.test_client()
#     response = result.get('/api/v1/foods/1', content_type='application/json')
#     assert response.status_code == 200


# """
#     Tests on food updating endpoint on data validation tests
# """


# def test_edit_food_item_empty_title():
#     """test on empty food title"""
#     result = app.test_client()
#     response = result.put(
#         '/api/v1/foods/1', data=mock_up_food[0], content_type='application/json')
#     assert(response.status_code == 400)


# def test_edit_food_item_empty_description():
#     """test on empty food description"""
#     result = app.test_client()
#     response = result.put(
#         '/api/v1/foods/1', data=mock_up_food[1], content_type='application/json')
#     assert(response.status_code == 400)


# def test_edit_food_item_string_price():
#     """test on string food price"""
#     result = app.test_client()
#     response = result.put(
#         '/api/v1/foods/1', data=mock_up_food[2], content_type='application/json')
#     assert(response.status_code == 400)


# def test_edit_food_item_empty_type():
#     """test on empty food type"""
#     result = app.test_client()
#     response = result.put(
#         '/api/v1/foods/1', data=mock_up_food[3], content_type='application/json')
#     assert(response.status_code == 400)


# def test_yupdate_food_successfully():
#     """ Test on successfull editing of a food item"""
#     result = app.test_client()
#     response = result.put(
#         '/api/v1/foods/1', data=json.dumps(mock_up_food[4]), content_type='application/json')
#     assert(response.status_code == 200)


# """
#     Test on deleting a specific food item from the list of food_items
# """


# def test_delete_not_existing_food_item():
#     """Test on trying to delete food item that does not exist"""
#     result = app.test_client()
#     response = result.delete(
#         '/api/v1/foods/300', content_type='application/json')
#     assert(response.status_code == 404)


# def test_delete_existing_food_item():
#     """Test on deleting an existing food item successfully"""
#     result = app.test_client()
#     response = result.delete(
#         '/api/v1/foods/3', content_type='application/json')
#     assert(response.status_code == 204)
