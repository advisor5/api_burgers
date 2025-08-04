import pytest 
import random
import string
from src.data.constants import UserData
from src.user.routes import ApiRegister, ApiUser


@pytest.fixture
def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string

@pytest.fixture
def generate_new_user(generate_random_string):
        new_user = UserData.NEW_USER_WHITHOUT_EMAIL
        new_user["email"] = f"{generate_random_string}@yandex.ru"
        return new_user

@pytest.fixture
def register_rand_user(generate_new_user):
    payload = generate_new_user
    response = ApiRegister().reg_user(payload)
    access_token = response.json()["accessToken"]

    data_user = []
    data_user.append(generate_new_user["email"])
    data_user.append(generate_new_user["password"])
    data_user.append(generate_new_user["name"])

    data_login = {
    "email": data_user[0],
    "password": data_user[1]
    }

    yield data_user, data_login, response, access_token 

    ApiUser().delete_user(access_token)
