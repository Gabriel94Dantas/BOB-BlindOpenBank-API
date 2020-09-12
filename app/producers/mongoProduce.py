"""
    This module is responsible to create mongo connection
"""

import os
from pymongo import MongoClient


"""
    This class is responsible to create mongo connection
"""


class MongoConnectionFactory:
    MONGO_PORT = 27017
    MONGO_DB = os.getenv('MONGO_HOST', 'localhost')

    def get_connection(self):
        """
        This method is responsible to return a mongo connection instance
        :return: MongoClient
        """
        return MongoClient(self.MONGO_DB, self.MONGO_PORT, connect=False)
