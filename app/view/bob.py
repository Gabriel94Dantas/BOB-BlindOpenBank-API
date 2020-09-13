"""
    This module is responsible to be the endpoints of bob
"""

from flask import jsonify
from app.controller.client import ClientController
from app.controller.bob_log import BobLogController
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


def transactions_safra(client_json):
    """
    This method is the endpoint to return the transactions of a client
    :param client_json: user_id, device_id, token
    :return: transactions response
    """
    client_controller = ClientController()
    transactions = client_controller.client_transactions(client_json)
    if transactions == constants.UNAUTHORIZED:
        response = {'status': constants.UNAUTHORIZED, 'response': 'Expired session'}
        return jsonify(response)
    response = {'status': constants.OK, 'response': transactions}
    return jsonify(response)


def morning_call_safra(client_json):
    """
    This method is the endpoint to return the morning call of a client
    :param client_json: user_id, device_id, token
    :return: morning call response
    """
    client_controller = ClientController()
    morning_calls = client_controller.client_morning_call(client_json)
    if morning_calls == constants.UNAUTHORIZED:
        response = {'status': constants.UNAUTHORIZED, 'response': 'Expired session'}
        return jsonify(response)
    response = {'status': constants.OK, 'audioURL': morning_calls['data'][1]['links'][1]['href']}
    return jsonify(response)


def bob_logs(adm_token):
    """
    This method is the endpoint to return the logs
    :return: JSON with all logs
    """
    bob_controller = BobLogController()
    bob_logs_json_array = bob_controller.find_all_bob_log(adm_token)
    if bob_logs_json_array == constants.NOT_FOUND:
        response = {'status': constants.NOT_FOUND, 'response': 'Not Found'}
        return jsonify(response)
    if bob_logs_json_array == constants.UNAUTHORIZED:
        response = {'status': constants.UNAUTHORIZED, 'response': 'Unauthorized'}
        return jsonify(response)
    response = {'status': constants.OK, 'response': bob_logs_json_array}
    return jsonify(response)
