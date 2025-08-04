class Url:
    HOST = "https://stellarburgers.nomoreparties.site/"

class UserAPI:
    AUTH_REG = "api/auth/register"
    AUTH_USER = "api/auth/user"
    AUTH_LOGIN = "api/auth/login"
    API_ORDERS = "api/orders"
    
class Parameters:
    HEADERS = {"Content-type": "application/json"}
    AUTH = {"authorization":""}

class StatusCode:
    OK_200 = 200
    FORBIDDEN_403 = 403
    UNAUTHORIZED_401 = 401
    BAD_REQUEST_400 = 400
    INTERNAL_SERVER_ERROR = 500

class MessageText:
    TRUE = True
    FALSE = False

class UserData:
    NEW_USER_WHITHOUT_EMAIL = {
        "email": "",
        "password": "123456!",
        "name": "Obi"
        }
 
class OrderData:
    ID_BUN_R2_D3 = "61c0c5a71d1f82001bdaaa6d"

    DATA_ORDER = {
            "ingredients": [ID_BUN_R2_D3]
        }
    
    EMPTY_DATA_ORDER = {
            "ingredients": []
        }
    
    INCORRECT_DATA_ORDER = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d9"]
        }
