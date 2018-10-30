""" module to handle siging up, and loging in user to db """
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask import jsonify


# local imports
from app import API
from app.api.utility.valid_user import UserAuthValidator
from app.api.v2.db.conndb import connectdb
from app.api.utility.messages import success_messages, error_messages


""" instance of validation classes"""
uservalidatoro = UserAuthValidator()


class ManageUserDAO():
    """Class to manage operations on a user"""

    def __init__(self, email, username, password, confirm_password):
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    def check_user_existance(self,email):
        """Method to check if user exists
        Check if a matching email exists in the DataBase"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE email = %(email)s",
                     {'email': email})
        existing_user = curs.fetchall()
        curs.close()
        connection.close()

        return existing_user

    def SignUpNewUser(self):
        """Method to validated user, and add to the database
            If all checks have passed add the user"""
        data_check_email = uservalidatoro.validEmail(self.email)
        data_check_pass = uservalidatoro.validPasswd(
            self.password, self.confirm_password)
        data_check_uname = uservalidatoro.validUsername(self.username)
        if self.username == os.getenv('PRIV'):
            user_priv = True
        else:
            user_priv = False

        if data_check_email & data_check_pass & data_check_uname:

            if self.check_user_existance(self.email.lower()):
                API.abort(
                    409, error_messages[0]['email_conflict'])

            connection = connectdb()
            curs = connection.cursor()

            self.passwd_hash = generate_password_hash(self.password)

            curs.execute("INSERT INTO users (email,username,priv,password)" +
                         "VALUES(%s,%s,%s,%s)",
                         (self.email.lower(),self.username, user_priv, self.passwd_hash))

            curs.close()
            connection.commit()
            connection.close()
            return success_messages[0]['account_created'], 201
        API.abort(500, error_messages[1]['validation_error'])

    @staticmethod
    def loginUser(email, password):
        """Method to validata user on login and checking if they exist
        if they do it compares the password hashes
        if this pasess it create user access token"""
        data_check_email = uservalidatoro.validEmail(email)
        data_check_pass = uservalidatoro.validSignInPassword(password)
        
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE email =%(email)s",
                     {'email': email.lower()})
        existance = curs.fetchall()
        curs.close()
        connection.close()

        if data_check_email and data_check_pass and existance:
            if check_password_hash(existance[0][4], password):
                access_token = create_access_token(existance[0][0])
                return {"Mesaage":"Login Successful","Token": access_token}
                
            API.abort(403, error_messages[9]['invalid_password'])
        API.abort(401, error_messages[10]['not_signed_up'])

    @staticmethod
    def get_username(user_id):
        """method to return a users username given their id"""
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE user_id = %(user_id)s",
                     {'user_id': user_id})
        known_user = curs.fetchone()

        return known_user[2]

    @staticmethod
    def normal_user_only(username):
        connection = connectdb()
        curs = connection.cursor()
        curs.execute("SELECT * FROM users WHERE username=%(username)s",
                     {'username': username})
        user_exixtance = curs.fetchone()
        if user_exixtance[3]:
            API.abort(403, error_messages[19]['unmet_priv'])
    
    @staticmethod
    def user_logout(user_token):
        # user_token = str(user_token)
        connection = connectdb()
        curs =  connection.cursor()
        curs.execute("INSERT INTO logout (user_token) VALUES (%s)",(user_token,))
        curs.close()
        connection.commit()
        connection.close()
        return {"message": "Successfully logged out"}, 200

    @staticmethod
    def fetch_blacklisted_token(user_token):
        connection = connectdb()
        curs =  connection.cursor()
        curs.execute("SELECT * FROM logout WHERE user_token = %(user_token)s",
        {'user_token': user_token})
        known_token = curs.fetchone()
        curs.close()
        connection.close()
        return known_token


