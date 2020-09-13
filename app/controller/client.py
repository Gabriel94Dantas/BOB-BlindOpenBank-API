"""
    The module is responsible for control actions when the model domain will be a client
"""

from app.model.client import Client
from app.controller.bob_log import BobLogController
from app.util.date import current_time, add_minutes
from app.constants import constants
from app.view.safra import account_information, balance_safra, \
    transactions_safra, morning_calls_safra


"""
    The controller client class is responsible for control actions 
    when the model domain will be a client 
"""


class ClientController:
    client_class = Client()
    bob_controller = BobLogController()

    def find_client_by_user_device_id(self, client_json):
        """
        The method responsible to find client using the parameters: device_id, user_id and token
        :param client_json: device_id, user_id and token must be inside this JSON
        :return: HTTP status code 401 if the token was invalid and return client JSON if everything was ok
        """
        client = self.client_class.json_to_client(client_json)
        client_returned = self.client_class.find_client_by_user_device_id(client)
        if client_returned:
            if client_returned.token_date < current_time():
                return constants.UNAUTHORIZED
        else:
            if not client_returned:
                return constants.UNAUTHORIZED
        return self.client_class.client_to_json(client_returned)

    def login_client(self, client_json):
        """
        This method makes the login to happen, to do that, this method
        receives user_id and device_id, generates a token,
        and saves when this token will be invalid
        :param client_json: device_id and user_id must be inside this JSON
        :return: If the client doesn't exist in the database will return the HTTP 404 code,
            and if the client exists, the client
            and the account information will be returned
        """
        client = self.client_class.json_to_client(client_json)
        client_returned = self.client_class.find_client_login(client)
        if client_returned:
            client_returned.token = client.token
            client_returned.token_date = add_minutes(current_time(), 30)
            self.client_class.update_client(client_returned)
            client_returned = self.client_class.find_client_by_user_device_id(client_returned)
            result = [{
                'client_bob': self.client_class.client_to_json(client_returned),
                'account_info': account_information(client_returned.account_id)
            }]
            self.bob_controller.insert_bob_log(
                self.bob_controller.set_bob_log(
                    client_json, constants.LOGIN_OP, constants.LOGIN_DES))
            self.bob_controller.insert_bob_log(
                self.bob_controller.set_bob_log(
                    client_json, constants.ACCOUNT_OP, constants.ACCOUNT_DES))
            return result
        return constants.NOT_FOUND

    def client_balance(self, client_json):
        """
        This method returns the balance of a client if its token be valid
        :param client_json: user_id, device_id, token must be inside this JSON
        :return: balance or unauthorized HTTP code
        """
        client_returned = self.find_client_by_user_device_id(client_json)
        if client_returned == constants.UNAUTHORIZED:
            return client_returned
        self.bob_controller.insert_bob_log(
            self.bob_controller.set_bob_log(
                client_json, constants.BALANCE_OP, constants.BALANCE_DES))
        return balance_safra(client_returned['account_id'])

    def client_transactions(self, client_json):
        """
        This method returns the transactions of a client if its token be valid
        :param client_json: user_id, device_id, token must be inside this JSON
        :return: transactions or unauthorized HTTP code
        """
        client_returned = self.find_client_by_user_device_id(client_json)
        if client_returned == constants.UNAUTHORIZED:
            return client_returned
        self.bob_controller.insert_bob_log(
            self.bob_controller.set_bob_log(
                client_json, constants.TRANSACTIONS_OP, constants.TRANSACTIONS_DES))
        return transactions_safra(client_returned['account_id'])

    def client_morning_call(self, client_json):
        """
        This method returns the morning call of a client if its token be valid
        :param client_json: user_id, device_id, token must be inside this JSON
        :return: morning call or unauthorized HTTP code
        """
        client_returned = self.find_client_by_user_device_id(client_json)
        if client_returned == constants.UNAUTHORIZED:
            return client_returned
        self.bob_controller.insert_bob_log(
            self.bob_controller.set_bob_log(
                client_json, constants.MORNING_OP, constants.MORNING_DES))
        return morning_calls_safra()
