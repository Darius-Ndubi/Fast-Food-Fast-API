
"""
    Mock data that is used to test the working of user create order endpoint
"""
mock_order = [{'quantity': '3', 'food_id': 'Burger', 'creator': ''},
              {'quantity': 3, 'food_id': "#", 'creator': ''},
              {'quantity': 3, 'food_id': '$%^&@!', 'creator': ''},
              {'quantity': [3], 'food_id': [1]},
              {},
              {'quantity': [3], 'food_id': [1,6]}]

"""
    Mock answer data to test the working of user edit order
"""
mock_answers = [{'status': '123'}, {'status': 'complete'},{}]
