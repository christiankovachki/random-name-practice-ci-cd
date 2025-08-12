from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class AllProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.ALL_PRODUCTS_HEADER = page.get_by_role(role="heading", name="All Products")
        self.ALL_PRODUCTS_CARDS = page.locator(".features_items div[class^='productinfo']")
        self.PRODUCT_VIEW_BUTTON = page.get_by_text(text="View Product")
        self.PRODUCT_ADD_TO_CART_BUTTON = self.ALL_PRODUCTS_CARDS.get_by_text(text="Add to cart")
        self.SEARCH_INPUT = page.locator("#search_product")
        self.SEARCH_BUTTON = page.locator("#submit_search")
        self.CONTINUE_SHOPPING_BUTTON = page.get_by_text(text="Continue Shopping")
        self.VIEW_CART_LINK = page.get_by_role(role="link", name="View Cart")

    def click_product_view_button(self, product_number):
        element = self.PRODUCT_VIEW_BUTTON.nth(product_number - 1)
        self.click_on_element(element)

    def click_continue_shopping_button(self):
        self.click_on_element(self.CONTINUE_SHOPPING_BUTTON)

    def click_view_cart_link(self):
        self.click_on_element(self.VIEW_CART_LINK)

    def add_products_in_cart(self, number_of_products: int):
        added_products = []
        product_index = 0
        while product_index < number_of_products:
            product_card = self.ALL_PRODUCTS_CARDS.nth(product_index)
            self.hover_over_element(product_card)
            product_price = product_card.get_by_role(role="heading", level=2).inner_text().strip()
            product_name = product_card.get_by_role(role="paragraph").inner_text().strip()

            added_products.append({
                'name': product_name,
                'price': product_price,
                'quantity': "1"
            })

            self.click_on_element(self.PRODUCT_ADD_TO_CART_BUTTON.nth(product_index))

            if product_index == number_of_products - 1:
                self.click_view_cart_link()
            else:
                self.click_continue_shopping_button()

            product_index += 1

        return added_products

    def click_search_button(self):
        self.click_on_element(self.SEARCH_BUTTON)

    def populate_search_input(self, text: str):
        self.type_text_in_input_field(self.SEARCH_INPUT, text)

    def get_products_count(self) -> int:
        expect(self.ALL_PRODUCTS_CARDS).not_to_have_count(0)
        return self.ALL_PRODUCTS_CARDS.count()

    def verify_all_products_heading_is_visible(self):
        self.verify_element_is_visible(self.ALL_PRODUCTS_HEADER)
