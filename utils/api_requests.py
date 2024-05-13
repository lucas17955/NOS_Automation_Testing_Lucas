import requests
from .config import BASE_URL, AUTH_TOKEN

def get_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json"
    }
    return requests.get(url, headers=headers)

def create_user(data):
    url = f"{BASE_URL}/users"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return requests.post(url, json=data, headers=headers)

def update_user(user_id, data):
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return requests.put(url, json=data, headers=headers)

def delete_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json"
    }
    return requests.delete(url, headers=headers)

def get_todos():
    url = f"{BASE_URL}/todos"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return requests.get(url, headers=headers)