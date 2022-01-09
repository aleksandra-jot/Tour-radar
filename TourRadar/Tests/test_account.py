from TourRadar.BaseSetup.BaseSetup import Base
from TourRadar.Pages.NavigationBarPage import NavigationBar as NB
from TourRadar.Pages.AccountPage import Account
from TourRadar.Pages.HomePage import Home


class TestAccount(Base):
    def test_add_and_delete_item_from_saved_wishlist(self):
        NB.hover_action_profile_btn(self)
        NB.click_on_login(self)
        NB.fill_form_login_email(self)
        NB.fill_form_login_password(self)
        NB.click_send_form(self)
        Home.select_where_destination(self)
        Home.click_search_btn(self)
        Home.click_first_tour_view(self)
        Home.click_tour_wishlist_icon(self)
        Home.click_navbar_wishlist_icon(self)
        assert Account.count_wishlist_items(self) == 1
        Account.click_on_account_wishlist_icon(self)
        Account.click_on_modal_wishlist_icon(self)
        Account.click_on_modal_done_btn(self)
        assert Account.count_wishlist_items(self) == 0
