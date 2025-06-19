# Facebook Automation with Selenium, Pytest, and Page Object Model (POM)

## Overview
This project demonstrates how to automate Facebook login using Selenium WebDriver in Python, following the Page Object Model (POM) design pattern. It uses pytest for test execution and organizes code for maintainability and scalability.

---

## Features
- Automates Facebook login using Selenium
- Uses Page Object Model for clean code structure
- Credentials and URLs are stored securely and excluded from version control
- Easily extendable for more Facebook automation scenarios

---

## Project Structure
```
pytest-demo/
│
├── config/
│   └── creds.py         # Stores credentials and URLs (excluded from git)
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py    # Page Object for Facebook login
│   └── home_page.py     # (Optional) Page Object for Facebook home
│
├── tests/
│   ├── __init__.py
│   └── test_facebook_login.py  # Test case(s) using POM
│
├── venv/                # Python virtual environment (excluded from git)
├── requirements.txt     # Python dependencies
└── .gitignore           # Excludes sensitive and unnecessary files from git
```

---

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd training-demoproject/pytest-demo
```

### 2. Create and Activate Virtual Environment
```
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# If you get a script execution error, use:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure Credentials
- Edit `config/creds.py` and add your Facebook username, password, and URL.
- **Never commit this file to git!**

### 5. Download ChromeDriver
- Download the ChromeDriver matching your Chrome version: https://sites.google.com/chromium.org/driver/
- Place `chromedriver.exe` in your project root or ensure it is in your system PATH.

### 6. Run the Tests
```
.\venv\Scripts\python.exe -m pytest tests/
```

---

## How It Works
- **Page Object Model:**
  - `pages/login_page.py` contains a `LoginPage` class with methods to interact with the Facebook login page.
  - (Optional) `pages/home_page.py` can be extended for post-login actions.
- **Test Case:**
  - `tests/test_facebook_login.py` uses pytest to launch the browser, navigate to Facebook, and perform login using the POM class.
  - Credentials and URL are imported from `config/creds.py`.

---

## Security
- Sensitive data is stored in `config/creds.py` and excluded from git via `.gitignore`.
- Do not share or commit your credentials.

---

## Extending the Project
- Add more Page Object classes for other Facebook pages or features.
- Add more test cases in the `tests/` folder.
- Parameterize tests for different scenarios.

---

## Troubleshooting
- **Script execution error:**
  - Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.
- **ChromeDriver not found:**
  - Ensure `chromedriver.exe` is in your project root or PATH, and matches your Chrome version.
- **Login fails:**
  - Double-check your credentials in `config/creds.py`.

---

## License
This project is for educational and demonstration purposes only.
