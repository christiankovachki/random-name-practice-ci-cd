from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from pages.table_page import Table


class ViewCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.CART_TABLE = Table(page, "[id^='cart_info']")
        self.CHECKOUT_BUTTON = page.get_by_text(text='Proceed To Checkout')
        # MOVE OUTSIDE THIS POM
        self.REGISTER_LOGIN_LINK = page.get_by_role(role="link", name="Register / Login")

    def click_checkout_button(self):
        self.click_on_element(self.CHECKOUT_BUTTON)

    # MOVE OUTSIDE THIS POM
    def click_register_login_link(self):
        self.click_on_element(self.REGISTER_LOGIN_LINK)

    def delete_products_in_cart(self, products: list[dict]):
        for product in products:
            product_name = product.get("name")
            delete_button = self.CART_TABLE.get_cell(row_value=product_name, column_name="")
            self.click_on_element(delete_button)

    def verify_products_in_cart(self, added_items: list[dict]):
        for expected in added_items:
            product_name = expected.get("name")
            product_price = expected.get("price")
            product_quantity = expected.get("quantity")
            product_total_price = self._calculate_expected_total_per_product(product_price, product_quantity)

            self.verify_product_name_in_cart(product_name)
            self.verify_product_price_in_cart(product_name, product_price)
            self.verify_product_quantity_in_cart(product_name, product_quantity)
            self.verify_product_price_in_cart(product_name, product_total_price)

    def verify_product_name_in_cart(self, product_name: str):
        actual_name = self.CART_TABLE.get_cell(
            row_value=product_name,
            column_name="Description").locator("a").text_content().strip()
        assert actual_name == product_name, (
            f"Expected the name of the product to be '{product_name}' but instead got '{actual_name}'"
        )

    def verify_product_price_in_cart(self, product_name: str, expected_price: str):
        actual_price = self.CART_TABLE.get_cell(
            row_value=product_name,
            column_name="Price").locator("p").text_content().strip()
        assert actual_price == expected_price, (
            f"Expected the price of {product_name} to be '{expected_price}' but instead got '{actual_price}'"
        )

    def verify_product_quantity_in_cart(self, product_name: str, expected_quantity: str):
        actual_quantity = self.CART_TABLE.get_cell(
            row_value=product_name,
            column_name="Quantity").text_content().strip()
        assert actual_quantity == expected_quantity, (
            f"Expected quantity of '{expected_quantity}' for product '{product_name}' but instead got '{actual_quantity}'"
        )

    def verify_product_total_price_in_cart(self, product_name: str, expected_total_price: str):
        actual_total_price = self.CART_TABLE.get_cell(
            row_value=product_name,
            column_name="Total").locator("p").text_content().strip()
        assert actual_total_price == expected_total_price, (
            f"Expected the total price of {product_name} to be '{expected_total_price}' but instead got '{actual_total_price}'"
        )

    def verify_cart_is_empty(self):
        self.CART_TABLE.verify_table_empty()

    def get_cart_total_price_of_products(self):
        cells = self.CART_TABLE.get_column_cells(column_name="Total")
        total = 0
        for cell in cells:
            price = int(cell.text_content().replace("Rs. ", "").strip())
            total += price

        return f"Rs. {total}"

    def _calculate_expected_total_per_product(self, product_price: str, expected_quantity: str):
        price = product_price.replace("Rs. ", "").strip()
        total = int(price) * int(expected_quantity)
        return f"Rs. {total}"
