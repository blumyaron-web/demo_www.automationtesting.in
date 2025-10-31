class Locators:
    SWITCH_TO_MENU = "text=SwitchTo"
    ALERTS_MENU_ITEM = "text=Alerts"

    NAVIGATE_TO_ALERTS_WITH_OK_CANCEL = "li:has-text('Alert with OK & Cancel')"
    NAVIGATE_TO_ALERTS_WITH_TEXTBOX = "li:has-text('Alert with Textbox')"
    ALERT_WITH_TEXTBOX = "li:has-text('Alert with Textbox')"

    ALERT_WITH_OK_BUTTON = "button[onclick='alertbox()']"
    ALERT_WITH_OK_CANCEL_BUTTON = "button[onclick='confirmbox()']"
    ALERT_WITH_TEXTBOX_BUTTON = "button[onclick='promptbox()']"
