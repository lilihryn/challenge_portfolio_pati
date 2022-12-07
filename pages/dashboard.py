from pages.base_page import BasePage


class Dashboard(BasePage):
    button_main_xpath = "// div[contains (@class, 'MuiListItemIcon-root')]"
    button_players_xpath = "//span[text()='Players' or text()='Gracze']"
    players_count_xpath = "//div[text()='Players count' or text()='Ilość graczy']"
    number_players_xpath = "//b[number()= '766']"
    matches_count_xpath = "//div[text()='Matches count' or text()='Ilość meczy']"
    number_matches_xpath = "//b[number()= '113']"
    reports_count_xpath = "//div[text()= 'Reports count' or text()='Ilość raportów']"
    number_reports_xpath = "//b[number()= '135']"
    events_count_xpath = "//div[text()= 'Events count' or text()='Ilość akcji']"
    number_events_xpath = "//b[number()= '156']"
    button_language_xpath = "//span[text()='Polski' or 'English']"
    button_sign_out_xpath = "//span[text()='Sign out']"
    button_dev_team_contact_xpath = "//span[text()='Dev team contact']"
    button_upd_player_xpath = "//span[text()='Add player']"
    button_last_crt_player_xpath = "//h6[text()='Last created player']"
    button_last_crt_match_xpath = "//h6[text()='Last created match']"
    button_last_upd_match_xpath = "//h6[text()='Last updated match']"
    button_last_upd_report_xpath = "//h6[text()='Last updated report']"
    button_add_player_xpath = "//span[text()='Add player']"
    image_logo_xpath = "//div[@title='Logo Scouts Panel']"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    expected_title = "Scouts panel"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.button_add_player_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.button_add_player_xpath)

    def sign_out_from_the_system(self):
        self.click_on_the_element(self.button_sign_out_xpath)
