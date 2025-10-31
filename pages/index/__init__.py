from pages.base_page import BasePage


class IndexPage(BasePage):
    SKIP_SIGNIN_BUTTON = "text=Skip Sign in"

    def __init__(self, page):
        super().__init__(page)
        self.__page = page
        self.url = "/Index.html"
        self.base_url = ""

    def set_base_url(self, base_url: str):
        self.base_url = base_url

    def navigate(self):
        # Construct full URL by combining base URL with relative path
        full_url = self.base_url + self.url if self.base_url else self.url
        self.__page.goto(full_url)

    def skip_signin(self):
        self.click(self.SKIP_SIGNIN_BUTTON)
