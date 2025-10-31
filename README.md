# Eleos Automation Test Project# Eleos Automation Test Project# Eleos Automation Test Project



A comprehensive test automation suite using Playwright and pytest, implementing the Page Object Model pattern for maintainable and scalable web application testing.



## 🎯 OverviewA comprehensive test automation suite using Playwright and pytest, implementing the Page Object Model pattern for maintainable and scalable web application testing.This project contains automated tests using Playwright and pytest for the automation assignment.



This project automates end-to-end testing scenarios for the demo automation testing website, covering form interactions, alert handling, and file upload functionality.



## 📁 Project Structure## 🎯 Overview## Project Structure



```

eleos/

├── 📂 pages/                    # Page Object Model implementationThis project automates end-to-end testing scenarios for the demo automation testing website, covering form interactions, alert handling, and file upload functionality.```

│   ├── __init__.py

│   ├── base_page.py            # Base page with common functionalityeleos/

│   ├── alerts/                 # Alert page components

│   │   ├── __init__.py## 📁 Project Structure├── pages/                      # Page Object Model classes

│   │   └── locators.py

│   ├── file_upload/            # File upload page components│   ├── __init__.py

│   │   ├── __init__.py

│   │   └── locators.py```│   ├── base_page.py           # Base page with common functionality

│   ├── index/                  # Home page components

│   │   ├── __init__.pyeleos/│   ├── index_page.py          # Index/home page objects

│   │   └── locators.py

│   └── register/               # Registration page components├── 📂 pages/                    # Page Object Model implementation│   ├── register_page.py       # Registration form page objects

│       ├── __init__.py

│       └── locators.py│   ├── __init__.py│   ├── alerts_page.py         # Alerts page objects

├── 📂 tests/                   # Test implementation

│   ├── __init__.py│   ├── base_page.py            # Base page with common functionality│   └── file_upload_page.py    # File upload page objects

│   └── test_automation_flow.py # Main automation test suite

├── 📂 test_data/               # Test assets│   ├── alerts/                 # Alert page components├── tests/                     # Test files

│   ├── __init__.py

│   └── dummy_file.txt         # Sample file for upload testing│   │   ├── __init__.py│   ├── __init__.py

├── 📂 utils/                   # Utility modules

│   ├── __init__.py│   │   └── locators.py│   └── test_automation_flow.py # Main automation test

│   └── logger.py              # Logging configuration

├── 📂 reports/                 # Test reports (generated)│   ├── file_upload/            # File upload page components├── test_data/                 # Test data files

├── 📂 logs/                    # Test logs (generated)

├── 🐳 Dockerfile              # Docker container configuration│   │   ├── __init__.py│   ├── __init__.py

├── 🐳 Dockerfile.playwright   # Alternative Playwright-based container

├── 🐳 docker-compose.yml      # Docker Compose setup│   │   └── locators.py│   └── dummy_file.txt        # Sample file for upload testing

├── ⚙️ conftest.py             # Pytest configuration and fixtures

├── ⚙️ pytest.ini             # Pytest settings│   ├── index/                  # Home page components├── conftest.py               # Pytest configuration and fixtures

├── 📋 requirements.txt        # Python dependencies

└── 📖 README.md              # This file│   │   ├── __init__.py├── pytest.ini               # Pytest settings

```

│   │   └── locators.py└── requirements.txt          # Python dependencies

## 🚀 Quick Start

│   └── register/               # Registration page components```

### Prerequisites

│       ├── __init__.py

- Python 3.13+

- Docker & Docker Compose (for containerized execution)│       └── locators.py## Setup



### 🔧 Setup Options├── 📂 tests/                   # Test implementation



#### Option 1: Local Development Setup│   ├── __init__.py### Option 1: Local Setup



1. **Clone and navigate to the project:**│   └── test_automation_flow.py # Main automation test suite

   ```bash

   cd /path/to/eleos├── 📂 test_data/               # Test assets1. Create virtual environment:

   ```

│   ├── __init__.py   ```bash

2. **Create and activate virtual environment:**

   ```bash│   └── dummy_file.txt         # Sample file for upload testing   python -m venv .venv

   python -m venv .venv

   source .venv/bin/activate  # macOS/Linux├── 📂 utils/                   # Utility modules   source .venv/bin/activate  # On macOS/Linux

   # or

   .venv\Scripts\activate     # Windows│   ├── __init__.py   ```

   ```

│   └── logger.py              # Logging configuration

3. **Install dependencies:**

   ```bash├── 📂 reports/                 # Test reports (generated)2. Install dependencies:

   pip install -r requirements.txt

   playwright install chromium├── 📂 logs/                    # Test logs (generated)   ```bash

   ```

├── 🐳 Dockerfile              # Docker container configuration   pip install -r requirements.txt

#### Option 2: Docker Setup (Recommended)

├── 🐳 docker-compose.yml      # Docker Compose setup   playwright install

**Standard Docker Build:**

```bash├── ⚙️ conftest.py             # Pytest configuration and fixtures   ```

# Using custom Dockerfile (if having issues, try the Playwright option below)

docker-compose up --build eleos-tests├── ⚙️ pytest.ini             # Pytest settings

```

├── 📋 requirements.txt        # Python dependencies### Option 2: Docker Setup

**Playwright Official Image (Recommended for reliability):**

```bash└── 📖 README.md              # This file

# Using official Playwright image - more reliable and avoids font/dependency issues

docker-compose up --build eleos-tests-playwright```1. Build and run with Docker Compose:

```

   ```bash

**Debug Mode:**

```bash## 🚀 Quick Start   docker-compose up --build

# For development with GUI access

docker-compose --profile debug up eleos-tests-debug   ```

```

### Prerequisites

## 🧪 Running Tests

2. Run in debug mode (with GUI display):

### Local Execution

- Python 3.13+   ```bash

```bash

# Run all tests with verbose output- Docker & Docker Compose (for containerized execution)   docker-compose --profile debug up eleos-tests-debug

pytest tests/test_automation_flow.py -v

   ```

# Generate HTML report

pytest tests/test_automation_flow.py --html=reports/report.html --self-contained-html### 🔧 Setup Options



# Run with specific browser3. Access interactive shell for debugging:

pytest tests/test_automation_flow.py --browser firefox

#### Option 1: Local Development Setup   ```bash

# Run in headless mode

pytest tests/test_automation_flow.py --headed=false   docker-compose --profile debug run eleos-shell

```

1. **Clone and navigate to the project:**   ```

### Docker Execution

   ```bash

```bash

# Standard test execution (custom build)   cd /path/to/eleos## Running Tests

docker-compose up eleos-tests

   ```

# Using official Playwright image (recommended)

docker-compose up eleos-tests-playwright### Local Execution



# Interactive debugging with GUI2. **Create and activate virtual environment:**

docker-compose --profile debug up eleos-tests-debug

   ```bashRun the complete automation test:

# Custom test execution

docker-compose run eleos-tests-playwright pytest tests/test_automation_flow.py -v --browser chromium   python -m venv .venv```bash



# Access container shell for debugging   source .venv/bin/activate  # macOS/Linuxpytest tests/test_automation_flow.py -v

docker-compose --profile debug run eleos-shell

```   # or```



## 🔄 Test Scenarios   .venv\Scripts\activate     # Windows



The automation suite covers the following comprehensive test flow:   ```Run with HTML report:



1. **🏠 Navigation & Initial Setup**```bash

   - Navigate to `https://demo.automationtesting.in/Index.html`

   - Handle initial page load and skip sign-in3. **Install dependencies:**pytest tests/test_automation_flow.py --html=reports/report.html



2. **📝 Registration Form Testing**   ```bash```

   - Fill complete registration form with test data

   - Validate form submission and navigation   pip install -r requirements.txt



3. **⚠️ Alert Handling**   playwright install chromium### Docker Execution

   - Navigate to SwitchTo → Alerts section

   - Test all JavaScript alert types:   ```

     - Simple alerts

     - Confirmation alerts  Run tests in Docker (headless):

     - Prompt alerts

#### Option 2: Docker Setup (Recommended)```bash

4. **📁 File Upload Testing**

   - Navigate to More → File Uploaddocker-compose up eleos-tests

   - Upload test file and validate success

1. **Quick start with Docker Compose:**```

## 🏗️ Architecture Features

   ```bash

- **🎨 Page Object Model**: Clean separation of test logic and page elements

- **🔧 Modular Design**: Reusable components and utilities   docker-compose up --buildRun tests with custom parameters:

- **📊 Comprehensive Reporting**: HTML reports with screenshots and logs

- **🌐 Cross-Browser Support**: Chrome, Firefox, Safari compatibility   ``````bash

- **🐳 Containerized**: Consistent execution across environments

- **📝 Detailed Logging**: Structured logging with timestampsdocker-compose run eleos-tests pytest tests/test_automation_flow.py -v --browser firefox

- **⚡ Pytest Integration**: Advanced fixtures and configuration

2. **For development with GUI access:**```

## 📊 Reports & Logs

   ```bash

- **HTML Reports**: Generated in `reports/report.html`

- **Test Logs**: Timestamped logs in `logs/` directory   docker-compose --profile debug up eleos-tests-debug## Test Flow

- **Screenshots**: Captured on test failures (when applicable)

   ```

## 🛠️ Configuration

The automation test covers the following steps:

### Pytest Configuration (`pytest.ini`)

- Browser settings (default: Chromium)## 🧪 Running Tests1. Navigate to https://demo.automationtesting.in/Index.html

- Test discovery patterns

- Report generation settings2. Click "Skip Sign In" button

- Base URL configuration

### Local Execution3. Fill all registration form fields

### Docker Configuration

- **Two Dockerfile options:**4. Submit the registration form

  - `Dockerfile`: Custom Python slim build

  - `Dockerfile.playwright`: Official Playwright image (recommended)```bash5. Navigate to SwitchTo -> Alerts

- Volume mounts for persistent reports

- Environment-specific settings# Run all tests with verbose output6. Handle all 3 types of JavaScript alerts

- Debug profiles for development

pytest tests/test_automation_flow.py -v7. Navigate to More -> File Upload

## 🔍 Troubleshooting

8. Upload a dummy text file

### Common Issues

# Generate HTML report

1. **Browser installation issues (Local):**

   ```bashpytest tests/test_automation_flow.py --html=reports/report.html --self-contained-html## Features

   playwright install --with-deps chromium

   ```



2. **Docker build failures with font packages:**# Run with specific browser- **Object-Oriented Design**: Uses Page Object Model pattern

   ```bash

   # Use the official Playwright image insteadpytest tests/test_automation_flow.py --browser firefox- **Reusable Components**: Base page class with common functionality

   docker-compose up eleos-tests-playwright

   ```- **Clean Test Structure**: Pytest fixtures and configuration



3. **Permission errors in Docker:**# Run in headless mode- **Cross-browser Support**: Playwright supports Chrome, Firefox, Safari

   ```bash

   docker-compose down && docker-compose up --buildpytest tests/test_automation_flow.py --headed=false- **Maintainable Code**: Separated locators and actions

   ``````



4. **Display issues in Docker (macOS):**### Docker Execution

   ```bash

   # Install XQuartz and enable "Allow connections from network clients"```bash

   xhost +localhost# Standard test execution (headless)

   ```docker-compose up eleos-tests



### Docker Image Options# Interactive debugging with GUI

docker-compose --profile debug up eleos-tests-debug

- **Custom Build (`eleos-tests`)**: Uses Python slim with manual Playwright setup

- **Playwright Official (`eleos-tests-playwright`)**: Uses Microsoft's official Playwright image (recommended for reliability)# Custom test execution

docker-compose run eleos-tests pytest tests/test_automation_flow.py -v --browser chromium

## 🤝 Contributing

# Access container shell for debugging

1. Follow the existing Page Object Model structuredocker-compose --profile debug run eleos-shell

2. Add appropriate logging and error handling```

3. Update tests for new functionality

4. Ensure Docker compatibility## 🔄 Test Scenarios



## 📄 LicenseThe automation suite covers the following comprehensive test flow:



This project is created for automation testing demonstration purposes.1. **🏠 Navigation & Initial Setup**

   - Navigate to `https://demo.automationtesting.in/Index.html`

---   - Handle initial page load and skip sign-in



**Built with ❤️ using Playwright & pytest**2. **📝 Registration Form Testing**
   - Fill complete registration form with test data
   - Validate form submission and navigation

3. **⚠️ Alert Handling**
   - Navigate to SwitchTo → Alerts section
   - Test all JavaScript alert types:
     - Simple alerts
     - Confirmation alerts  
     - Prompt alerts

4. **📁 File Upload Testing**
   - Navigate to More → File Upload
   - Upload test file and validate success

## 🏗️ Architecture Features

- **🎨 Page Object Model**: Clean separation of test logic and page elements
- **🔧 Modular Design**: Reusable components and utilities
- **📊 Comprehensive Reporting**: HTML reports with screenshots and logs
- **🌐 Cross-Browser Support**: Chrome, Firefox, Safari compatibility
- **🐳 Containerized**: Consistent execution across environments
- **📝 Detailed Logging**: Structured logging with timestamps
- **⚡ Pytest Integration**: Advanced fixtures and configuration

## 📊 Reports & Logs

- **HTML Reports**: Generated in `reports/report.html`
- **Test Logs**: Timestamped logs in `logs/` directory
- **Screenshots**: Captured on test failures (when applicable)

## 🛠️ Configuration

### Pytest Configuration (`pytest.ini`)
- Browser settings (default: Chromium)
- Test discovery patterns
- Report generation settings
- Base URL configuration

### Docker Configuration
- Multi-stage builds for optimization
- Volume mounts for persistent reports
- Environment-specific settings
- Debug profiles for development

## 🔍 Troubleshooting

### Common Issues

1. **Browser installation issues:**
   ```bash
   playwright install --with-deps chromium
   ```

2. **Permission errors in Docker:**
   ```bash
   docker-compose down && docker-compose up --build
   ```

3. **Display issues in Docker (macOS):**
   ```bash
   # Install XQuartz and enable "Allow connections from network clients"
   xhost +localhost
   ```

## 🤝 Contributing

1. Follow the existing Page Object Model structure
2. Add appropriate logging and error handling
3. Update tests for new functionality
4. Ensure Docker compatibility

## 📄 License

This project is created for automation testing demonstration purposes.

---

**Built with ❤️ using Playwright & pytest**