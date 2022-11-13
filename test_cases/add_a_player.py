import os
import time
import unittest
from selenium import webdriver

from pages.add_a_player_page import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

        user_add_a_player = AddAPlayer(self.driver)
        user_add_a_player.player_add_button()
        user_add_a_player.player_name('Liliia')
        user_add_a_player.player_surname('Hryniuk1')
        user_add_a_player.player_age('13.12.1988')
        user_add_a_player.player_position('Defender')
        user_add_a_player.button_submit()
        user_add_a_player.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

