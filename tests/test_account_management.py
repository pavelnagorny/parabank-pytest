import pytest
import logging as logger
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.open_account_page import OpenAccountPage


@pytest.fixture(scope="module")
def api_created_user(api_client, new_user):
    response = api_client.register_user(new_user)
    assert (
        f"{new_user.firstname} {new_user.lastname}" in response.text
    ), "User registration failed."
    yield [api_client, new_user]


@pytest.mark.parametrize("account_type", [("CHECKING"), ("SAVINGS")])
@pytest.mark.account_test
def test_user_can_open_the_account(base_page, api_created_user, account_type) -> None:
    page = base_page
    api_client = api_created_user[0]
    user = api_created_user[1]
    LoginPage(page).login(user)
    MainPage(page).click_open_account_button()
    account_id = OpenAccountPage(page).open_account(account_type)

    logger.info(f"\nNew account for user has been created:\nUser:{user}\nAccount_id: {account_id}")


def test_user_can_transfer_funds_between_accounts() -> None:
    pass


"""
  Scenario: Verify new user can transfer funds between accounts
    When I register a "user" on API
    And I create random account for "user" user on API
    And I am on the homepage
    And I login as a "user"
    And I navigate to the Transfer Funds page
    And I transfer 100 to the newly created account for "user" user
    Then I see money was transferred

"""
