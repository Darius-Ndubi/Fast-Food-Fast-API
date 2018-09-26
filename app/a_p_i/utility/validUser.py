"""Module to check user data entered on registration"""

import re

# local imports
from app import api
from app.a_p_i.utility.messages import success_messages, error_messages


class UserAuthValidator():
    """Class to validate user entered information
    """
    # def __init__(self,email,username,password,conPassword):
    #     self.email=email
    #     username=username
    #     password=password
    #     conPassword=conPassword

    def validEmail(self, email):
        """Email data validator for both signup and signin forms
        """
        # check if email type is a string
        if type(email) != str:
            api.abort(400, error_messages[3]['Incorrect_email'])

        # checking email entered through regular expressions
        elif not re.match(r"(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)", email):
            api.abort(
                400, error_messages[2]['Invalid_email'])
        return True

    def validPasswd(self, password, conPassword):
        """Signup password and repeated password data validator
        """
        # check if password entered is a string
        if type(password) != str:
            api.abort(
                400, error_messages[4]['incorrect_passwd'])

        # check if password and confirm password match
        elif password != conPassword:
            api.abort(400, error_messages[5]['unmatching'])

        # checking email entered through regular expressions
        elif not re.match(r"([A-Za-z0-9@#$&*]{6,10})", password):
            api.abort(
                400, error_messages[6]['poor_pass'])
        return True

    def validUsername(self, username):
        """Username data validator
        """
        # username check
        if type(username) != str:
            api.abort(
                400, error_messages[7]['invalid_uname'])

        # username check
        elif not re.match(r"([A-Za-z0-9-]{5,})", username):
            api.abort(
                400, error_messages[8]['poor_uname'])
        return True

    def validSignInPassword(self, password):
        """Sign In password checker
        """
        if type(password) != str:
            api.abort(
                400, error_messages[4]['incorrect_passwd'])

        elif not re.match(r"[A-Za-z0-9@#$&*]{6,10}", password):
            api.abort(400, error_messages[6]['poor_pass'])
        return True
