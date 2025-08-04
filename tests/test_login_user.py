import allure
from src.user.routes import ApiLogin
from src.data.constants import StatusCode


class TestRegisterUser:
    @allure.title("Тест получения кода 200, при авторизации текущего пользователя")
    @allure.description(
    "Проверка: логин под существующим пользователем, возвращается 200")
    def test_auth_current_user_return_200(self, register_rand_user):

        data_login = register_rand_user[1]
 
        response = ApiLogin().auth_user(data_login)

        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 401, при авторизации пользователя с неверным 'email'")
    @allure.description(
    "Проверка: авторизация с неверным 'email', возвращает 401")
    def test_auth_incorrect_email_return_401(self, register_rand_user):

        data_user = register_rand_user[0]
        data_login = {
            "email": f"{data_user[0]}1",
            "password": data_user[1]
        }

        response = ApiLogin().auth_user(data_login)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 401, при авторизации пользователя с неверным паролем")
    @allure.description(
    "Проверка: авторизация с неверным паролем, возвращает 401")
    def test_incorrect_pass_return_401(self, register_rand_user):

        data_user = register_rand_user[0]
        data_login = {
            "email": {data_user[0]},
            "password": f"{data_user[1]}1"
        }
  
        response = ApiLogin().auth_user(data_login)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 401, при авторизации пользователя с без поля 'email'")
    @allure.description(
    "Проверка: авторизация без поля 'email', возвращает 401")
    def test_without_email_return_401(self, register_rand_user):

        data_user = register_rand_user[0]
        data_login = {
            "email": "",
            "password": f"{data_user[1]}1"
        }
  
        response = ApiLogin().auth_user(data_login)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 401, при авторизации пользователя без пароля")
    @allure.description(
    "Проверка: авторизация без пароля, возвращает 401")
    def test_without_pass_return_401(self, register_rand_user):

        data_user = register_rand_user[0]
        data_login = {
            "email": {data_user[0]},
            "password": ""
        }

        response = ApiLogin().auth_user(data_login)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
