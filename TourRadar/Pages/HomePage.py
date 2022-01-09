from TourRadar.Pages.HomePageLocators import HomePageLocators
from TourRadar.Pages.NavigationBarLocators import NavigationBarLocators
from selenium.webdriver.common.keys import Keys
import time


class Home:
    def select_where_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_where).send_keys('Poland')
        self.driver.find_element_by_xpath(HomePageLocators.search_where).send_keys(Keys.TAB)
        time.sleep(2)

    def select_when_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_when).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(HomePageLocators.search_month).click()

    def select_who_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_who).click()
        time.sleep(1)

    def click_search_btn(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_btn).click()
        time.sleep(2)

    def click_first_wishlist_icon(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(HomePageLocators.search_icon_wishlist).click()

    def click_navbar_wishlist_icon(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.saved_tours).click()

    def click_first_tour_view(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(HomePageLocators.tour_view_btn).click()

    def click_tour_wishlist_icon(self):
        p = self.driver.current_window_handle
        chwd = self.driver.window_handles
        for w in chwd:
            if (w != p):
                self.driver.switch_to.window(w)
        time.sleep(1)
        element = self.driver.find_element_by_xpath("//*[contains(@class, 'price-block')]")
        element.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.find_element_by_xpath(HomePageLocators.tour_view_wishlist_button).click()

    def get_search_result_title_text(self):
        search_text = self.driver.find_element_by_xpath(HomePageLocators.search_title_result).text
        return search_text

    def select_budget_range(self):
        self.driver.get(self.driver.current_url + "#budget=1000-1500")
        self.driver.refresh()

    def get_all_description_values(self):
        return self.driver.find_elements_by_xpath(HomePageLocators.description_value)

    def assert_budget_range(self):
        time.sleep(2)
        values = Home.get_all_description_values(self)
        print(values)
        for value in values:
            print(value.text)
            if int(value.text.replace(',', '')) > 1000 and int(value.text.replace(',', '')) < 1500:
                print("1000 < ",  value.text.replace(',', ''), " < 1500")
            else:
                print("Assertion failure")
                return False