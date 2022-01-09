from TourRadar.Pages.AccountLocators import AccountLocators
import time

class Account:
    def get_greetings_txt(self):
        global greeting_text
        greeting_text = self.driver.find_element_by_xpath(AccountLocators.greeting_txt).text
        return greeting_text

    def click_on_account_wishlist_icon(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(AccountLocators.account_icon_wishlist).click()

    def click_on_modal_wishlist_icon(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(AccountLocators.modal_icon_wishlist).click()

    def click_on_modal_done_btn(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(AccountLocators.modal_done_btn).click()

    def count_wishlist_items(self):
        time.sleep(2)
        items = self.driver.find_elements_by_xpath(AccountLocators.saved_tour_items)
        print(items)
        len_items = len(items)
        print(len_items)
        return len_items
