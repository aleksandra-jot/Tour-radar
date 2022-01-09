from selenium.webdriver import ActionChains
import time
from TourRadar.Pages.NavigationBarLocators import NavigationBarLocators
from faker import Faker

f = Faker()

class NavigationBar:
    def __init__(self, driver):
        self.driver = driver

    def hover_action_profile_btn(self):
        actions = ActionChains(self.driver)
        hover = self.driver.find_element_by_xpath(NavigationBarLocators.profile_btn)
        actions.move_to_element(hover).perform()

    def click_on_signup(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(NavigationBarLocators.singup_btn).click()

    def click_on_login(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.login_btn).click()

    def check_as_traveller(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.radiobtn_traveller)

    def fill_form_full_name(self):
        time.sleep(1)
        global full_name
        full_name = f.name()
        self.driver.find_element_by_xpath(NavigationBarLocators.form_fullname).send_keys(full_name)

    def get_form_full_name(self):
        return full_name

    def fill_form_email(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(NavigationBarLocators.form_email).send_keys(f.pystr(5) + "@email.ghostinspector.com")

    def fill_form_login_email(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.form_login_email).send_keys("trav@email.ghostinspector.com")

    def fill_form_login_password(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.form_password).send_keys("haslo123")

    def fill_form_password(self):
        time.sleep(1)
        global password
        password = f.pystr(8)
        self.driver.find_element_by_xpath(NavigationBarLocators.form_password).send_keys(password)

    def fill_form_repeat_password(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(NavigationBarLocators.form_repeat_password).send_keys(password)

    def click_send_form(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(NavigationBarLocators.form_send_btn).click()
        time.sleep(3)

    def hover_action_destinations_btn(self):
        actions = ActionChains(self.driver)
        hover = self.driver.find_element_by_xpath(NavigationBarLocators.destinations_btn)
        actions.move_to_element(hover).perform()

    def click_first_destinations_subitem(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.destinations_subitem).click()