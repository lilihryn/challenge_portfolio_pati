from pages.base_page import BasePage


class AddMatch(BasePage):
    button_add_match_player = " //div[contains (@class, 'MuiCardHeader-content')]"
    input_my_team = "//input[@name='myTeam']"
    input_my_enemy = "//input[@name='enemyTeam']"
    input_my_score = "//input[@name='myTeamScore']"
    input_enemy_score = "//input[@name='enemyTeamScore']"
    input_date = "//input[@name='date']"
    input_tshirt = "//input[@name='tshirt']"
    input_league = "//input[@name='league']"
    input_time_played = "//input[@name='timePlayed'] "
    input_number = " //input[@name='number'] "
    input_webMatch = "//input[@name='webMatch'] "
    input_general = "//input[@name='general'] "
    input_rating = " //input[@name='rating'] "
    button_match_at_home = "//input[@name='matchAtHome' and @value='true']"
    button_match_out_home = "//input[@name='matchAtHome' and @value='false']"
    button_submit = "//button[@type='submit']"
    button_clear = "//span[ text()= 'Clear'] "


