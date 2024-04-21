import data
import sender_stand_request


def get_new_user_token():
    response = sender_stand_request.post_new_user()
    return response.json()["authToken"]


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    authToken = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_create_kit_1_letter():
    positive_assert("a")
