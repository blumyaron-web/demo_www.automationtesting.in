"""
Test data generation using Faker library.
Provides realistic test data for automation tests.
"""

import random
from dataclasses import dataclass
from typing import List
from faker import Faker

from .constants import FORM_OPTIONS, DATE_OPTIONS, PASSWORD_CONFIG, DEFAULT_LOCALE


@dataclass
class PersonalInfo:
    """Personal information data structure."""
    first_name: str
    last_name: str
    full_address: str
    email_address: str
    phone_number: str


@dataclass
class FormSelections:
    """Form selection data structure."""
    gender: str
    hobbies: List[str]
    language: str
    skills: str
    country: str


@dataclass
class BirthDate:
    """Birth date data structure."""
    year: str
    month: str
    day: str


@dataclass
class UserCredentials:
    """User credentials data structure."""
    password: str


@dataclass
class TestData:
    """Complete test data structure."""
    personal_info: PersonalInfo
    form_selections: FormSelections
    birth_date: BirthDate
    credentials: UserCredentials
    alert_input_text: str


class TestDataGenerator:
    """Generates realistic test data using Faker."""
    
    def __init__(self, locale: str = DEFAULT_LOCALE):
        """Initialize the test data generator.
        
        Args:
            locale: Faker locale for generating localized data
        """
        self.fake = Faker(locale)
    
    def generate_personal_info(self) -> PersonalInfo:
        """Generate personal information data."""
        return PersonalInfo(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            full_address=self.fake.address().replace('\n', ', '),
            email_address=self.fake.email(),
            phone_number=self.fake.phone_number()[:10]  # Limit to 10 digits
        )
    
    def generate_form_selections(self) -> FormSelections:
        """Generate form selection data."""
        return FormSelections(
            gender=random.choice(FORM_OPTIONS["genders"]),
            hobbies=[random.choice(FORM_OPTIONS["hobbies"])],
            language=random.choice(FORM_OPTIONS["languages"]),
            skills=random.choice(FORM_OPTIONS["skills"]),
            country=random.choice(FORM_OPTIONS["countries"])
        )
    
    def generate_birth_date(self) -> BirthDate:
        """Generate birth date data."""
        return BirthDate(
            year=str(random.randint(*DATE_OPTIONS["year_range"])),
            month=random.choice(DATE_OPTIONS["months"]),
            day=str(random.randint(*DATE_OPTIONS["day_range"]))
        )
    
    def generate_credentials(self) -> UserCredentials:
        """Generate user credentials."""
        return UserCredentials(
            password=self.fake.password(**PASSWORD_CONFIG)
        )
    
    def generate_alert_text(self) -> str:
        """Generate random text for alert testing."""
        return self.fake.sentence(nb_words=3)
    
    def generate_complete_test_data(self) -> TestData:
        """Generate complete test data for automation tests."""
        return TestData(
            personal_info=self.generate_personal_info(),
            form_selections=self.generate_form_selections(),
            birth_date=self.generate_birth_date(),
            credentials=self.generate_credentials(),
            alert_input_text=self.generate_alert_text()
        )


# Convenience function for quick data generation
def get_test_data(locale: str = DEFAULT_LOCALE) -> TestData:
    """
    Quick function to generate complete test data.
    
    Args:
        locale: Faker locale for generating localized data
        
    Returns:
        TestData: Complete test data structure
    """
    generator = TestDataGenerator(locale)
    return generator.generate_complete_test_data()