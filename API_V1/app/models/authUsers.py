from app import api
from app.utility.validUser import UserAuthValidator
from werkzeug.security import generate_password_hash,check_password_hash

""" 
    A class to handle the
        -> Signup of new users
        Steps
            -> It check if the user email is linked to another account
                if linked it errors out that there is a conflict
            
            -> It validates user input using modules in the utility
                if input is not of expected format an error is outputed
            
            -> If the above checks pass it allows user to signup
        
"""

class ManageUsersDAO(object):
    def __init__(self):
        self.users=[]
        
    """ 
        Check email exixtance
    """
    def check_user_email(self,email):
        for user in self.users:
            if user.get('email') == email:
                
                return email

    """
        Add new user
    """
    def add_user_details(self,data):

        #user input validation checks
        uservalidatorO=UserAuthValidator(data['email'],data['username'],data['password'],data['confirm_password'])
        data_check = uservalidatorO.signupValidator()

        if data_check == True:

            #email existance check
            if self.check_user_email(data['email']) != None:
                api.abort(409, "Sign up request for {} could not be completed due to existance of same email".format(data['email']))
            
            #user id assignment
            data['id'] = len(self.users)+1
            #password hashing
            password_hash = generate_password_hash(data['password'])

            data['password'] = password_hash
            data['confirm_password']='#'

            #append the user data dictionary to users list
            self.users.append(data)
            print (self.users)
        
            return "Sign Up was successful proceed to Sign In",201

        api.abort (500, "An expected error occurred during data Validation")
