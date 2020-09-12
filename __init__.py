"""
    The module responsible to initialize the Flask application
"""


from flask import Flask, request
app = Flask(__name__)
from app.view import bob


@app.route('/login', methods=['POST'])
def login():
    """
        The method responsible to be the route to login with BOB API
    """
    client_json = request.get_json()
    return bob.login(client_json)


if __name__ == '__main__':
    """
        The main method of application
    """
    app.run(host='0.0.0.0')
