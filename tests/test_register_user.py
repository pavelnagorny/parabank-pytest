import pytest

from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


pytestmark = pytest.mark.ui_test


@pytest.mark.nn
def test_new_user_can_successfully_register_to_app(base_page, new_user) -> None:
    # Assess - Given
    # Act - When/And
    page = base_page
    LoginPage(page).click_register_button()
    SignUpPage(page).fill_out_register_form(new_user)
    SignUpPage(page).click_register_button()
    # Assert - Then
    assert page.is_visible(f"text={new_user.firstname}")


def test_new_user_can_successfully_sign_in(base_page, new_user) -> None:
    # Act - When/And
    LoginPage(base_page).login(new_user)
    # Assert - Then
    assert base_page.is_visible(
        f"text=Welcome {new_user.firstname} {new_user.lastname}"
    )
