from app import api 
import re

"""
    Class to validate if the id entered is correct
"""

class IdDataValidator(object):
    def __init__(self,id_query):
        self.id_query=id_query

    """
        Method to validate the order ID entered by user if it is from 1 or more
    """
    
    def orderIdValid(self):
        if self.id_query == 0:
            api.abort(404, "Order id  :{} cannot be found, Orders are identified from 1 onwards".format(self.id_query))
        
        elif not re.match(r"(^[0-9]+$)",self.id_query):
            api.abort(404, "Order id  :{} cannot be found, Orders are identified from 1 onwards".format(self.id_query))
        
        return True