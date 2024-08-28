import allure

from http_methods import HttpMethods


class API:
    base_url = 'https://jsonplaceholder.typicode.com'

    @staticmethod
    def get_posts_1(set_id):
        get_resource = f'/posts/{set_id}'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_posts_all():
        get_resource = f'/posts'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step('Endpoint: /posts'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def post_creating_resource(body: dict):
        post_resource = f'/posts'
        url = API.base_url + post_resource
        response = HttpMethods.post(url=url, body=body)
        with allure.step('Endpoint: /posts'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {body}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def put_updating_resource(body: dict, set_id):
        put_resource = f'/posts/{set_id}'
        url = API.base_url + put_resource
        response = HttpMethods.put(url=url, body=body)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {body}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def patch_updating_resource(body: dict, set_id):
        patch_resource = f'/posts/{set_id}'
        url = API.base_url + patch_resource
        response = HttpMethods.patch(url=url, body=body)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {body}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def delete_resource(set_id):
        delete_resource = f'/posts/{set_id}'
        url = API.base_url + delete_resource
        response = HttpMethods.delete(url=url)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_comments(set_id):
        get_resource = f'/posts/{set_id}/comments'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /posts/{set_id}/comments'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_albums_photo(set_id):
        get_resource = f'/albums/{set_id}/photos'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /albums/{set_id}/photo'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_users_albums(set_id):
        get_resource = f'/users/{set_id}/albums'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /users/{set_id}/albums'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_users_todos(set_id):
        get_resource = f'/users/{set_id}/todos'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /users/{set_id}/todos'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_users_posts(set_id):
        get_resource = f'/users/{set_id}/posts'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /users/{set_id}/posts'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response