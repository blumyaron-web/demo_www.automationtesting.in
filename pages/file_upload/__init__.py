from .locators import Locators
from pages.base_page import BasePage


class FileUploadPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.__locators = Locators

    def navigate_to_file_upload(self):
        self.click(self.__locators.MORE_MENU)
        self.click(self.__locators.FILE_UPLOAD_MENU_ITEM)

    def file_upload(self, file_path: str):
        super().upload_file(self.__locators.FILE_INPUT, file_path)

    def upload_file(self, file_path: str):
        self.file_upload(file_path)
