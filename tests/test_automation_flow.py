import os
from data.generator import TestDataGenerator


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

        # Generate test data
        data_gen = TestDataGenerator()
        personal_info = data_gen.get_personal_info()
        form_selections = data_gen.get_form_selections()
        birth_date = data_gen.get_birth_date()
        password = data_gen.get_password()
        alert_text = data_gen.get_alert_text()
        
        logger.info(f"Generated test data - Name: {personal_info['first_name']} {personal_info['last_name']}, Email: {personal_info['email']}")

        app_pages.index.navigate()
        app_pages.index.skip_signin()

        app_pages.register.fill_personal_info(
            first_name=personal_info['first_name'],
            last_name=personal_info['last_name'],
            address=personal_info['address'],
            email=personal_info['email'],
            phone=personal_info['phone'],
        )

        app_pages.register.select_gender(form_selections['gender'])
        app_pages.register.select_hobbies(form_selections['hobbies'])
        app_pages.register.select_language(form_selections['language'])
        app_pages.register.select_skills(form_selections['skills'])
        app_pages.register.select_country(form_selections['country'])
        app_pages.register.select_birth_date(birth_date['year'], birth_date['month'], birth_date['day'])
        app_pages.register.fill_password(password)
        app_pages.register.submit_form()

        app_pages.alerts.navigate_to_alerts()

        alert_text_1 = app_pages.alerts.click_alert_with_ok()

        app_pages.alerts.navigate_to_alerts_with_ok_and_cancel()
        alert_text_2 = app_pages.alerts.click_alert_with_ok_cancel("accept")

        app_pages.alerts.navigate_to_alerts_with_textbox()
        input_text = app_pages.alerts.click_alert_with_textbox(alert_text)

        app_pages.file_upload.navigate_to_file_upload()

        dummy_file_path = os.path.join(
            os.path.dirname(__file__), "..", "test_data", "dummy_file.txt"
        )
        dummy_file_path = os.path.abspath(dummy_file_path)
        app_pages.file_upload.upload_file(dummy_file_path)

        logger.info(
            f"Test completed successfully with generated data for {personal_info['first_name']} {personal_info['last_name']}"
        )
