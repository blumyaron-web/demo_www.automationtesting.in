import random
from faker import Faker


class TestDataGenerator:
    """Simple test data generator for form filling"""

    def __init__(self):
        self.fake = Faker()

    def get_personal_info(self):
        """Generate personal information data"""
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "address": self.fake.address().replace("\n", ", "),
            "email": self.fake.email(),
            "phone": self.fake.phone_number()[:10],
        }

    def get_form_selections(self):
        """Generate form selection data"""
        return {
            "gender": random.choice(["Male", "Female"]),
            "hobbies": [random.choice(["Cricket", "Movies", "Hockey"])],
            "language": random.choice(["English", "Arabic", "Bulgarian"]),
            "skills": random.choice(["Java", "C", "C++", "Python"]),
            "country": random.choice(["India", "Australia", "United States"]),
        }

    def get_birth_date(self):
        """Generate birth date components"""
        return {
            "year": str(random.randint(1980, 2000)),
            "month": random.choice(
                [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ]
            ),
            "day": str(random.randint(1, 28)),
        }

    def get_password(self):
        """Generate secure password"""
        return self.fake.password(
            length=12, special_chars=True, digits=True, upper_case=True
        )

    def get_alert_text(self):
        """Generate text for alert testing"""
        return self.fake.sentence(nb_words=3)
