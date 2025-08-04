import allure
from src.user.routes import ApiUser, ApiRegister
from src.data.constants import StatusCode


class TestRegisterUser:
    @allure.title("Тест получения кода 2000 при успешной регистрации нового пользователя")
    @allure.description(
    "Проверка: успешноое создание уникального пользователя и возвращение кода 200")
    
    def test_register_new_user_return_200(self, generate_new_user):
        
        new_user = generate_new_user
        response = ApiRegister().reg_user(new_user)
        access_token = response.json()['accessToken']

        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

        ApiUser().delete_user(access_token)

    @allure.title("Тест регистрации существующего пользователя")
    @allure.description("Проверка: создать пользователя, который уже зарегистрирован")
    def test_register_existing_user_return_403(self, generate_new_user):

        new_user = generate_new_user
        response_first = ApiRegister().reg_user(new_user)
        access_token = response_first.json()['accessToken']
        response_second = ApiRegister().reg_user(new_user)

        actually_value = response_second.status_code
        expected_value = StatusCode.FORBIDDEN_403
        assert actually_value == expected_value
        allure.attach(f"Status {response_second.status_code}", "Response status")

        ApiUser().delete_user(access_token)
    
    @allure.title("Тест регистрации пользователя без заполненного поля email")
    @allure.description(
        "Проверка: создать пользователя и не заполнить обязательное поле emmail"
    )
    def test_register_user_without_email_return_403(self):
        
        new_user_without_email ={
            "email": "",
            "password": "123456!",
            "name": "Obi"
        }
        
        response = ApiRegister().reg_user(new_user_without_email)

        actually_value = response.status_code
        expected_value = StatusCode.FORBIDDEN_403
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест регистрации пользователя без заполненного поля password")
    @allure.description(
        "Проверка: создать пользователя и не заполнить обязательное поле password,\
            вернется коды 403"
        )
    def test_register_user_without_pass_return_403(self, generate_random_string):
        
        data = {
            "email": f"{generate_random_string}@yandex.ru",
            "password": "",
            "name": "Obi"
        }
        
        response = ApiRegister().reg_user(data)

        actually_value = response.status_code
        expected_value = StatusCode.FORBIDDEN_403
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
