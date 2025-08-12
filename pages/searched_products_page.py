from playwright.sync_api import Page

from pages.base_page import BasePage


class SearchedProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SEARCHED_PRODUCTS_HEADER = page.get_by_role(role="heading", name="Searched Products")
        self.SEARCHED_PRODUCTS_CARDS = page.locator(".features_items div[class^='productinfo']")
        self.SEARCHED_PRODUCTS_NAMES = self.SEARCHED_PRODUCTS_CARDS.get_by_role("paragraph")

    def verify_search_results(self, product_name: str, exact_match: bool = True):
        products = self.SEARCHED_PRODUCTS_NAMES.all()

        for product in products:
            if exact_match:
                self.verify_element_text(product, product_name)
            else:
                self.verify_element_contains_text(product, product_name)

    def verify_searched_products_heading_is_visible(self):
        self.verify_element_is_visible(self.SEARCHED_PRODUCTS_HEADER)
