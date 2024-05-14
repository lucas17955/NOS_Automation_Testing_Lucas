from datetime import datetime
import pytz #library for timezone test
import pytest #library for tests in python
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
        try:
            validate_response_schema(response, expected_schema)
        except AssertionError as e:
            assert False, str(e)

        with allure.step("Verify all status fields are 'completed'"):
        # Get the JSON response data
            response_data = response.json()

        # Check if all status fields are 'completed'
        for item in response_data:
            try:
                assert item['status'] == 'completed', f"Status is not completed: {item['status']}"
            except AssertionError as e:
                assert False, str(e)
        
    with allure.step("Interpret and validate the 'due_on' value"):
        # Check if the 'due_on' value is in ISO 8601 format and in the future
        current_time = datetime.now(pytz.utc)  # Get current UTC time
        for item in response_data:
            due_on = item['due_on']
            try:
                # Parse the due_on value
                due_date = datetime.fromisoformat(due_on.replace('Z', '+00:00'))

                # Ensure the due_date is timezone-aware
                try:
                    assert due_date.tzinfo is not None, f"Due date '{due_on}' is offset-naive"
                except AssertionError as e:
                    assert False, str(e)

                # Compare the due_date with the current time
                try:
                    assert due_date > current_time, f"Due date '{due_on}' is in the past"
                except AssertionError as e:
                    assert False, str(e)
            except ValueError:
                assert False, f"Invalid due date format: '{due_on}'"