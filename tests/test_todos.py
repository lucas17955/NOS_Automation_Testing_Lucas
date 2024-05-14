import jsonschema #this library is to validate the schema
import pytest #this library is for tests in python
import allure #for report
from utils.api_requests import get_todos
from utils.response_validator import validate_response_schema # fuction to validate schema
from utils.allure_helper import attach_response_data #function to attach the response to the allure report

@pytest.fixture(scope="module")
def setup():
    # Setup code 
    yield
    # Teardown code 

def test_get_todos(setup):
    with allure.step("Send GET request to retrieve todos"):
        response = get_todos()

        # Attach the response data to the test step
        attach_response_data(response)

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Verify response schema"):
        # Define the expected schema for the response
        expected_schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "user_id": {"type": "integer"},
                    "title": {"type": "string"},
                    "due_on": {"type": "string", "format": "date-time"},
                    "status": {"type": "string"}
                },
                "required": ["id", "user_id", "title", "due_on", "status"]
            }
        }

        # Validate the response against the expected schema
        validate_response_schema(response, expected_schema)

        with allure.step("Verify all status fields are 'completed'"):
        # Get the JSON response data
            response_data = response.json()

        # Check if all status fields are 'completed'
            for item in response_data:
                assert item['status'] == 'completed'