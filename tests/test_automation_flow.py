import pytest


class TestAutomationFlow:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky
    def test_complete_automation_flow(self, test_data, app_pages, app_flows):
        alert_text = test_data.get_alert_text()

        app_pages.index.navigate()
        app_pages.index.skip_signin()

        app_flows.register.fill_personal_info()
        app_flows.register.register_user()

        app_pages.alerts.navigate_to_alerts()
        app_pages.alerts.click_alert_with_ok()

        app_pages.alerts.navigate_to_alerts_with_ok_and_cancel()
        app_pages.alerts.click_alert_with_ok_cancel("accept")

        app_pages.alerts.navigate_to_alerts_with_textbox()
        app_pages.alerts.click_alert_with_textbox(alert_text)

        app_pages.file_upload.navigate_to_file_upload()
        app_flows.file_upload.execute_file_upload_flow()
