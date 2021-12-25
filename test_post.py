import requests
import json
import pytest

url = 'https://petstore.swagger.io/v2/user'


def base(**kwargs):
    with open(str(kwargs['json_file'])) as f:
        user = json.load(f)[str(kwargs['user'])]

        obj_post = requests.post(url, json=user)
        assert obj_post.status_code == int(kwargs['post_status']), \
            f'ERROR POST: url {url}.\nData {user}.\nStatus error {obj_post.status_code}'

        obj_get = requests.get(f'{url}/{user["username"]}')
        assert obj_get.status_code == int(kwargs['get_status']), \
            f'ERROR GET: url {url}. \nUsername {user["username"]}. \nStatus error {obj_get.status_code}'


# POST REQUESTS
def test_create_user():
    base(
        json_file='post_response.json',
        user='create_user',
        post_status=200,
        get_status=200
    )


def test_create_user_null():
    base(
        json_file='post_response.json',
        user='create_user_null',
        post_status=500,
        get_status=404
    )


def test_create_user_id_str():
    base(
        json_file='post_response.json',
        user='create_user_id_str',
        post_status=500,
        get_status=404
    )


def test_create_user_id_minus():
    base(
        json_file='post_response.json',
        user='create_user_id_minus',
        post_status=500,
        get_status=404
    )


def test_create_user_all_info_int():
    base(
        json_file='post_response.json',
        user='create_user_all_info_int',
        post_status=500,
        get_status=404
    )


def test_create_user_more_then_limit_user_status():
    base(
        json_file='post_response.json',
        user='create_user_more_then_limit_userStatus',
        post_status=500,
        get_status=404
    )


def test_create_user_boolean_id():
    base(
        json_file='post_response.json',
        user='create_user_boolean_id',
        post_status=500,
        get_status=404
    )


def test_create_user_boolean_user_status():
    base(
        json_file='post_response.json',
        user='create_user_boolean_userStatus',
        post_status=500,
        get_status=404
    )


def test_create_user_empty_username():
    base(
        json_file='post_response.json',
        user='create_user_empty_username',
        post_status=400,
        get_status=404
    )


def test_create_user_only_username():
    base(
        json_file='post_response.json',
        user='create_user_only_username',
        post_status=400,
        get_status=404
    )


if __name__ == '__main__':
    test_create_user()
    # test_create_user_null()
    # test_create_user_id_str()
    # test_create_user_all_info_int()
    # test_create_user_more_then_limit_user_status()
    # test_create_user_boolean_id()
    # test_create_user_boolean_userStatus()
    # test_create_user_empty_username()
    # test_create_user_only_username()
    # pass