from playwright.sync_api import Page

from pages.base_page import BasePage
from settings import settings


class SignupLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SIGNUP_FORM_HEADER = page.get_by_role(role="heading", name="New User Signup!")
        self.SIGNUP_NAME_INPUT = page.get_by_test_id("signup-name")
        self.SIGNUP_EMAIL_INPUT = page.get_by_test_id("signup-email")
        self.SIGNUP_BUTTON = page.get_by_test_id("signup-button")
        self.LOGIN_FORM_HEADER = page.get_by_role(role="heading", name="Login to your account")
        self.LOGIN_EMAIL_INPUT = page.get_by_test_id("login-email")
        self.LOGIN_PASSWORD_INPUT = page.get_by_test_id("login-password")
        self.LOGIN_BUTTON = page.get_by_test_id("login-button")
        self.EXISTING_EMAIL_ERROR_MSG = page.get_by_text(text='Email Address already exist!')
        self.INCORRECT_CREDS_ERROR_MSG = page.get_by_text(text='Your email or password is incorrect!')

    def populate_signup_form(self, username: str, email: str):
        self.type_text_in_input_field(self.SIGNUP_NAME_INPUT, username)
        self.type_text_in_input_field(self.SIGNUP_EMAIL_INPUT, email)

    def populate_login_form(self, email: str, password: str):
        self.type_text_in_input_field(self.LOGIN_EMAIL_INPUT, email)
        self.type_text_in_input_field(self.LOGIN_PASSWORD_INPUT, password)

    def click_signup_button(self):
        self.click_on_element(self.SIGNUP_BUTTON)

    def click_login_button(self):
        self.click_on_element(self.LOGIN_BUTTON)

    def login_existing_user(self):
        self.populate_login_form(settings.TEST_USER_EMAIL, settings.TEST_USER_PASSWORD)
        self.click_login_button()

    def verify_login_form_content_is_visible(self):
        self.verify_element_is_visible(self.LOGIN_FORM_HEADER)
        self.verify_element_is_visible(self.LOGIN_EMAIL_INPUT)
        self.verify_element_is_visible(self.LOGIN_PASSWORD_INPUT)

    def verify_existing_email_error_message_is_visible(self):
        self.verify_element_is_visible(self.EXISTING_EMAIL_ERROR_MSG)

    def verify_incorrect_credentials_error_message_is_visible(self):
        self.verify_element_is_visible(self.INCORRECT_CREDS_ERROR_MSG)
