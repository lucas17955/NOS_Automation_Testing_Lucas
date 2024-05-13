import jsonschema #this library is to validate the schema
import pytest #this library is for tests in python
import allure #for report
from utils.api_requests import get_todos

@pytest.fixture(scope="module")
def setup():
    # Setup code if needed
    yield
    # Teardown code if needed

def test_get_todos(setup):
    with allure.step("Send GET request to retrieve todos"):
        response = get_todos()

        # Attach the response data to the test step
        allure.attach(response.text, name="Response Data", attachment_type=allure.attachment_type.TEXT)

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
        jsonschema.validate(response.json(), expected_schema)