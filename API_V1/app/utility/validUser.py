from app import api
import re


"""
    Class to validate user entered information
"""

class UserAuthValidator(object):
    # def __init__(self,email,username,password,conPassword):
    #     self.email=email
    #     self.username=username
    #     self.password=password
    #     self.conPassword=conPassword

    """
        Email data validator for both signup and signin forms
    """
    def validEmail(self,email):
        self.email = email
        #check if email type is a string
        if type(self.email) != str:
            api.abort(400, "An email is a string not a number:{} ".format(self.email))
        
        #checking email entered through regular expressions
        elif not re.match(r"(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)" , self.email):
            api.abort(400, "Email: {} is not well formatted (Must have @ and .com) and not contain spaces".format(self.email))
        return True
    """
        Signup password and repeated password data validator
    """
    def validPasswd(self,password,conPassword):
        self.password = password
        self.conPassword = conPassword

        #check if password entered is a string
        if type(self.password) != str:
            api.abort(400, "A password is a string not a number:{} ".format(self.password))

        #check if password and confirm password match
        elif self.password !=self.conPassword:
            api.abort(400, "Password: {} and confirm_password: {} don't match".format(self.password,self.conPassword))

        #checking email entered through regular expressions
        elif not re.match(r"([A-Za-z0-9@#$&*]{6,10})",self.password):
             api.abort(400, "Password: {} is not well formatted or its too short".format(self.password))
        return True
    
    """
        Username data validator
    """    
    def validUsername(self,username):
        self.username = username
        #username check
        if type(self.username) != str :
            api.abort(400, "A username is not a number you enterd: {} ".format(self.username))

        #username check
        elif not re.match(r"([A-Za-z0-9]{5,})",self.username) :
            api.abort(400, "The username is less then 5 characters, You entered: {} ".format(self.username))
        return True

    """
        Sign In password checker
    """
    def validSignInPassword(self,password):
        self.password = password
        if type(password) != str:
            api.abort(400, "A password is a string not a number:{} ".format(password))

        elif not re.match(r"[A-Za-z0-9@#$&*]{6,10}",password):
             api.abort(400, "Password: {} is not well formatted".format(password))
        return True
