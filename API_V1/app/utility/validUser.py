from app import api
import re


"""
    Class to validate user entered information
    It takes in:
        -> email,usernaem,password and confirm password fields
    Steps:
        -> Check if entered email is a str
        -> Check if email consists of a char between a-z,A-Z,0-9 then @ then a-z,A-Z,0-9 then . then a-z,A-Z,0-9
        -> Check if password is enterd as a string
        -> Check if confirm pssword and Password Match
        -> Check if password consists of a char between a-z,A-Z,0-9 then @#$*& and has a minimum of 6 characters and maximum of 10
        -> Check if username is of type string
        -> Check if username consista of chars in a-z,A-Z,0-9 and minimum of 5 characters
"""

class UserAuthValidator(object):
    def __init__(self,email,username,password,conPassword):
        self.email=email
        self.username=username
        self.password=password
        self.conPassword=conPassword

    def signupValidator(self):
        
    
        #check if email type is a string
        if type(self.email) != str:
            api.abort(400, "An email is a string not a number:{} ".format(self.email))
        
        #checking email entered through regular expressions
        elif not re.match(r"(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)" , self.email):
            api.abort(400, "Email: {} is not well formatted (Must have @ and .com) and not contain spaces".format(self.email))

        #check if password entered is a string
        elif type(self.password) != str:
            api.abort(400, "A password is a string not a number:{} ".format(self.password))

        #check if password and confirm password match
        elif self.password !=self.conPassword:
            api.abort(400, "Password: {} and confirm_password: {} don't match".format(self.password,self.conPassword))

        #checking email entered through regular expressions
        elif not re.match(r"([A-Za-z0-9@#$&*]{6,10})",self.password):
             api.abort(400, "Password: {} is not well formatted or its too short".format(self.password))
        
        #username check
        elif type(self.username) != str :
            api.abort(400, "A username is not a number you enterd: {} ".format(self.username))

        #username check
        elif not re.match(r"([A-Za-z0-9]{5,})",self.username) :
            api.abort(400, "The username is less then 5 characters, You entered: {} ".format(self.username))

        return True