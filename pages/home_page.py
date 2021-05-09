from locators.locators import locators
import time


class home_page:
    def __init__(self, driver):
        self.driver = driver
        self.welcome = locators.welcome_id

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome).click()
        time.sleep(2)


