from playwright.sync_api import Page

from pages.all_products_page import AllProductsPage
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.contact_us_page import ContactUsPage
from pages.created_deleted_account_page import CreatedDeletedAccountPage
from pages.navigation_bar import NavigationBar
from pages.payment_page import PaymentPage
from pages.product_detail_page import ProductDetailPage
from pages.searched_products_page import SearchedProductsPage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage


class WebContext:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_page = BasePage(page)
        self.navigation_bar = NavigationBar(page)
        self.signup_login_page = SignupLoginPage(page)
        self.signup_page = SignupPage(page)
        self.created_deleted_account_page = CreatedDeletedAccountPage(page)
        self.contact_us_page = ContactUsPage(page)
        self.all_products_page = AllProductsPage(page)
        self.product_detail_page = ProductDetailPage(page)
        self.searched_products_page = SearchedProductsPage(page)
        self.view_cart_page = ViewCartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.payment_page = PaymentPage(page)
