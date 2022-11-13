import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    button_add_player = "//span[text()='Add player']"
    player_name_xpath = "//input[@name='name']"
    player_surname_xpath = "//input[@name='surname']"
    player_position_xpath = "//input[@name='mainPosition']"
    player_age_xpath = "//input[@name='age']"
    button_submit_player_xpath = "//button[@type='submit']"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    title_of_box_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"

    def player_add_button(self):
        self.click_on_the_element(self.button_add_player)

    def player_name(self, name):
        self.field_send_keys(self.player_name_xpath, name)

    def player_surname(self, surname):
        self.field_send_keys(self.player_surname_xpath, surname)

    def player_age(self, age):
        self.field_send_keys(self.player_age_xpath, age)

    def player_position(self, position):
        self.field_send_keys(self.player_position_xpath, position)

    def button_submit(self):
        self.click_on_the_element(self.button_submit_player_xpath)

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_player_url) == self.expected_title
