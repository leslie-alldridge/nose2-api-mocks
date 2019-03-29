import requests
from env import token

USERS_URL = 'http://jsonplaceholder.typicode.com/users'
weather_url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=' + token
print(weather_url)


def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None


def get_user(user_id):
    """Get a single user using their ID"""
    all_users = get_users().json()
    for user in all_users:
        if user['id'] == user_id:
            return user


def get_api():
    response = requests.get(weather_url)
    if response.ok:
        print(response.json())
        return response
    else:
        return None


# commented out but can be used to run api call
# get_api()
