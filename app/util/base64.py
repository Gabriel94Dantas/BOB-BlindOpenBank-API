"""
    This module is responsible to encode and decode base64
"""

import base64


def encode(msg):
    """
    This method encodes a message into base64
    :param msg: Anyone string
    :return: base64 encoded string
    """
    msg_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    return base64_bytes.decode('ascii')


def decode(base64_msg):
    """
    this method decodes a base64 message
    :param base64_msg: base64 string
    :return: Original message
    """
    base64_bytes = base64_msg.encode('ascii')
    msg_bytes = base64.b64decode(base64_bytes)
    return msg_bytes.decode('ascii')

