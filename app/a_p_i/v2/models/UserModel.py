""" module to handle siging up, and loging in user to db """
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import os

# local imports
from app import api
from app.a_p_i.utility.validUser import UserAuthValidator
from app.a_p_i.v2.db.connDB import connDb
from app.a_p_i.utility.messages import success_messages, error_messages

""" instance of validation class"""
uservalidatorO = UserAuthValidator()


class ManageUserDAO():
    def __init__(self, email, username, password, confirm_password):
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    def CheckUserExistance(self):
        """Method to check if user exists
        Check if a matching email exists in the DataBase"""
        connection = connDb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE email = %(email)s",
                     {'email': self.email})
        existing_user = curs.fetchall()
        curs.close()
        connection.close()

        return existing_user

    def SignUpNewUser(self):
        """Method to validated user, and add to the database
            If all checks have passed add the user"""
        data_check_email = uservalidatorO.validEmail(self.email)
        data_check_pass = uservalidatorO.validPasswd(
            self.password, self.confirm_password)
        data_check_uname = uservalidatorO.validUsername(self.username)
        if str(self.username) == os.getenv('PRIV'):
            
            user_priv = True
        else:
            user_priv = False

        if data_check_email & data_check_pass & data_check_uname:

            if self.CheckUserExistance():
                api.abort(
                    409, error_messages[0]['email_conflict'])

            connection = connDb()
            curs = connection.cursor()

            self.passwd_hash = generate_password_hash(self.password)

            curs.execute("INSERT INTO users (email,username,priv,password) VALUES(%s,%s,%s,%s)",
                         (self.email, self.username, user_priv, self.passwd_hash))

            curs.close()
            connection.commit()
            connection.close()
            return success_messages[0]['account_created'], 201
        api.abort(500, error_messages[1]['validation_error'])

    @staticmethod
    def loginUser(email, password):
        """Method to validata user on login and checking if they exist
        if they do it compares the password hashes
        if this pasess it create user access token"""
        data_check_email = uservalidatorO.validEmail(email)
        data_check_pass = uservalidatorO.validSignInPassword(password)
        connection = connDb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE email =%(email)s",
                     {'email': email})
        existance = curs.fetchall()
        curs.close()
        connection.close()

        if data_check_email and data_check_pass and existance:
            if check_password_hash(existance[0][4], password):
                access_token = create_access_token(existance[0][0])
                return access_token
            api.abort(401, error_messages[9]['invalid_password'])
        api.abort(404, error_messages[10]['not_signed_up'])

    @staticmethod
    def get_username(user_id):
        """method to return a users username given their id"""
        connection = connDb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE user_id = %(user_id)s",
                     {'user_id': user_id})
        known_user = curs.fetchone()
        
        return known_user[2]
        
    