import os

from context_config import WebContext
from factories.user_factory import UserFactory


def test_search_products_and_verify_cart_after_login(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.verify_all_products_heading_is_visible()

    product = "Jeans"
    ctx.all_products_page.populate_search_input(product)
    ctx.all_products_page.click_search_button()

    ctx.searched_products_page.verify_searched_products_heading_is_visible()
    ctx.searched_products_page.verify_search_results(product, exact_match=False)

    count_of_products_to_be_added = ctx.all_products_page.get_products_count()
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=count_of_products_to_be_added)
    ctx.view_cart_page.verify_products_in_cart(added_items)

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.login_existing_user()
    username = UserFactory.get_existing_user_username()
    ctx.navigation_bar.verify_logged_in_as_user(username)

    ctx.navigation_bar.click_nav_bar_link_by_name("Cart")
    ctx.view_cart_page.verify_products_in_cart(added_items)
    ctx.view_cart_page.delete_products_in_cart(added_items)
    ctx.view_cart_page.verify_cart_is_empty()
