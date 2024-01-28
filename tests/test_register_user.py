from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


def test_new_user_can_successfully_register_to_app(home_page, new_user) -> None:
    # Assess - Given
    # Act - When/And
    LoginPage(home_page).click_register_button()
    sign_up_page = SignUpPage(home_page)
    sign_up_page.fill_out_register_form(new_user)
    sign_up_page.click_register_button()
    # Assert - Then
    assert home_page.is_visible(f"text={new_user.firstname}")


def test_new_user_can_successfully_sign_in(home_page, new_user) -> None:
    # Act - When/And
    LoginPage(home_page).login(new_user)
    # Assert - Then
    assert home_page.is_visible(
        f"text=Welcome {new_user.firstname} {new_user.lastname}"
    )
