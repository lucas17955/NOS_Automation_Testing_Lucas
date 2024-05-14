# REST API Test Automation Project

This project provides a framework for automating tests for a REST API using Python.

## Overview

This test automation project aims to provide a robust and scalable solution for testing a REST API. It includes test cases for performing CRUD (Create, Read, Update, Delete) operations on a sample REST API. The project demonstrates how to use Python and the `requests` library to interact with the API endpoints, as well as how to organize test cases and utility functions for better maintainability and scalability.

## Features

- **Automated testing of REST APIs**
- **Validation of response schemas**
- **Modular and reusable test components**
- **Support for multiple test report formats**

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd NOS_Automation_Testing_Lucas
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Allure:
    Follow this link https://allurereport.org/docs/install/ 

## Usage 

1. Navigate to the project directory:

    ```bash
    cd NOS_Automation_Testing_Lucas
    ```

2. Run the test suite with HTML report:

    ```bash
    pytest --html=report.html tests/<testfile>.py
    ```

    This will generate an HTML report named `report.html` in the project directory. You can open this file in a web browser to view the test results. This is a simple report that don't need the use of external installations.

3. Run the test suite with Allure report:

    ```bash
    pytest --alluredir=allure-report tests/<testfile>.py
    ```

    After running the tests, you can generate the Allure report by executing the following command:

    ```bash
    allure serve allure-report
    ```

    This will open a web browser with the generated Allure report, showing detailed information about the test execution.
    This is a more complete report, that will need to have allure installed in order to open it.

4. View the test results in the chosen report format.

## Running JMeter Tests with Python

This project includes a Python script to automate the execution of JMeter tests and generate HTML reports.

### Prerequisites

1. Ensure you have the Apache JMeter binaries placed in the `apache-jmeter` directory inside your project folder.
2. Ensure the following files and directories exist:
    - `jmeter/projects/get_user_stress_test.jmx`
    - `jmeter/configs/jmeter.properties`
    - `jmeter/results/` (will be created if it doesn't exist)

### Running the JMeter Test Plan

1. Navigate to the `jmeter/tests` directory.
2. Run the Python script to execute the JMeter test plan and generate the HTML report:

   ```bash
   python run_jmeter_tests.py

## Output Location
The script will save the JTL (JMeter Test Log) output file to the results directory inside the jmeter folder. The file name will include a timestamp to ensure uniqueness.

The HTML report will also be generated in the results directory inside a folder named html_report_<timestamp>.

For example:

JTL output file: results_20240514_153045.jtl
HTML report directory: html_report_20240514_153045
Open the index.html file inside the HTML report directory to view the detailed test results.

## Project Structure

- **tests/**: Directory containing test scripts.
    - **test_todos.py**: Test script for GET operation on todos.
    - **test_users_CRUD.py**: Test script for CRUD operations on users.
- **utils/**: Directory containing utility functions.
    - **api_requests.py**: Module for making API requests.
    - **config.py**: Configuration settings for the project.
- **requirements.txt**: File listing the project dependencies.
- **README.md**: Markdown file containing project documentation.
- **.gitignore**: File specifying which files and directories to ignore in version control.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.