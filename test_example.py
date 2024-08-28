import allure

from checking import Checking
from request import API


@allure.epic('Test Api.')
class TestApi:
    @allure.title('test_posts_1')
    def test_posts_1(self):
        response = API.get_posts_1(1)
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'id', 1)
        Checking.check_json_value(response, 'userId', 1)

    @allure.title('test_posts_all')
    def test_posts_all(self):
        response = API.get_posts_all()
        Checking.check_status_code(response, 200)
        Checking.check_json_many_keys(response, 0, ['userId', 'id', 'title', 'body'])

    @allure.title('test_post_creating_resource')
    def test_post_creating_resource(self):
        body = {'title': 'foo',
                'body': 'bar',
                'userId': 1}
        response = API.post_creating_resource(body=body)
        Checking.check_status_code(response, 201)
        Checking.check_json_keys(response, ['title', 'body', 'userId', 'id'])
        Checking.check_json_value(response, 'title', body['title'])
        Checking.check_json_value(response, 'body', body['body'])
        Checking.check_json_value(response, 'userId', body['userId'])

    @allure.title('test_updating_resource')
    def test_updating_resource(self):
        set_id = 1
        body = {'id': set_id,
                'title': 'foo',
                'body': 'bar',
                'userId': 1}
        response = API.put_updating_resource(
            body=body,
            set_id=set_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'id', set_id)

    @allure.title('test_patch_updating_resource')
    def test_patch_updating_resource(self):
        set_id = 1
        body = {'title': 'lambotik'}
        response = API.patch_updating_resource(
            body=body,
            set_id=set_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'title', body['title'])
        Checking.check_json_keys(response, ['id', 'title', 'body', 'userId'])

    @allure.title('test_delete_resource')
    def test_delete_resource(self):
        set_id = 1
        response = API.delete_resource(set_id=set_id)
        Checking.check_status_code(response, 200)
        assert response.text == '{}'

    @allure.title('test_get_comments')
    def test_get_comments(self):
        set_id = 1
        response = API.get_comments(set_id=set_id)
        Checking.check_status_code(response, 200)

    @allure.title('test_get_albums_photo')
    def test_get_albums_photo(self):
        set_id = 1
        response = API.get_albums_photo(set_id=set_id)
        Checking.check_status_code(response, 200)

    @allure.title('test_get_albums_photo')
    def test_get_users_albums(self):
        set_id = 1
        response = API.get_users_albums(set_id=set_id)
        Checking.check_status_code(response, 200)

    @allure.title('test_get_users_todos')
    def test_get_users_todos(self):
        set_id = 1
        response = API.get_users_todos(set_id=set_id)
        Checking.check_status_code(response, 200)

    @allure.title('test_get_users_posts')
    def test_get_users_posts(self):
        set_id = 1
        response = API.get_users_posts(set_id=set_id)
        Checking.check_status_code(response, 200)