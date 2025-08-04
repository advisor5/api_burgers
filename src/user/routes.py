import allure
import requests
from src.data.constants import Url, UserAPI, Parameters


class ApiRegister:

    @allure.step("POST запрос на ручку 'api/auth/register' - регистрация пользователя")
    def reg_user(self, data):
        return requests.post(f"{Url.HOST}{UserAPI.AUTH_REG}", data=data)

class ApiUser:

    @allure.step("DELETE запрос на ручку 'api/auth/user' - удаление пользователя")    
    def delete_user(self, access_token):
        headers = Parameters.HEADERS
        headers["authorization"] = access_token
        return requests.delete(f"{Url.HOST}{UserAPI.AUTH_USER}", headers=headers)
    
    @allure.step("PATCH запрос на ручку 'api/auth/user' - изменение данных пользователя")    
    def patch_user(self, data, access_token):
        headers = Parameters.AUTH
        headers["authorization"] = access_token
        return requests.patch(f"{Url.HOST}{UserAPI.AUTH_USER}", data, headers=headers)

class ApiLogin:

    @allure.step("POST запрос на ручку 'api/auth/login' - авторизация пользователя")    
    def auth_user(self, data):
        return requests.post(f"{Url.HOST}{UserAPI.AUTH_LOGIN}", data)

class ApiOrders:

    @allure.step("POST запрос на ручку 'api/orders' - создание заказа")    
    def create_orders(self, data, access_token):
        headers = Parameters.AUTH
        headers["authorization"] = access_token 
        return requests.post(f"{Url.HOST}{UserAPI.API_ORDERS}", data, headers=headers)
    
    @allure.step("GET запрос на ручку 'api/orders' - получение заказов пользователя")    
    def get_orders_user(self, access_token):
        headers = Parameters.AUTH
        headers["authorization"] = access_token
        return requests.get(f"{Url.HOST}{UserAPI.API_ORDERS}", headers=headers)
    