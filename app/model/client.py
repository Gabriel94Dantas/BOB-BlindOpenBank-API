"""
    The module is responsible to create clients objects
    like a model domain
"""

from app.producers.mongoProduce import MongoConnectionFactory
from pymongo.errors import PyMongoError

"""
    The module is responsible to create clients objects
    like a model domain
"""


class Client:
    device_id = None
    user_id = None
    token = None
    token_date = None
    panic_password = None
    account_id = None
    password = None
    mongo_connection_factory = MongoConnectionFactory()

    def insert_client(self, client):
        """
        This method inserts a client on the database.
        :param client:
        :return: None
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            client_json = self.client_to_json(client)
            db_client['bob']['clients'].insert_one(client_json)
        except PyMongoError as error:
            print("Error while inserting a client.", error)
        finally:
            db_client.close()

    def find_client_by_user_device_id(self, client):
        """
        This method has to find a client using user_id, device_id, and token
        :param client: user_id, device_id, and token must be on the object
        :return: Client object
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            query = {
                'user_id': client.user_id,
                'device_id': client.device_id,
                'token': client.token
            }
            result = db_client['bob']['clients'].find(query)
            if result:
                for client_json in result:
                    client_returned = self.json_to_client(client_json)
                    return client_returned
            return
        except PyMongoError as error:
            print("Error while finding a client.", error)
        finally:
            db_client.close()

    def find_client_login(self, client):
        """
            This method has to find a client using user_id and device_id
            :param client: user_id and device_id must be on the object
            :return: Client object
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            query = {
                'user_id': client.user_id,
                'device_id': client.device_id,
                'password': client.password
            }
            result = db_client['bob']['clients'].find(query)
            if result:
                for client_json in result:
                    client_returned = self.json_to_client(client_json)
                    return client_returned
            return
        except PyMongoError as error:
            print("Error while finding a client.", error)
        finally:
            db_client.close()

    def update_client(self, client):
        """
            This method has to find a client using user_id, device_id, and token
            :param client: user_id, device_id, and token must be on the object
            :return: Client object
        """
        db_client = None
        try:
            db_client = self.mongo_connection_factory.get_connection()
            query = {
                'user_id': client.user_id,
                'device_id': client.device_id
            }
            new_values = {
                "$set": {
                    'token': client.token,
                    'token_date': client.token_date
                }
            }
            db_client['bob']['clients'].update_one(query, new_values)
        except PyMongoError as error:
            print("Error while updating a client.", error)
        finally:
            db_client.close()

    def client_to_json(self, client):
        """
            The method is responsible to convert the class object
            to JSON
        :param client: client object
        :return: client_json
        """
        client_json = {
            'device_id': client.device_id,
            'user_id': client.user_id,
            'token': client.token,
            'token_date': client.token_date,
            'panic_password': client.panic_password,
            'account_id': client.account_id,
            'password': client.password
        }

        return client_json

    def json_to_client(self, client_json):
        """
            The method is responsible to convert the JSON
            to client object
        :param client_json: client into JSON mode
        :return: client object
        """
        client = Client()
        if 'device_id' in client_json:
            client.device_id = client_json['device_id']
        if 'user_id' in client_json:
            client.user_id = client_json['user_id']
        if 'token' in client_json:
            client.token = client_json['token']
        if 'token_date' in client_json:
            client.token_date = client_json['token_date']
        if 'panic_password' in client_json:
            client.panic_password = client_json['panic_password']
        if 'account_id' in client_json:
            client.account_id = client_json['account_id']
        if 'password' in client_json:
            client.password = client_json['password']
        return client
