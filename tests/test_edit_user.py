import allure
from src.user.routes import ApiUser, ApiLogin
from src.data.constants import StatusCode


class TestRegisterUser:
    @allure.title("Тест изменение логина пользователя с авторизацией")
    @allure.description(
        "Проверка: После изменение логина пользователя,\
            при запросе данных, возвращается измененный логин")
    def test_auth_edit_login_return_new_login(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]

        new_data = {
            "email": f"new_{data_login["email"]}"
        }
        
        ApiLogin().auth_user(data_login)
        response = ApiUser().patch_user(new_data, access_token)

        actually_value = response.json()["user"]["email"]
        expected_value = new_data["email"]
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        
    @allure.title("Тест изменение имени пользователя с авторизацией")
    @allure.description(
        "Проверка: После изменение имени пользователя, \
            при запросе данных, возвращается измененное имя")
    def test_auth_edit_login_return_new_name(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        user_data = register_rand_user[0]

        new_data = {
            "name": f"new_{user_data[2]}"
        }
        
        ApiLogin().auth_user(data_login)
        response = ApiUser().patch_user(new_data, access_token)

        actually_value = response.json()["user"]["name"]
        expected_value = new_data["name"]
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест изменение логина и имени пользователя с авторизацией")
    @allure.description(
        "Проверка: После изменение логина и имени пользователя, \
            при запросе данных, возвращается код 200")
    def test_auth_edit_login_and_name_return_200(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        user_data = register_rand_user[0]

        new_data = {
            "email": f"new_{user_data[1]}",
            "name": f"new_{user_data[2]}"
        }
        
        ApiLogin().auth_user(data_login)
        response = ApiUser().patch_user(new_data, access_token)

        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест изменение логина пользователя без авторизации")
    @allure.description(
    "Проверка: при запросе на изменени логина пользователя без авторизации, вернется код 401")
    def test_not_auth_edit_login_return_401(self, register_rand_user):

        data_user = register_rand_user[0]
        access_token = None
 
        new_data = {
            "name": f"new_{data_user[2]}"
        }
        
        response = ApiUser().patch_user(new_data, access_token)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
