class OpenAccountPage:
    def __init__(self, page):
        self.account_type_dropdown = page.locator("#type")
        self.from_account_dropdown = page.locator("#fromAccountId")
        self.open_new_account_button = page.locator("//input[@value='Open New Account']")
        self.new_account_id_text = page.locator("#newAccountId")

    def click_open_account_button(self):
        self.open_new_account_button.click()

    def return_new_account_id(self):
        return self.new_account_id_text.text_content()

    def open_account(self, type):
        self.account_type_dropdown.select_option(type)
        self.click_open_account_button()
        return self.return_new_account_id()
