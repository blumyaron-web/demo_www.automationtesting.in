from abc import ABC
from playwright.sync_api import Page


class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: str) -> None:
        self.page.click(locator)

    def fill(self, locator: str, value: str) -> None:
        self.page.fill(locator, value)

    def select_option(self, locator: str, value: str) -> None:
        self.page.select_option(locator, value)

    def wait_for_element(self, locator: str, timeout: int = 5000) -> None:
        self.page.wait_for_selector(locator, timeout=timeout)

    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)

    def get_text(self, locator: str) -> str:
        return self.page.text_content(locator)

    def upload_file(self, locator: str, file_path: str) -> None:
        self.page.set_input_files(locator, file_path)

    def close_dropdown(self) -> None:
        viewport = self.page.viewport_size
        x, y = viewport["width"] / 2 + 10, viewport["height"] / 2 + 10
        self.page.mouse.click(x, y)
