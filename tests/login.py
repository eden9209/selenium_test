from selenium import webdriver
import time
import unittest
from pages.login_page import login_page
from pages.home_page import home_page


class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/edens/pythonProject/pythonProject/drivers/chromedriver.exe")
        cls.driver.maximize_window()

    def test_validation_login(self):
        driver = self.driver
        driver.get(r"https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
        # object for login page
        l = login_page(driver)
        l.enter_user("Admin")
        l.enter_password("admin123")
        l.clicked()
        # object for home page
        h = home_page(driver)
        h.click_welcome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("login test complete")


if __name__ == '__main__':
    unittest.main()
