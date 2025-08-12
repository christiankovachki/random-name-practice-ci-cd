from playwright.sync_api import Page

from models.user import User
from pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.CARD_NAME_INPUT = page.get_by_test_id("name-on-card")
        self.CARD_NUMBER_INPUT = page.get_by_test_id("card-number")
        self.CVC_INPUT = page.get_by_test_id("cvc")
        self.CARD_EXPIRATION_MONTH_INPUT = page.get_by_test_id("expiry-month")
        self.CARD_EXPIRATION_YEAR_INPUT = page.get_by_test_id("expiry-year")
        self.PAY_BUTTON = page.get_by_test_id("pay-button")
        self.CONFIRMED_ORDER_SUCCESS_MESSAGE = page.get_by_text(text="Congratulations! Your order has been confirmed!")
        self.CONTINUE_BUTTON = page.get_by_test_id("continue-button")

    def click_pay_button(self):
        self.click_on_element(self.PAY_BUTTON)

    def click_continue_button(self):
        self.click_on_element(self.CONTINUE_BUTTON)

    def populate_payment_details(self, user: User, card_details: dict):
        self.type_text_in_input_field(self.CARD_NAME_INPUT,
                                f"{user.first_name.upper()} {user.last_name.upper()}")
        self.type_text_in_input_field(self.CARD_NUMBER_INPUT,
                                      card_details.get("card_number"))
        self.type_text_in_input_field(self.CVC_INPUT,
                                      card_details.get("card_cvc"))
        self.type_text_in_input_field(self.CARD_EXPIRATION_MONTH_INPUT,
                                      card_details.get("card_expiration_month"))
        self.type_text_in_input_field(self.CARD_EXPIRATION_YEAR_INPUT,
                                      card_details.get("card_expiration_year"))

    def verify_confirmed_order_success_message_is_visible(self):
        self.verify_element_is_visible(self.CONFIRMED_ORDER_SUCCESS_MESSAGE)
