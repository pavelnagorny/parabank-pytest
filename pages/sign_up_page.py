class SignUpPage:
    def __init__(self, page):
        self.login_header = page.locator("//*[text()='Signing up is easy!']")
        self.first_name_field = page.locator("#customer\.firstName")
        self.last_name_field = page.locator("#customer\.lastName")
        self.address_field = page.locator("#customer\.address\.street")
        self.city_field = page.locator("#customer\.address\.city")
        self.state_field = page.locator("#customer\.address\.state")
        self.zip_code_field = page.locator("#customer\.address\.zipCode")
        self.phone_number_field = page.locator("#customer\.phoneNumber")
        self.ssn_field = page.locator("#customer\.ssn")
        self.username_field = page.locator("#customer\.username")
        self.password_field = page.locator("#customer\.password")
        self.confirm_password_field = page.locator("#repeatedPassword")
        self.register_button = page.locator("//input[@value='Register']")

    def fill_out_register_form(self, user):
        self.first_name_field.fill(user.firstname)
        self.last_name_field.fill(user.lastname)
        self.address_field.fill(user.address)
        self.city_field.fill(user.city)
        self.state_field.fill(user.state)
        self.zip_code_field.fill(user.zip_code)
        self.phone_number_field.fill(user.phone_number)
        self.ssn_field.fill(user.ssn)
        self.username_field.fill(user.username)
        self.password_field.fill(user.password)
        self.confirm_password_field.fill(user.password)

    def click_register_button(self):
        self.register_button.click()
