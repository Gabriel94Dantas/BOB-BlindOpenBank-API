"""
    This module is responsible to create bob_log objects
    like a model domain
"""

from app.producers.mongoProduce import MongoConnectionFactory
from pymongo.errors import PyMongoError

"""
    This class is responsible to create bob_log objects 
    like a model domain
"""


class BobLog:
    operation_type = None
    description = None
    device_id = None
    user_id = None
    operation_time = None
    mongo_connection_factory = MongoConnectionFactory()

    def insert_bob_log(self, bob_log):
        """
        This method is responsible to insert bob_log
        into Mongo database.
        :param bob_log:
        :return: None
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            bob_log_json = self.bob_log_to_json(bob_log)
            db_client['bob']['logs'].insert_one(bob_log_json)
        except PyMongoError as error:
            print("Error while inserting bob log.", error)
        finally:
            db_client.close()

    def find_all(self):
        """
        This method is responsible to find all bob_log
        into Mongo database.
        :param: None
        :return: bob_log list
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            result = db_client['bob']['logs'].find()
            bob_logs = []
            if result:
                for bob_log_json in result:
                    bob_log = self.json_to_bob_log(bob_log_json)
                    bob_logs.append(bob_log)
            return bob_logs
        except PyMongoError as error:
            print("Error while finding bob log find all.", error)
        finally:
            db_client.close()

    def bob_log_to_json(self, bob_log):
        """
        This method is responsible to convert
        bob_log object to JSON
        :param bob_log:
        :return: bob_log_json
        """
        bob_log_json = {}
        if bob_log:
            if bob_log.operation_type:
                bob_log_json['operation_type'] = bob_log.operation_type
            if bob_log.description:
                bob_log_json['description'] = bob_log.description
            if bob_log.device_id:
                bob_log_json['device_id'] = bob_log.device_id
            if bob_log.user_id:
                bob_log_json['user_id'] = bob_log.user_id
            if bob_log.operation_time:
                bob_log_json['operation_time'] = bob_log.operation_time
        return bob_log_json

    def json_to_bob_log(self, bob_log_json):
        """
        This method is responsible to convert JSON into
        bob_log object
        :param bob_log_json:
        :return: bob_log
        """
        bob_log = BobLog()
        if 'operation_type' in bob_log_json:
            bob_log.operation_type = bob_log_json['operation_type']
        if 'description' in bob_log_json:
            bob_log.description = bob_log_json['description']
        if 'device_id' in bob_log_json:
            bob_log.device_id = bob_log_json['device_id']
        if 'user_id' in bob_log_json:
            bob_log.user_id = bob_log_json['user_id']
        if 'operation_time' in bob_log_json:
            bob_log.operation_time = bob_log_json['operation_time']
        return bob_log