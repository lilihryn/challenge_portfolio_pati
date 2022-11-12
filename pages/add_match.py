from pages.base_page import BasePage


class AddMatch(BasePage):
    button_add_match_player_xpath = " //div[contains (@class, 'MuiCardHeader-content')]"
    input_my_team_xpath = "//input[@name='myTeam']"
    input_my_enemy_xpath = "//input[@name='enemyTeam']"
    input_my_score_xpath = "//input[@name='myTeamScore']"
    input_enemy_score_xpath = "//input[@name='enemyTeamScore']"
    input_date_xpath = "//input[@name='date']"
    input_tshirt_xpath = "//input[@name='tshirt']"
    input_league_xpath = "//input[@name='league']"
    input_time_played_xpath = "//input[@name='timePlayed'] "
    input_number_xpath = " //input[@name='number'] "
    input_webMatch_xpath = "//input[@name='webMatch'] "
    input_general_xpath = "//input[@name='general'] "
    input_rating_xpath = " //input[@name='rating'] "
    button_match_at_home_xpath = "//input[@name='matchAtHome' and @value='true']"
    button_match_out_home_xpath = "//input[@name='matchAtHome' and @value='false']"
    button_submit_xpath = "//button[@type='submit']"
    button_clear_xpath = "//span[ text()= 'Clear'] "
