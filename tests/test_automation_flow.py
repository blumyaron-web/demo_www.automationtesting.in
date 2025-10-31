import os
from data import get_standard_test_data


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
        
        # Generate test data using dedicated data module
        test_data = get_standard_test_data()
        
        # Extract data for easier access
        personal = test_data.personal_info
        selections = test_data.form_selections
        birth = test_data.birth_date
        credentials = test_data.credentials
        alert_text = test_data.alert_input_text
        
        logger.info(f"Generated test data - Name: {personal.first_name} {personal.last_name}, Email: {personal.email_address}")
        
        app_pages.index.navigate()
        app_pages.index.skip_signin()

        app_pages.register.fill_personal_info(
            first_name=personal.first_name,
            last_name=personal.last_name,
            address=personal.full_address,
            email=personal.email_address,
            phone=personal.phone_number,
        )

        app_pages.register.select_gender(selections.gender)
        app_pages.register.select_hobbies(selections.hobbies)
        app_pages.register.select_language(selections.language)
        app_pages.register.select_skills(selections.skills)
        app_pages.register.select_country(selections.country)
        app_pages.register.select_birth_date(birth.year, birth.month, birth.day)
        app_pages.register.fill_password(credentials.password)
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
            f"Test completed successfully with generated data for {personal.first_name} {personal.last_name}"
        )
