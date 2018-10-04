"""module to hold apps messages"""

error_messages = [{'email_conflict':
                   'Sign up request for could not be completed due to' +
                   ' existance of same email'},
                  {'validation_error':
                   "An expected error occurred during data Validation"},
                  {'Invalid_email':
                   "Email is not well formatted (Must have @ and .com) and " +
                   "not contain spaces or #,$,%,^,&,*,!,(,) and :"},
                  {'Incorrect_email': "An email should string not a number"},
                  {'incorrect_passwd': "A password is a string not a number"},
                  {'unmatching': 'Password and confirm password don\'t match'},
                  {'poor_pass':
                   "Password should contain @,#,$,& or * with minimum of 6" +
                   " chars and maximum of 10"},
                  {'invalid_uname':
                   "A username is not a number,spaces or empty"},
                  {'poor_uname':
                   "The username is less then 5 characters or doesn't " +
                   "contain letters a-z or A-Z or - ONLY"},
                  {'invalid_password': "Password or email invalid"},
                  {'not_signed_up':
                   "Sign in request failed, user not signed up!"},
                  {'Int_title': "Title entered is not a string"},
                  {'wrong_format_title':
                   "Title entered should have letter between a-z or A-Z or _"},
                  {'int_des': "Description entered is not an string"},
                  {'wrong_format_des':
                   "description entered should have letter between a-z or " +
                   "A-Z or _ "},
                  {'str_price': "Price entered is not an integer"},
                  {'int_type': "Type entered is not an string"},
                  {'wrong_format_ty':
                   "Title entered should have letter between a-z or A-Z or _"},
                  {'food_exist':
                   "food item creation could not be completed due to " +
                   "existance of same item"},
                  {'unmet_priv':
                   "Sorry your privileges won't allow you to perform this" +
                   "action"},
                  {'item_not_found': "Item or items do not exist"},
                  {"invalid_quantity": "Quantity entered is not an integer"},
                  {"None_zero":
                   "Order id cannot be found, Orders are identified from 1" +
                   " onwards"},
                  {"invalid_status": "Order status  should be a string"},
                  {"incorect_status":
                   "Order status can either be processing , cancelled or" +
                   " complete. Ensure you have no spaces at the begining" +
                   " or end of status entered"},
                  {"invalid_data": "You have either not entered anything" +
                   " in the body or the json object is invalid"}
                  ]

success_messages = [
    {'account_created': 'Sign Up was successful proceed to Sign In'},
    {"food_created": "Food item was successfully created"},
    {'order_created': "order was successfully created"},
    {"order_created1": "Order has been created you,You can edit it to" +
     " make modifications"},
    {'edit_success': 'Status update was successfull'},
    {'user_orders': "All users orders"},
    {'user_order': 'Your orders'}
]
