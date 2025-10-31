"""
Test data factory for creating specific types of test scenarios.
"""

from .generators import TestDataGenerator, TestData
from .constants import DEFAULT_LOCALE


class TestDataFactory:
    """Factory for creating different types of test data scenarios."""
    
    def __init__(self, locale: str = DEFAULT_LOCALE):
        """Initialize the factory with a data generator."""
        self.generator = TestDataGenerator(locale)
    
    def create_standard_user_data(self) -> TestData:
        """Create standard user data for typical test scenarios."""
        return self.generator.generate_complete_test_data()
    
    def create_international_user_data(self) -> TestData:
        """Create international user data with different locale."""
        intl_generator = TestDataGenerator('en_GB')  # UK locale
        return intl_generator.generate_complete_test_data()
    
    def create_minimal_user_data(self) -> TestData:
        """Create minimal required data for basic tests."""
        data = self.generator.generate_complete_test_data()
        # Could customize here for minimal requirements
        return data
    
    def create_edge_case_data(self) -> TestData:
        """Create edge case data for boundary testing."""
        data = self.generator.generate_complete_test_data()
        # Could customize here for edge cases
        return data


# Convenience functions
def get_standard_test_data() -> TestData:
    """Get standard test data for most test scenarios."""
    factory = TestDataFactory()
    return factory.create_standard_user_data()


def get_international_test_data() -> TestData:
    """Get international test data for localization testing."""
    factory = TestDataFactory()
    return factory.create_international_user_data()