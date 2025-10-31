from playwright.async_api import Page

from .index import IndexPage
from .alerts import AlertsPage
from .register import RegisterPage
from .file_upload import FileUploadPage


class AppPages:
    def __init__(self, page: Page):
        self.__page = page
        self.__base_url = ""

    def set_base_url(self, base_url: str):
        self.__base_url = base_url

    @property
    def index(self):
        index_page = IndexPage(self.__page)
        if self.__base_url:
            index_page.set_base_url(self.__base_url)
        return index_page

    @property
    def alerts(self):
        return AlertsPage(self.__page)

    @property
    def register(self):
        return RegisterPage(self.__page)

    @property
    def file_upload(self):
        return FileUploadPage(self.__page)
