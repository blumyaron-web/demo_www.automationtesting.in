from .locators import Locators
from pages.base_page import BasePage


class AlertsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.__locators = Locators
    
    def navigate_to_alerts(self):
        self.click(self.__locators.SWITCH_TO_MENU)
        self.click(self.__locators.ALERTS_MENU_ITEM)
    
    def click_alert_with_ok(self):
        alert_text = ""
        
        def handle_dialog(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            print(f"Alert appeared: {alert_text}")
            dialog.accept()
        
        self.page.on("dialog", handle_dialog)
        self.click(self.__locators.ALERT_WITH_OK_BUTTON)
        self.page.wait_for_timeout(1000)
        return alert_text

    def navigate_to_alerts_with_ok_and_cancel(self):
        self.page.click(self.__locators.NAVIGATE_TO_ALERTS_WITH_OK_CANCEL)


    def click_alert_with_ok_cancel(self, action="accept"):
        alert_text = ""

        def handle_dialog(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            print(f"Confirm dialog appeared: {alert_text}")
            if action == "accept":
                dialog.accept()
            else:
                dialog.dismiss()
        
        self.page.on("dialog", handle_dialog)
        self.click(self.__locators.ALERT_WITH_OK_CANCEL_BUTTON)
        self.page.wait_for_timeout(1000)
        return alert_text
    
    def navigate_to_alerts_with_textbox(self):
        self.page.click(self.__locators.ALERT_WITH_TEXTBOX)

    def click_alert_with_textbox(self, text_input="Test Input"):
        alert_text = ""
        
        def handle_prompt(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            print(f"Prompt dialog appeared: {alert_text}")
            dialog.accept(text_input)
        
        self.page.on("dialog", handle_prompt)
        self.click(self.__locators.ALERT_WITH_TEXTBOX_BUTTON)
        self.page.wait_for_timeout(1000)
        return alert_text