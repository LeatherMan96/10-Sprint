import requests
import configuration
import data


def post_new_user():
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return requests.post(url, json=data.user_body, headers=data.headers)


def post_new_client_kit(kit_body, authToken):
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    new_headers = data.headers.copy()
    new_headers['Authorization'] = f'Bearer {authToken}'
    return requests.post(url, json=body, headers=new_headers)

