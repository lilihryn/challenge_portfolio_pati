import os
import time
import unittest

from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    def test_check_the_title(self):
        user_login = LoginPage(self.driver)
        user_login.wait_to_find_title()

    def test_wrong_credentials(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.type_in_email("")
        user_login.type_in_password("")
        user_login.click_on_sign_in_button()
        user_login.check_the_credentials()

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.type_in_email("")
        user_login.type_in_password("")
        user_login.click_on_sign_in_button()
        user_login.check_the_credentials()
        user_login.click_remind_password()
        user_login.title_of_remind_password_page()
        time.sleep(5)

    def test_change_the_language(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_login_page()
        user_login.change_the_language()



    @classmethod
    def tearDown(self):
        self.driver.quit()
