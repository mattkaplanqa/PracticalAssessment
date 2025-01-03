# README

## Introduction
This project is an automation test suite created as part of a technical assessment. The primary objective is to test the login functionality for a portfolio page on a given web application and validate the total portfolio value. Sensitive information like credentials is handled securely using environment variables.

---

## Features
- **Technology Stack**: Python, Selenium, Pytest
- **Testing Framework**: Page Object Model (POM)
- **Environment Management**: `.env` file for secure credential storage
- **Browser Automation**: Chrome WebDriver

---

## Prerequisites
### Software Requirements:
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Python Libraries:
Install the required libraries:
```bash
pip install selenium pytest python-dotenv
```

### Environment Setup:
Create a `.env` file in the project root directory and add your login credentials:
```env
USERNAME=your_username
PASSWORD=your_password
```
> Note: Ensure that the `.env` file is not pushed to a public repository by including it in the `.gitignore` file.

---

## Project Structure
```
/project-root
  |-- pages/                   # Page Object Model (POM) classes
       |-- base_page.py        # Base class for common Selenium interactions
       |-- login_page.py       # Login page interactions
       |-- portfolio_page.py   # Portfolio page interactions
  |-- tests/                   # Test cases
       |-- test_portfolio.py   # Test for portfolio value validation
  |-- .env                     # Environment variables for credentials
  |-- .gitignore               # Excludes sensitive files from Git
  |-- conftest.py              # Pytest configuration (optional)
  |-- pytest.ini               # Pytest settings
  |-- README.md                # Documentation (this file)
```

---

## How to Run the Tests
### 1. Clone the Repository
Clone this project to your local machine:
```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Set Up ChromeDriver
Download ChromeDriver from the [official website](https://chromedriver.chromium.org/downloads) and ensure it is in your system’s PATH or the project directory.

### 3. Run the Tests
Run the test suite using Pytest:
```bash
pytest tests/
```

---

## Test Description
### Test Case: Validate Portfolio Value
1. **Navigate to the Login Page**: Open the specified web application.
2. **Enter Credentials**: Use credentials stored in environment variables to log in.
3. **Validate Portfolio Value**: Retrieve and assert the total portfolio value on the portfolio page.

---

## Notes
- This project adheres to the principles of modular and reusable code by implementing the Page Object Model (POM).
- Sensitive data such as usernames and passwords are securely handled using environment variables.
- The test is parameterized to work with different accounts and environments by modifying the `.env` file.

---

## Limitations
- No multi-factor authentication (MFA) or email verification handling is included.

---

## Improvements
- Add support for email verification or MFA if required in future scenarios.
- Implement additional test cases to cover other areas of the application, such as transaction history or account settings.

---

## Submission
Submit the project repository link to your recruiting contact for review. Ensure the repository is public and all necessary dependencies and instructions are included.

---

Thank you for your time and consideration!

