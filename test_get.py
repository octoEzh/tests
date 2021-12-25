import requests
import json
import pytest

url = 'https://petstore.swagger.io/v2/user'


def base(**kwargs):
    with open(str(kwargs['json_file'])) as f:
        user = json.load(f)[str(kwargs['user'])]

        requests.post(url, json=user)

        obj_get = requests.get(f'{url}/{user["username"]}')
        assert obj_get.status_code == int(kwargs['get_status']), \
            f'ERROR GET: url {url}. \nUsername {user["username"]}. \nStatus error {obj_get.status_code}'


def base_positive(**kwargs):
    with open(str(kwargs['json_file'])) as f:
        user = json.load(f)[str(kwargs['user'])]

        obj_post = requests.post(url, json=user)

        obj_get = requests.get(f'{url}/{user["username"]}')
        assert obj_get.status_code == int(kwargs['get_status']), \
            f'ERROR GET: url {url}. \nUsername {user["username"]}. \nStatus error {obj_get.status_code}'

        assert str(obj_get.json()['id']) == str(obj_post.json()['message']), \
            f'get_id {obj_get.json()["id"]} != user_id {obj_post.json()["message"]}'

        for attribute in ['username', 'firstName', 'lastName', 'email', 'phone', 'userStatus']:
            assert str(obj_get.json()[attribute]) == str(user[attribute]), \
                f'obj_{attribute} {obj_get.json()[attribute]} != user_{attribute} {user[attribute]}'


# Positive cases
def test_get_user():
    base_positive(
        json_file='get_response.json',
        user='get_user',
        get_status=200
    )


# Negative cases
def test_get_user_with_int_username():
    base(
        json_file='get_response.json',
        user='get_user_with_int_username',
        get_status=404
    )


def test_get_user_with_null_username():
    base(
        json_file='get_response.json',
        user='get_user_with_null_username',
        get_status=404
    )


def test_get_user_with_empty_username():
    base(
        json_file='get_response.json',
        user='get_user_with_empty_username',
        get_status=405
    )


def test_get_user_with_boolean_username():
    base(
        json_file='get_response.json',
        user='get_user_with_boolean_username',
        get_status=404
    )


if __name__ == '__main__':
    test_get_user()
    test_get_user_with_int_username()
    test_get_user_with_empty_username()
    test_get_user_with_boolean_username()
    test_get_user_with_null_username()
    pass
