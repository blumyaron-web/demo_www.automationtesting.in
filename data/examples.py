"""
Examples of using the test data generation module.

This file demonstrates different ways to generate and use test data
for automation testing scenarios.
"""

from data import (
    get_test_data,
    get_standard_test_data, 
    get_international_test_data,
    TestDataGenerator,
    TestDataFactory
)


def example_basic_usage():
    """Basic usage example."""
    print("=== Basic Usage ===")
    
    # Quick way to get test data
    data = get_standard_test_data()
    
    print(f"Name: {data.personal_info.first_name} {data.personal_info.last_name}")
    print(f"Email: {data.personal_info.email_address}")
    print(f"Country: {data.form_selections.country}")
    print(f"Birth Date: {data.birth_date.month} {data.birth_date.day}, {data.birth_date.year}")


def example_international_data():
    """International data example."""
    print("\n=== International Data ===")
    
    data = get_international_test_data()
    
    print(f"Name: {data.personal_info.first_name} {data.personal_info.last_name}")
    print(f"Address: {data.personal_info.full_address}")


def example_custom_generator():
    """Custom generator example."""
    print("\n=== Custom Generator ===")
    
    # Use specific locale
    generator = TestDataGenerator('fr_FR')  # French locale
    data = generator.generate_complete_test_data()
    
    print(f"French Name: {data.personal_info.first_name} {data.personal_info.last_name}")
    print(f"French Address: {data.personal_info.full_address}")


def example_factory_usage():
    """Factory usage example."""
    print("\n=== Factory Usage ===")
    
    factory = TestDataFactory()
    
    # Different scenarios
    standard_data = factory.create_standard_user_data()
    minimal_data = factory.create_minimal_user_data()
    edge_case_data = factory.create_edge_case_data()
    
    print(f"Standard: {standard_data.personal_info.first_name}")
    print(f"Minimal: {minimal_data.personal_info.first_name}")
    print(f"Edge Case: {edge_case_data.personal_info.first_name}")


def example_data_structure_access():
    """Example of accessing structured data."""
    print("\n=== Data Structure Access ===")
    
    data = get_test_data()
    
    # Access personal info
    personal = data.personal_info
    print(f"Personal Info: {personal.first_name}, {personal.email_address}")
    
    # Access form selections
    selections = data.form_selections
    print(f"Selections: {selections.gender}, {selections.skills}")
    
    # Access birth date
    birth = data.birth_date
    print(f"Birth: {birth.month} {birth.day}, {birth.year}")
    
    # Access credentials
    print(f"Password: {data.credentials.password}")
    
    # Access alert text
    print(f"Alert Text: {data.alert_input_text}")


if __name__ == "__main__":
    """Run all examples."""
    example_basic_usage()
    example_international_data()
    example_custom_generator()
    example_factory_usage()
    example_data_structure_access()