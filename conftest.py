import pytest
from pages import AppPages
from utils.logger import get_logger


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def app_pages(page, request):
    base_url = request.config.getoption(
        "--base-url", default="https://demo.automationtesting.in"
    )
    app_pages_instance = AppPages(page=page)
    app_pages_instance.set_base_url(base_url)
    return app_pages_instance


@pytest.fixture(scope="function")
def logger():
    return get_logger()
