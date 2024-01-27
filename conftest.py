import pytest
import os

from lib.models.user import User


@pytest.fixture(scope="session")
def context_creation(playwright):
    headless_bool = False
    slowmo_value = 0

    browser = playwright.webkit.launch(headless=headless_bool, slow_mo=slowmo_value)
    context = browser.new_context()

    context.storage_state(path="state.json")

    yield context
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def home_page(context_creation, browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto(os.environ["BASE_URL"])

    yield page
    page.close()


@pytest.fixture(scope="module")
def random_user():
    return User.generate_random()
