class MainPage:
    def __init__(self, page):
        self.open_account_button = page.locator("//a[text()='Open New Account']")
        self.accounts_overview_button = page.locator("//a[text()='Accounts Overview']")
        self.transfer_funds_button = page.locator("//a[text()='Transfer Funds']")
        self.bill_pay_button = page.locator("//a[text()='Bill Pay']")

    def click_open_account_button(self):
        self.open_account_button.click()

    def click_accounts_overview_button(self):
        self.accounts_overview_button.click()

    def click_transfer_funds_button(self):
        self.transfer_funds_button.click()

    def click_bill_pay_button(self):
        self.bill_pay_button.click()
