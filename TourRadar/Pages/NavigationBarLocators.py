class NavigationBarLocators:
    profile_btn = "//div[contains(@class, 'profile-placeholder')]"
    destinations_btn = "//*[@data-type='destinations']/a"
    destinations_subitem = "//*[contains(@class, 'dropdown-submenu-item')]/a[1]"
    login_btn = "//ul//a[contains(@href,'login')] [contains(@class, 'dropdown')]"
    singup_btn = "//ul//a[contains(@href,'registration')] [contains(@class, 'dropdown')]"
    radiobtn_traveller = '//*[@id="traveller"]'
    radiobtn_guide = '//*[@id="guide"]'
    form_fullname = "//*[@placeholder='Full name']"
    form_email = "//*[@placeholder='Enter your email']"
    form_login_email = "//*[@placeholder='Enter your Email or Username']"
    form_password = '//*[@placeholder="Enter password"]'
    form_repeat_password = '//*[@placeholder="Repeat password"]'
    form_send_btn = '//*[@id="g_send"]/span'
    saved_tours = " //*//li[contains(@class, 'ao-header-navigation__wishlist')]"

