import requests
import json
import pytest

url = 'https://petstore.swagger.io/v2/user'


def base_get(**kwargs):
    user = kwargs['user']

    obj_get = requests.get(f'{url}/{user["username"]}')
    assert obj_get.status_code == int(kwargs['get_status']), \
        f'ERROR GET: url {url}. \nUsername {user["username"]}. \nStatus error {obj_get.status_code}'


def base_post_list(**kwargs):
    with open(str(kwargs['json_file'])) as f:
        user_list = json.load(f)[str(kwargs['user'])]

        obj_post = requests.post(f'{url}/createWithList', json=user_list)
        assert obj_post.status_code == kwargs['post_status'], \
            f'ERROR POST: url {url}.\nData {user_list}.\nStatus error {obj_post.status_code}'

        for idx, user in enumerate(user_list):
            base_get(
                user=user,
                get_status=kwargs['get_status'][idx]
                )


# Positive cases
def test_create_list_of_users():
    base_post_list(
        json_file='post_lists_response.json',
        user='create_list_of_users',
        post_status=200,
        get_status=[200, 200]
    )


def test_create_list_one_user():
    base_post_list(
        json_file='post_lists_response.json',
        user='create_list_one_user',
        post_status=200,
        get_status=[200]
    )


# Negative cases
def test_create_empty_list():
    base_post_list(
        json_file='post_lists_response.json',
        user='create_empty_list',
        post_status=400
    )


def test_create_list_of_users_with_error_user():
    base_post_list(
        json_file='post_lists_response.json',
        user='create_list_of_users_with_error_user',
        post_status=500,
        get_status=[404, 404]
    )


if __name__ == '__main__':
    test_create_list_of_users()
    test_create_list_one_user()
    # test_create_empty_list() 200
    # test_create_list_of_users_with_error_user() 500

    pass