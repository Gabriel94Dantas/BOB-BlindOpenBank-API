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


def balance_safra(client_json):
    """
        This method is the endpoint to return the balance of a client
    :param client_json: user_id, device_id, token
    :return: balance response
    """
    client_controller = ClientController()
    balance = client_controller.client_balance(client_json)
    if balance == constants.UNAUTHORIZED:
        response = {'status': constants.UNAUTHORIZED, 'response': 'Expired session'}
        return jsonify(response)
    response = {'status': constants.OK, 'response': balance}
    return jsonify(response)


def transactions_safra(client_json, day_before):
    client_controller = ClientController()
    if day_before:
        return
    transactions = client_controller.client_transactions(client_json)
    if transactions == constants.UNAUTHORIZED:
        response = {'status': constants.UNAUTHORIZED, 'response': 'Expired session'}
        return jsonify(response)
    response = {'status': constants.OK, 'response': transactions}
    return jsonify(response)
