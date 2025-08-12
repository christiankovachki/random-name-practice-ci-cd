from playwright.sync_api import Page

from models.user import User
from pages.base_page import BasePage
from pages.signup_login_page import SignupLoginPage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.MR_RADIO_BUTTON = page.get_by_role(role="radio", name="Mr.")
        self.MRS_RADIO_BUTTON = page.get_by_role(role="radio", name="Mrs.")
        self.NAME_INPUT = page.get_by_test_id("name")
        self.EMAIL_INPUT = page.get_by_test_id("email")
        self.PASSWORD_INPUT = page.get_by_test_id("password")
        self.DOB_DAY_DROPDOWN = page.get_by_test_id("days")
        self.DOB_MONTH_DROPDOWN = page.get_by_test_id("months")
        self.DOB_YEAR_DROPDOWN = page.get_by_test_id("years")
        self.NEWSLETTER_CHECKBOX = page.get_by_role(role="checkbox", name="newsletter")
        self.SPECIAL_OFFERS_CHECKBOX = page.get_by_role(role="checkbox", name="special offers")
        self.FIRST_NAME_INPUT = page.get_by_test_id("first_name")
        self.LAST_NAME_INPUT = page.get_by_test_id("last_name")
        self.COMPANY_INPUT = page.get_by_test_id("company")
        self.MANDATORY_ADDRESS_INPUT = page.get_by_test_id("address")
        self.OPTIONAL_ADDRESS_INPUT = page.get_by_test_id("address2")
        self.COUNTRY_DROPDOWN = page.get_by_test_id("country")
        self.STATE_INPUT = page.get_by_test_id("state")
        self.CITY_INPUT = page.get_by_test_id("city")
        self.ZIPCODE_INPUT = page.get_by_test_id("zipcode")
        self.MOBILE_NUMBER_INPUT = page.get_by_test_id("mobile_number")
        self.CREATE_ACCOUNT_BUTTON = page.get_by_test_id("create-account")
        self.signup_login_page = SignupLoginPage(page)

    def populate_account_information_details(self,
                                             user: User,
                                             subscribe_newsletter: bool = True,
                                             accept_special_offers: bool = True):
        self._select_title(user.title)
        self.type_text_in_input_field(self.PASSWORD_INPUT, user.password)
        self.select_dropdown_option(self.DOB_DAY_DROPDOWN, user.day_of_birth)
        self.select_dropdown_option(self.DOB_MONTH_DROPDOWN, user.month_of_birth)
        self.select_dropdown_option(self.DOB_YEAR_DROPDOWN, user.year_of_birth)
        self._handle_newsletter_checkbox(subscribe_newsletter)
        self._handle_special_offers_checkbox(accept_special_offers)

    def populate_address_information_details(self, user: User):
        self.type_text_in_input_field(self.FIRST_NAME_INPUT, user.first_name)
        self.type_text_in_input_field(self.LAST_NAME_INPUT, user.last_name)
        if user.company:
            self.type_text_in_input_field(self.COMPANY_INPUT, user.company)
        self.type_text_in_input_field(self.MANDATORY_ADDRESS_INPUT, user.address)
        if user.second_address:
            self.type_text_in_input_field(self.OPTIONAL_ADDRESS_INPUT, user.second_address)
        self.select_dropdown_option(self.COUNTRY_DROPDOWN, user.country)
        self.type_text_in_input_field(self.STATE_INPUT, user.state)
        self.type_text_in_input_field(self.CITY_INPUT, user.city)
        self.type_text_in_input_field(self.ZIPCODE_INPUT, user.zipcode)
        self.type_text_in_input_field(self.MOBILE_NUMBER_INPUT, user.mobile_number)

    def click_create_account_button(self):
        self.click_on_element(self.CREATE_ACCOUNT_BUTTON)

    def signup_new_user(self, user: User):
        self.signup_login_page.populate_signup_form(user.username, user.email)
        self.signup_login_page.click_signup_button()
        self.populate_account_information_details(user)
        self.populate_address_information_details(user)
        self.click_create_account_button()

    def _select_title(self, title: str):
        if title == "Mr.":
            self.check_checkbox(self.MR_RADIO_BUTTON)
        elif title == "Mrs.":
            self.check_checkbox(self.MRS_RADIO_BUTTON)
        else:
            raise ValueError(f"Unsupported title: '{title}'. Expected 'Mr' or 'Mrs.'")

    def _handle_newsletter_checkbox(self, sign_up: bool):
        if sign_up:
            self.check_checkbox(self.NEWSLETTER_CHECKBOX)
        else:
            self.uncheck_checkbox(self.NEWSLETTER_CHECKBOX)

    def _handle_special_offers_checkbox(self, accept: bool):
        if accept:
            self.check_checkbox(self.SPECIAL_OFFERS_CHECKBOX)
        else:
            self.uncheck_checkbox(self.SPECIAL_OFFERS_CHECKBOX)
