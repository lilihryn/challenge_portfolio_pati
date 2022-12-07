import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class LoginPage(BasePage):
    login_field_xpath = "//input[@name='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    remind_password_url = "https://scouts-test.futbolkolektyw.pl/en/remind"
    password_invalid_xpath = "//*[@id='__next']/form/div/div[1]/div[3]/span"
    expected_text_wrong_password = 'Identifier or password invalid.'
    remind_password_xpath = '//*[@id="__next"]/form/div/div[1]/a'
    title_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    expected_text_remind = 'Remind password'
    expected_text_remind_polish = 'Przypomnij hasło'
    expected_text_remind_english = 'Remind password'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    button_language_xpath = "//div[@role='button']"
    list_dropdown_xpath = "//ul[@role='listbox']"
    button_language_english_xpath = "//li[@data-value='en']"
    expected_english_xpath = " //div[text()='English']"
    button_language_polish_xpath = "//li[@data-value='pl']"
    expected_polish_xpath = " //div[text()='Polski']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_login_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def wait_to_click_sign_in_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((DEFAULT_LOCATOR_TYPE, "//button[@type='submit']"))).click()

    def wait_to_find_title(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.title_is(self.expected_title))

    def check_the_credentials(self):
        time.sleep(5)
        self.assert_element_text(self.driver, self.remind_password_xpath, self.expected_text_remind)

    def click_remind_password(self):
        self.wait_for_element_to_be_clickable(self.remind_password_xpath)
        self.click_on_the_element(self.remind_password_xpath)

    def title_of_remind_password_page(self):
        assert self.get_page_title(self.remind_password_url) == self.expected_text_remind

    def change_the_language(self):
        self.click_on_the_element(self.button_language_xpath)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((DEFAULT_LOCATOR_TYPE, "//ul[@role='listbox']")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='pl']"))).click()
        time.sleep(8)

