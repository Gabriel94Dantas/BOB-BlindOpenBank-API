

def header_to_client_json(header):
    client_json = {
        'user_id': header['UserId'],
        'device_id': header['DeviceId'],
        'token': header['SessionId']
    }
    return client_json
