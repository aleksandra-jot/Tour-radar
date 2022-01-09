from TourRadar.BaseSetup.BaseSetup import Base
from TourRadar.Pages.NavigationBarPage import NavigationBar as NB
from TourRadar.Pages.AccountPage import Account
from TourRadar.Pages.HomePage import Home


class TestHomePage(Base):
    def test_create_an_account(self):
        NB.hover_action_profile_btn(self)
        NB.click_on_signup(self)
        NB.check_as_traveller(self)
        NB.fill_form_full_name(self)
        NB.fill_form_email(self)
        NB.fill_form_password(self)
        NB.fill_form_repeat_password(self)
        NB.click_send_form(self)
        assert str(Account.get_greetings_txt(self)) == str("Hello " + NB.get_form_full_name(self) + "!")

    def test_search_for_a_trip(self):
        Home.click_search_btn(self)
        Home.select_where_destination(self)
        Home.click_search_btn(self)
        assert Home.get_search_result_title_text(self) == 'Poland Tours & Trips'

    def test_navbar_select_destination(self):
        NB.hover_action_destinations_btn(self)
        NB.click_first_destinations_subitem(self)
        assert Home.get_search_result_title_text(self) == 'South Africa Tours & Trips'

    def test_search_budget_filter(self):
        Home.click_search_btn(self)
        Home.select_where_destination(self)
        Home.click_search_btn(self)
        Home.select_budget_range(self)
        Home.assert_budget_range(self)


