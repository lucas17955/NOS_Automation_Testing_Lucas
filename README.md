# REST API Test Automation Project

This project provides a framework for automating tests for a REST API using Python.

## Overview

This project includes test cases for performing CRUD (Create, Read, Update, Delete) operations on a sample REST API. It demonstrates how to use Python and the `requests` library to interact with the API endpoints, as well as how to organize test cases and utility functions for better maintainability and scalability.

## Features

- **CRUD Operations**: Test cases are provided for creating, reading, updating, and deleting resources (users) using the REST API.
- **Modular Structure**: The project is organized into separate modules for tests and utility functions, making it easier to manage and extend.
- **Dynamic Data Generation**: Random data generation is implemented for creating test data, ensuring test independence and repeatability.
- **Response Logging**: Responses from API requests are logged, providing visibility into the interactions with the API endpoints.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd rest_api_test_automation_project
    ```

2. Run the test suite:

    ```bash
    pytest -s tests/test_users_CRUD.py
    ```

3. View the test results in the terminal.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
