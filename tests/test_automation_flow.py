import os


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
        
        app_pages.index.navigate()
        app_pages.index.skip_signin()
        
        app_pages.register.fill_personal_info(
            first_name="John",
            last_name="Doe",
            address="123 Test Street, Test City",
            email="john.doe@test.com",
            phone="1234567890"
        )

        app_pages.register.select_gender("Male")
        app_pages.register.select_hobbies(["Cricket"])
        app_pages.register.select_language("English")
        app_pages.register.select_skills("Java")
        app_pages.register.select_country("India")
        app_pages.register.select_birth_date("1990", "January", "1")
        app_pages.register.fill_password("TestPassword123")
        app_pages.register.submit_form()

        app_pages.alerts.navigate_to_alerts()
        
        alert_text_1 = app_pages.alerts.click_alert_with_ok()

        app_pages.alerts.navigate_to_alerts_with_ok_and_cancel()
        alert_text_2 = app_pages.alerts.click_alert_with_ok_cancel("accept")

        app_pages.alerts.navigate_to_alerts_with_textbox()
        input_text = app_pages.alerts.click_alert_with_textbox("Test Input")

        app_pages.file_upload.navigate_to_file_upload()
        
        dummy_file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "dummy_file.txt")
        dummy_file_path = os.path.abspath(dummy_file_path)
        app_pages.file_upload.upload_file(dummy_file_path)
