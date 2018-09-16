from app import api
#from app.v1.utility.validUser import UserAuthValidator
from app.utility.validUser import UserAuthValidator
from werkzeug.security import generate_password_hash,check_password_hash

""" instance of validation class"""
uservalidatorO= UserAuthValidator()

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
        self.logged_users=[]
        
    """ 
        Check email exixtance
    """
    def check_user_email(self,email):
        for user in self.users:
            if user.get('email') == email:
                
                return user
    """
        Method to validate sigin data
    """
    def signin_data_validator(self,signin_data):
        signinvalidata = UserAuthValidator()
        email_check = signinvalidata.validEmail(signin_data['email'])
        passwd_check = signinvalidata.validSignInPassword(signin_data['password'])

        if email_check & passwd_check == True:
            return True
        return False


    """
        Add new user
    """
    def add_user_details(self,data):

        #user input validation checks
        #uservalidatorO=UserAuthValidator(data['email'],data['username'],data['password'],data['confirm_password'])
        data_check_email = uservalidatorO.validEmail(data['email'])
        data_check_pass  = uservalidatorO.validPasswd(data['password'],data['confirm_password'])
        data_check_uname = uservalidatorO.validUsername(data['username'])


        if data_check_email & data_check_pass & data_check_uname == True:

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
            #print (self.users)
        
            return "Sign Up was successful proceed to Sign In",201

        api.abort (500, "An expected error occurred during data Validation")


        """
        User sign In method
        Steps:
            -> Validated user input to be of expected standards
            -> Check if email of the user exists in the list of registered users
            -> check if user is already signed in
            -> Hash the entered password and verify it matches stored hash
            -> if password hash match add users username to logged in list of users
            -> if email is not found error out that user is not signed up
    """

    def user_signin(self,data):
        #check inputs
        data_check = self.signin_data_validator(data)

        if data_check == True:
        
            #find user with the entered email
            existing_user = self.check_user_email(data['email'])

            #block repeated signins from the same user
            for i in self.logged_users:
                if i == existing_user['username']:
                    api.abort(409, "You: {} are already logged in".format(data['email']))

           #check if the created hash and stored hash match
            if check_password_hash(existing_user.get('password'),data['password']):
                self.logged_users.append(existing_user['username'])
                return "Sign in Successful Go see our food Menu"

            #if they dont match then the entered password is invalid
            else:
                api.abort(401, "Password: {} is invalid".format(data['password']))

        #user is not registered
        api.abort(404, "Sign in request for {} failed, user not signed up!".format(data['email']))
