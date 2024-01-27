class LoginPage:
    def __init__(self, page):
        self.login_header = page.locator("//*[text()='Customer Login']")
        self.login_button = page.locator("//input[@value='Log In']")
        self.username_field = page.locator("//input[@name='username']")
        self.password_field = page.locator("//input[@name='password']")
        self.register_button = page.locator("//a[text()='Register']")

    def login(self, user):
        self.username_field.fill(user.username)
        self.password_field.fill(user.password)
        self.login_button.click()

    def click_register_button(self):
        self.register_button.click()
