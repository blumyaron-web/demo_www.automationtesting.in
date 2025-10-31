"""
Constants and configuration data for tests.
"""

# Form selection options
FORM_OPTIONS = {
    "genders": ["Male", "Female"],
    "hobbies": ["Cricket", "Movies", "Hockey"],
    "languages": ["English", "Arabic", "Bulgarian"],
    "skills": ["Java", "C", "C++", "Python"],
    "countries": ["India", "Australia", "United States"]
}

# Date options
DATE_OPTIONS = {
    "months": [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ],
    "year_range": (1980, 2000),
    "day_range": (1, 28)  # Safe range for all months
}

# Password requirements
PASSWORD_CONFIG = {
    "length": 12,
    "special_chars": True,
    "digits": True,
    "upper_case": True,
    "lower_case": True
}

# File paths
TEST_FILES = {
    "dummy_file": "dummy_file.txt"
}

# Default locale for Faker
DEFAULT_LOCALE = "en_US"