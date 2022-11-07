from pages.base_page import BasePage


class Dashboard(BasePage):

    button_main = "// div[contains (@class, 'MuiListItemIcon-root')]"
    button_players = "//span[text()='Players' or text()='Gracze']"
    players_count = "//div[text()='Players count' or text()='Ilość graczy']"
    number_players = "//b[number()= '766']"
    matches_count = "//div[text()='Matches count' or text()='Ilość meczy']"
    number_matches = "//b[number()= '113']"
    reports_count = "//div[text()= 'Reports count' or text()='Ilość raportów']"
    number_reports = "//b[number()= '135']"
    events_count = "//div[text()= 'Events count' or text()='Ilość akcji']"
    number_events = "//b[number()= '156']"
    button_language = "//span[text()='Polski' or 'English']"
    button_sign_out = "//span[text()='Sign out']"
    button_dev_team_contact = "//span[text()='Dev team contact']"
    button_upd_player = "//span[text()='Add player']"
    button_last_crt_player = "//h6[text()='Last created player']"
    button_last_crt_match = "//h6[text()='Last created match']"
    button_last_upd_match = "//h6[text()='Last updated match']"
    button_last_upd_report = "//h6[text()='Last updated report']"
    button_add_player = "//span[text()='Add player']"
    image_logo = "//div[@title='Logo Scouts Panel']"
