import requests

def get(url, json=None, data=None, headers=None, timeout=60, return_json=True):
    response = requests.get(url, json=json, data=data, headers=headers, timeout=timeout)
    if return_json:
        response = response.json()
    return response
