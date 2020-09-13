"""
    The module responsible to initialize the Flask application
"""


from flask import Flask, request
app = Flask(__name__)
from app.view import bob
from app.util import header_to_client_json


@app.route('/login', methods=['POST'])
def login():
    """
        The method is responsible to be the route to login with BOB API
    """

    client_json = header_to_client_json.header_to_client_json(request.headers)
    client_json['password'] = request.get_json()['password']
    return bob.login(client_json)


@app.route('/balance', methods=['GET'])
def balance_safra():
    """
        The method is responsible to be the route to balance
    """
    client_json = header_to_client_json.header_to_client_json(request.headers)
    return bob.balance_safra(client_json)


@app.route('/transactions', methods=['GET'])
def transactions_safra():
    """
        The method is responsible to be the route to transactions
    """
    client_json = header_to_client_json.header_to_client_json(request.headers)
    return bob.transactions_safra(client_json=client_json)


@app.route('/morning-calls', methods=['GET'])
def morning_calls_safra():
    """
        The method is responsible to be the route to morning-calls
    """
    client_json = header_to_client_json.header_to_client_json(request.headers)
    return bob.morning_call_safra(client_json)


@app.route('/logs', methods=['GET'])
def bob_logs():
    """
        The method is responsible to be the route to logs
    """
    return bob.bob_logs()


if __name__ == '__main__':
    """
        The main method of application
    """
    app.run(host='0.0.0.0')
