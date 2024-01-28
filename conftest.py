import logging as logger
import pytest
import os

from lib.api_client import APIClient
from lib.helpers.common_helpers import *


@pytest.fixture(scope="module")
def api_client():
    api_client = APIClient(os.environ["INDEX_API_HOST"])
    yield api_client


@pytest.fixture(scope="module")
def new_user():
    user = generate_user_data()
    logger.info(f"Created user: {user}")
    return user


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
def base_page(context_creation, browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto(os.environ["BASE_URL"])

    yield page
    page.close()
