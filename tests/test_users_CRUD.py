import pytest
from faker import Faker
from utils.api_requests import create_user, get_user, update_user, delete_user

@pytest.fixture(scope="module")
def setup():
    # Setup code if needed
    yield
    # Teardown code if needed

def test_user_CRUD(setup):
    fake = Faker()

    # Generate a random email address
    email = fake.email()

    # Create a user
    create_data = {"name": "Tenali Ramakrishna", "gender": "male", "email": email, "status": "active"}
    create_response = create_user(create_data)
    print("Create User Response:", create_response.json())  # Print the response
    assert create_response.status_code == 201

    # Retrieve the user ID from the response
    user_id = create_response.json()["id"]

    # Read the created user
    read_response = get_user(user_id)
    print("Get User Response:", read_response.json())  # Print the response
    assert read_response.status_code == 200
    assert read_response.json()["name"] == create_data["name"]
    assert read_response.json()["email"] == create_data["email"]

    # Update the user
    update_data = {"name": "Tenali Ramakrishna", "email": fake.email()}
    update_response = update_user(user_id, update_data)
    print("Update User Response:", update_response.json())  # Print the response
    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_data["name"]
    assert update_response.json()["email"] == update_data["email"]

    # Delete the user
    delete_response = delete_user(user_id)
    print("Delete User Response:", delete_response.text)  # Print the response
    assert delete_response.status_code == 204