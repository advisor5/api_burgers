import allure
from src.data.constants import StatusCode
from src.user.routes import ApiLogin, ApiOrders


class TestRegisterUser:
    @allure.title("Тест получения заказов автризованного пользователя")
    @allure.description(
    "При успешном подключении бэкенд вернёт максимум\
        50 последних заказов пользователя")
    def test_get_orders_auth_user_return_200(self, register_rand_user):
        data_login = register_rand_user[1]
        access_token = register_rand_user[3]

        ApiLogin().auth_user(data_login)
        response = ApiOrders().get_orders_user(access_token)

        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title("Тест получения заказов неавторизованного пользователя")
    @allure.description(
    "ПЕсли выполнить запрос без авторизации, вернётся код ответа 401 Unauthorized")
    def test_get_orders_not_auth_user_return_401(self):

        access_token = None
        response = ApiOrders().get_orders_user(access_token)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")
