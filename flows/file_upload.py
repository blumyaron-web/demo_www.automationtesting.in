import os


class FileUploadFlow:

    def __init__(self, app_pages):
        self.app_pages = app_pages

    @staticmethod
    def get_dummy_file_path():
        dummy_file_path = os.path.join(
            os.path.dirname(__file__), "..", "test_data", "dummy_file.txt"
        )
        return os.path.abspath(dummy_file_path)

    def execute_file_upload_flow(self, dummy_file_path: str = None):
        if not dummy_file_path:
            dummy_file_path = self.get_dummy_file_path()

        try:
            self.app_pages.file_upload.upload_file(dummy_file_path)

        except Exception as e:
            raise Exception(f"failed to properly upload file: {e}")
