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
    assert kit_response.json()["name"] == {'name': name}


def negative_assert(name):
    kit_body = get_kit_body(name)
    authToken = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)
    assert kit_response.status_code == 400


def test_create_kit_1_letters():
    positive_assert("a")


def test_create_kit_511_letters():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_0_letters():
    negative_assert("")


def test_create_kit_512_letters():
    negative_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_kit_eng_letters():
    positive_assert("QWErty")


def test_create_kit_rus_letters():
    positive_assert("Мария")


def test_create_kit_spec_symbols():
    positive_assert(""%@",")


def test_create_kit_space():
    positive_assert("Человек и КО")


def test_create_kit_nums():
    positive_assert("123")


def test_create_kit_empty():
    negative_assert(data.kit_body.pop("name"))






