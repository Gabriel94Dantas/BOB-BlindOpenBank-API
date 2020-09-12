"""
    This module is responsible to be the endpoints of bob
"""

from flask import jsonify
from app.controller.client import ClientController
from app.constants import constants


def login(client_json):
    """
        This method is the endpoint to login
    :param client_json: user_id, device_id
    :return: response
    """
    client_controller = ClientController()
    client_returned = client_controller.login_client(client_json)

    if client_returned == constants.NOT_FOUND:
        response = {'status': constants.NOT_FOUND, 'response': 'Not Found.'}
        return jsonify(response)
    response = {'status': constants.OK, 'response': client_returned}
    return jsonify(response)
