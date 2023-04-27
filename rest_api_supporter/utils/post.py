import requests

def post(url, json=None, data=None, headers=None, timeout=60, return_json=True):
    response = requests.post(url, json=json, data=data, headers=headers, timeout=timeout)
    if return_json:
        response = response.json()
    return response
