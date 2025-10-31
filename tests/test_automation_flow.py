import os
import random
from faker import Faker


class TestAutomationFlow:

    def test_complete_automation_flow(self, app_pages, logger):
        """
        Complete automation test flow as per requirements:
        1. Navigate to demo site
        2. Skip sign-in
        3. Fill registration form
        4. Submit form
        5. Navigate to alerts and handle all 3 types
        6. Navigate to file upload and upload dummy file
        """
        
        # Initialize Faker for generating test data
        fake = Faker()
        
        # Generate test data variables
        first_name = fake.first_name()
        last_name = fake.last_name()
        full_address = fake.address().replace('\n', ', ')
        email_address = fake.email()
        phone_number = fake.phone_number()[:10]  # Limit to 10 digits
        
        # Form selection data
        gender = random.choice(["Male", "Female"])
        hobbies = [random.choice(["Cricket", "Movies", "Hockey"])]
        language = random.choice(["English", "Arabic", "Bulgarian"])
        skills = random.choice(["Java", "C", "C++", "Python"])
        country = random.choice(["India", "Australia", "United States"])
        
        # Birth date components
        birth_year = str(random.randint(1980, 2000))
        birth_month = random.choice(["January", "February", "March", "April", "May", "June", 
                                   "July", "August", "September", "October", "November", "December"])
        birth_day = str(random.randint(1, 28))  # Safe range for all months
        
        # Password
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True)
        
        # Alert test input
        alert_input_text = fake.sentence(nb_words=3)
        
        logger.info(f"Generated test data - Name: {first_name} {last_name}, Email: {email_address}")
        
        app_pages.index.navigate()
        app_pages.index.skip_signin()
        
        app_pages.register.fill_personal_info(
            first_name=first_name,
            last_name=last_name,
            address=full_address,
            email=email_address,
            phone=phone_number
        )

        app_pages.register.select_gender(gender)
        app_pages.register.select_hobbies(hobbies)
        app_pages.register.select_language(language)
        app_pages.register.select_skills(skills)
        app_pages.register.select_country(country)
        app_pages.register.select_birth_date(birth_year, birth_month, birth_day)
        app_pages.register.fill_password(password)
        app_pages.register.submit_form()

        app_pages.alerts.navigate_to_alerts()
        
        alert_text_1 = app_pages.alerts.click_alert_with_ok()

        app_pages.alerts.navigate_to_alerts_with_ok_and_cancel()
        alert_text_2 = app_pages.alerts.click_alert_with_ok_cancel("accept")

        app_pages.alerts.navigate_to_alerts_with_textbox()
        input_text = app_pages.alerts.click_alert_with_textbox(alert_input_text)

        app_pages.file_upload.navigate_to_file_upload()
        
        dummy_file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "dummy_file.txt")
        dummy_file_path = os.path.abspath(dummy_file_path)
        app_pages.file_upload.upload_file(dummy_file_path)
        
        logger.info(f"Test completed successfully with generated data for {first_name} {last_name}")
