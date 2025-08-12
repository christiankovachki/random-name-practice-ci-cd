from playwright.sync_api import Page

from pages.base_page import BasePage


class NavigationBar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        __locator = page.locator("li")
        self.HOME_LINK = __locator.filter(has_text="Home")
        self.PRODUCTS_LINK = __locator.filter(has_text="Products")
        self.CART_LINK = __locator.filter(has_text="Cart")
        self.SIGNUP_LOGIN_LINK = __locator.filter(has_text="Signup / Login")
        self.TEST_CASES_LINK = __locator.filter(has_text="Test Cases")
        self.API_TESTING_LINK = __locator.filter(has_text="API Testing")
        self.VIDEO_TUTORIALS_LINK = __locator.filter(has_text="Video Tutorials")
        self.CONTACT_US_LINK = __locator.filter(has_text="Contact us")
        self.DELETE_ACCOUNT_LINK = __locator.filter(has_text="Delete Account")
        self.LOGOUT_LINK = __locator.filter(has_text="Logout")
        self.LOGGED_IN_AS_USER = __locator.filter(has_text="Logged in as")

    def click_nav_bar_link_by_name(self, name: str):
        element = self.page.locator("li").filter(has_text=f"{name}")
        self.click_on_element(element)

    def verify_nav_bar_link_is_visible(self, name: str):
        element = self.page.locator("li").filter(has_text=f"{name}")
        self.verify_element_is_visible(element)

    def verify_nav_bar_link_is_not_visible(self, name: str):
        element = self.page.locator("li").filter(has_text=f"{name}")
        self.verify_element_is_not_visible(element)

    def verify_logged_in_as_user(self, username: str):
        self.verify_element_text(self.LOGGED_IN_AS_USER, f"Logged in as {username}")
