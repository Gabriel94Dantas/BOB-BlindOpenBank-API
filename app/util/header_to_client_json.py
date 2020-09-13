

def header_to_client_json(header):
    """
    Convert header to client_json
    """
    client_json = {
        'user_id': header['UserId'],
        'device_id': header['DeviceId'],
        'token': header['SessionId']
    }
    return client_json
