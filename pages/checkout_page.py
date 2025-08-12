from playwright.sync_api import Page

from models.user import User
from pages.base_page import BasePage
from pages.table_page import Table


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.CART_TABLE = Table(page, "#cart_info")
        self.DELIVERY_ADDRESS_HEADER = page.get_by_text(text='Your delivery address')
        self.DELIVERY_ADDRESS_SECTION = self.page.locator("#address_delivery")
        self.BILLING_ADDRESS_HEADER = page.get_by_text(text='Your billing address')
        self.BILLING_ADDRESS_SECTION = self.page.locator("#address_invoice")
        self.REVIEW_ORDER_HEADER = page.get_by_role(role="heading", name="Review Your Order")
        self.TOTAL_AMOUNT = page.locator("td:has-text('Total Amount') + td .cart_total_price")
        self.ORDER_COMMENT_TEXTAREA = page.locator("textarea[name='message']")
        self.PLACE_ORDER_BUTTON = page.get_by_text(text="Place Order")

    def click_place_order_button(self):
        self.click_on_element(self.PLACE_ORDER_BUTTON)

    def populate_order_comment_textarea(self, text: str):
        self.type_text_in_input_field(self.ORDER_COMMENT_TEXTAREA, text)

    def verify_user_address(self, user: User, address_type: str):
        address_type = address_type.upper()
        if address_type not in ("DELIVERY", "BILLING"):
            raise ValueError(
                f"Invalid address_type: '{address_type}'. Must be 'delivery' or 'billing'")

        if address_type == "DELIVERY":
            self.verify_element_is_visible(self.DELIVERY_ADDRESS_HEADER)
            section_locator = self.DELIVERY_ADDRESS_SECTION
        else:
            self.verify_element_is_visible(self.BILLING_ADDRESS_HEADER)
            section_locator = self.BILLING_ADDRESS_SECTION

        locators = section_locator.locator("li").all()

        expected_field_values = {
            1: ("Title/Full Name", f"{user.title} {user.first_name} {user.last_name}"),
            2: ("Company", user.company),
            3: ("First Address", user.address),
            4: ("Second Address", user.second_address),
            5: ("City/State/Zip", f"{user.city} {user.state} {user.zipcode}"),
            6: ("Country", user.country),
            7: ("Mobile Number", user.mobile_number)
        }

        for position, (field_name, expected_value) in expected_field_values.items():
            self.verify_element_text(locators[position], expected_value)

    def verify_products_total_amount(self, expected_total: str):
        self.verify_element_text(self.TOTAL_AMOUNT, expected_total)
