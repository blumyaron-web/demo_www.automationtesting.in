"""
Data generation and management package for test automation.

This package provides:
- Realistic test data generation using Faker
- Structured data models for different test scenarios
- Factory patterns for creating specific test data types
- Constants and configuration for consistent data generation

Main interfaces:
- get_test_data(): Quick function for standard test data
- get_standard_test_data(): Standard user scenarios
- get_international_test_data(): International/localized scenarios
- TestDataGenerator: Full control over data generation
- TestDataFactory: Factory for specific scenarios
"""

from .generators import (
    TestData,
    PersonalInfo, 
    FormSelections,
    BirthDate,
    UserCredentials,
    TestDataGenerator,
    get_test_data
)

from .factory import (
    TestDataFactory,
    get_standard_test_data,
    get_international_test_data
)

from .constants import (
    FORM_OPTIONS,
    DATE_OPTIONS,
    PASSWORD_CONFIG,
    TEST_FILES,
    DEFAULT_LOCALE
)

__all__ = [
    # Data structures
    'TestData',
    'PersonalInfo',
    'FormSelections', 
    'BirthDate',
    'UserCredentials',
    
    # Generators
    'TestDataGenerator',
    'get_test_data',
    
    # Factory
    'TestDataFactory',
    'get_standard_test_data',
    'get_international_test_data',
    
    # Constants
    'FORM_OPTIONS',
    'DATE_OPTIONS', 
    'PASSWORD_CONFIG',
    'TEST_FILES',
    'DEFAULT_LOCALE'
]