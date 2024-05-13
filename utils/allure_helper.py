import allure

def attach_response_data(response):
    """
    Attaches the response data to the Allure report.
    """
    allure.attach(response.text, name="Response Data", attachment_type=allure.attachment_type.TEXT)