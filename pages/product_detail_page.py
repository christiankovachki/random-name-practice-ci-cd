from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.PRODUCT = page.locator(".product-information")
        self.PRODUCT_NAME = self.PRODUCT.get_by_role(role="heading", level=2)
        self.PRODUCT_CATEGORY = self.PRODUCT.get_by_role("paragraph").filter(has_text="Category:")
        self.PRODUCT_PRICE = self.PRODUCT.get_by_text("Rs.")
        self.QUANTITY_INPUT = page.locator("#quantity")
        self.ADD_TO_CART_BUTTON = self.page.get_by_role(role="button", name="Add to cart")
        self.PRODUCT_AVAILABILITY = self.PRODUCT.get_by_role("paragraph").filter( has_text="Availability:")
        self.PRODUCT_CONDITION = self.PRODUCT.get_by_role("paragraph").filter( has_text="Condition:")
        self.PRODUCT_BRAND = self.PRODUCT.get_by_role("paragraph").filter( has_text="Brand:")

    def click_add_to_cart_button(self):
        self.click_on_element(self.ADD_TO_CART_BUTTON)

    def get_product_name(self):
        return self.get_element_text_content(self.PRODUCT_NAME)

    def adjust_product_quantity(self, quantity: str):
        self.type_text_in_input_field(self.QUANTITY_INPUT, "")
        self.type_text_in_input_field(self.QUANTITY_INPUT, quantity)

    def verify_all_product_details_are_visible(self):
        elements = {
            "Product Name": self.PRODUCT_NAME,
            "Product Category": self.PRODUCT_CATEGORY,
            "Product Price": self.PRODUCT_PRICE,
            "Availability": self.PRODUCT_AVAILABILITY,
            "Condition": self.PRODUCT_CONDITION,
            "Brand": self.PRODUCT_BRAND
        }

        for name, element in elements.items():
            try:
                self.verify_element_is_visible(element)
            except AssertionError:
                raise AssertionError(f"Product detail not visible: {name}")
