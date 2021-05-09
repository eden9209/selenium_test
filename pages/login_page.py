from locators.locators import locators


class login_page:
    def __init__(self, driver):
        self.driver = driver
        self.user = locators.user_input_id
        self.password = locators.user_password_id
        self.button = locators.user_button_id

    def enter_user(self, name):
        self.driver.find_element_by_id(self.user).clear()
        self.driver.find_element_by_id(self.user).send_keys(name)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    def clicked(self):
        self.driver.find_element_by_id(self.button).click()
