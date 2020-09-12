"""
    This module is responsible to consume Safra API
"""

import requests
import json
from app.constants import constants
from app.util.base64 import encode


def token_generator():
    """
        This method generates the access token to access Safra API
    :return: access_token
    """
    key = constants.CLIENT_ID + ':' + constants.SECRET_KEY
    key_base64 = encode(key)
    key_base64 = 'Basic ' + key_base64
    header = {
        'authorization': key_base64,
        'content-type': 'application/x-www-form-urlencoded'
    }
    body = "grant_type=client_credentials&scope=urn:opc:resource:consumer::all"
    response = requests.post(url=constants.AUTH_URL, headers=header, data=body)
    response_json = json.loads(response.content.decode('ascii'))
    return response_json['access_token']


def account_information(account_id):
    """
        This method returns Safra's client account information
    :param account_id:
    :return: Safra's client account information
    """
    url = constants.API_SF_URL+constants.OPEN_BANK_ACCOUNT+str(account_id)
    token = 'Bearer ' + token_generator()
    header = {
        'Authorization': token
    }
    response = requests.get(url=url, headers=header)
    return json.loads(response.content.decode('ascii'))


def balance_safra(account_id):
    """
        This method returns Safra's client balance
    :param account_id
    :return: Safra's client balance information
    """
    url = constants.API_SF_URL + constants.OPEN_BANK_ACCOUNT + \
        str(account_id) + constants.BALANCE_LINK
    token = 'Bearer ' + token_generator()
    header = {
        'Authorization': token
    }
    response = requests.get(url=url, headers=header)
    return json.loads(response.content.decode('ascii'))


def transactions_safra(account_id):
    """
            This method returns Safra's client transactions
        :param account_id
        :return: Safra's client transactions information
        """
    url = constants.API_SF_URL + constants.OPEN_BANK_ACCOUNT + \
        str(account_id) + constants.TRANSACTIONS_LINK
    token = 'Bearer ' + token_generator()
    header = {
        'Authorization': token
    }
    response = requests.get(url=url, headers=header)
    return json.loads(response.content.decode('ascii'))


def transactions_days_before_safra(client_json, days_before):
    return client_json
