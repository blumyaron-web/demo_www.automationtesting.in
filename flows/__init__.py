from .register import RegisterFlow
from .file_upload import FileUploadFlow


class AppFlows:
    def __init__(self, app_pages, test_data):
        self.__app_pages = app_pages
        self.__test_data = test_data

    @property
    def file_upload(self):
        return FileUploadFlow(app_pages=self.__app_pages)

    @property
    def register(self):
        return RegisterFlow(app_pages=self.__app_pages, test_data=self.__test_data)
