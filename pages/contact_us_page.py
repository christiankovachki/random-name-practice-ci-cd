from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.GET_IN_TOUCH_HEADER = page.get_by_role(role="heading", name="Get In Touch")
        self.NAME_INPUT = page.get_by_test_id("name")
        self.EMAIL_INPUT = page.get_by_test_id("email")
        self.SUBJECT_INPUT = page.get_by_test_id("subject")
        self.MESSAGE_INPUT = page.get_by_test_id("message")
        self.FILE_UPLOAD_INPUT = page.get_by_role(role="button", name="Choose File")
        self.SUBMIT_BUTTON = page.get_by_test_id("submit-button")
        self.SUCCESS_ALERT = page.locator("#contact-page").get_by_text(
            "Success! Your details have been submitted successfully.")
        self.HOME_BUTTON = page.locator("#form-section").get_by_text(text="Home")

    def populate_contact_us_form_details(self, name: str, email: str, subject: str, message: str):
        self.type_text_in_input_field(self.NAME_INPUT, name)
        self.type_text_in_input_field(self.EMAIL_INPUT, email)
        self.type_text_in_input_field(self.SUBJECT_INPUT, subject)
        self.type_text_in_input_field(self.MESSAGE_INPUT, message)

    def click_submit_button(self):
        self.page.wait_for_timeout(timeout=500)
        self.click_on_element(self.SUBMIT_BUTTON)

    def click_home_button(self):
        self.click_on_element(self.HOME_BUTTON)

    def upload_contact_us_form_file(self, file_path: str):
        self.upload_file(self.FILE_UPLOAD_INPUT, file_path)

    def verify_get_in_touch_heading_is_visible(self):
        self.verify_element_is_visible(self.GET_IN_TOUCH_HEADER)

    def verify_success_alert_is_visible(self):
        self.verify_element_is_visible(self.SUCCESS_ALERT)