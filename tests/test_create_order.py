import allure
from src.data.constants import StatusCode, MessageText, OrderData
from src.user.routes import ApiLogin, ApiOrders


class TestRegisterUser:
    @allure.title("Тест возвращения сообщения при успешном создании заказа с авторизацией")
    @allure.description(
        "Проверка: при создании заказа с авторизацией в теле ответа вернется 'success: true'"
    )
    def test_auth_user_create_order_return_success_true(self, register_rand_user):
        
        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        data_order = OrderData.DATA_ORDER
        
        ApiLogin().auth_user(data_login)
        response = ApiOrders().create_orders(data_order, access_token)
        
        actually_value = response.json()["success"]
        print(actually_value)
        expected_value = MessageText.TRUE
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title("Тест возвращения кода 200 при успешном создании заказа с авторизацией")
    @allure.description(
        "Проверка: при создании заказа с авторизацией в теле ответа вернется 200"
    )
    def test_auth_user_create_order_return_200(self, register_rand_user):
        
        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        data_order = OrderData.DATA_ORDER
        
        response = ApiLogin().auth_user(data_login)
        response_add = ApiOrders().create_orders(data_order, access_token)
        
        actually_value = response_add.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title("Тест создания заказа без авторизации")
    @allure.description(
        "Проверка: при создании заказа без авторизаци в теле ответа вернется 'success: false'"
    )
    def test_not_auth_user_create_order_return_success_false(self, register_rand_user):

        access_token = register_rand_user[3]

        data_order = OrderData.DATA_ORDER
        response = ApiOrders().create_orders(data_order, access_token)

        actually_value = response.json()["success"]
        expected_value = MessageText.FALSE
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title("Тест создания заказа c ингредиентами авторизованным пользователем")
    @allure.description(
        "Проверка: при создании заказа с ингредиентами, \
            авторизованным пользователем, в ответе содержится id ингредиента"
        )
    def test_auth_user_create_order_return_id_ingredient(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        data_order = OrderData.DATA_ORDER

        ApiLogin().auth_user(data_login)
        response = ApiOrders().create_orders(data_order, access_token)

        actually_value = str(response.json())
        expected_value = OrderData.ID_BUN_R2_D3
        assert expected_value in actually_value  
        
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title(
            "Тест получения ошибки, при создании заказа без ингредиентов \
                авторизованным пользователем")
    @allure.description(
        "Если не передать ни один ингредиент, вернётся код ответа 400 Bad Request"
    )
    def test_auth_user_create_order_without_ingredient_return_400(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        data_order = OrderData.EMPTY_DATA_ORDER

        ApiLogin().auth_user(data_login)
        response = ApiOrders().create_orders(data_order, access_token)

        actually_value = response.status_code
        expected_value = StatusCode.BAD_REQUEST_400
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")

    @allure.title("Тест получения ошибки, при создании заказа с неверным хешем ингредиентов")
    @allure.description(
        "Если не передать неверный хеш ингредиентов, \
        вернётся код ответа 500 Internal Server Error"
    )
    def test_auth_user_create_order_with_incorrect_hash_return_500(self, register_rand_user):

        data_login = register_rand_user[1]
        access_token = register_rand_user[3]
        data_order = OrderData.INCORRECT_DATA_ORDER

        ApiLogin().auth_user(data_login)
        response = ApiOrders().create_orders(data_order, access_token)

        actually_value = response.status_code
        expected_value = StatusCode.INTERNAL_SERVER_ERROR
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
