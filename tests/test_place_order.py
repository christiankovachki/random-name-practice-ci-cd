from context_config import WebContext
from factories.user_factory import UserFactory
from utilities.generators import Generators


def test_register_while_checkout(ctx: WebContext):
    user = UserFactory().create_user()

    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=product_number)

    ctx.view_cart_page.verify_products_in_cart(added_items)
    ctx.view_cart_page.click_checkout_button()

    ctx.view_cart_page.click_register_login_link()
    ctx.signup_page.signup_new_user(user)
    ctx.created_deleted_account_page.click_continue_button()
    ctx.navigation_bar.verify_logged_in_as_user(user.username)

    ctx.navigation_bar.click_nav_bar_link_by_name("Cart")
    ctx.view_cart_page.verify_products_in_cart(added_items)
    total_price = ctx.view_cart_page.get_cart_total_price_of_products()
    ctx.view_cart_page.click_checkout_button()

    ctx.checkout_page.verify_user_address(user, address_type="delivery")
    ctx.checkout_page.verify_user_address(user, address_type="billing")
    ctx.view_cart_page.verify_products_in_cart(added_items)
    ctx.checkout_page.verify_products_total_amount(expected_total=total_price)

    order_comment = Generators.generate_random_text()
    ctx.checkout_page.populate_order_comment_textarea(order_comment)
    ctx.checkout_page.click_place_order_button()

    card_details = Generators.generate_payment_card_details()
    ctx.payment_page.populate_payment_details(user, card_details)
    ctx.payment_page.click_pay_button()
    ctx.payment_page.verify_confirmed_order_success_message_is_visible()
    ctx.payment_page.click_continue_button()

    ctx.navigation_bar.click_nav_bar_link_by_name("Delete Account")
    ctx.created_deleted_account_page.verify_account_deleted_heading_is_visible()
    ctx.created_deleted_account_page.click_continue_button()

def test_register_before_checkout(ctx: WebContext):
    user = UserFactory().create_user()

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_page.signup_new_user(user)
    ctx.created_deleted_account_page.click_continue_button()
    ctx.navigation_bar.verify_logged_in_as_user(user.username)

    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=product_number)

    ctx.view_cart_page.verify_products_in_cart(added_items)
    total_price = ctx.view_cart_page.get_cart_total_price_of_products()
    ctx.view_cart_page.click_checkout_button()

    ctx.checkout_page.verify_user_address(user, address_type="delivery")
    ctx.checkout_page.verify_user_address(user, address_type="billing")
    ctx.view_cart_page.verify_products_in_cart(added_items)
    ctx.checkout_page.verify_products_total_amount(expected_total=total_price)

    order_comment = Generators.generate_random_text()
    ctx.checkout_page.populate_order_comment_textarea(order_comment)
    ctx.checkout_page.click_place_order_button()

    card_details = Generators.generate_payment_card_details()
    ctx.payment_page.populate_payment_details(user, card_details)
    ctx.payment_page.click_pay_button()
    ctx.payment_page.verify_confirmed_order_success_message_is_visible()
    ctx.payment_page.click_continue_button()

    ctx.navigation_bar.click_nav_bar_link_by_name("Delete Account")
    ctx.created_deleted_account_page.verify_account_deleted_heading_is_visible()
    ctx.created_deleted_account_page.click_continue_button()

def test_login_before_checkout(ctx: WebContext):
    user = UserFactory().create_user()

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.login_existing_user()

    username = UserFactory.get_existing_user_username()
    ctx.navigation_bar.verify_logged_in_as_user(username)

    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=product_number)

    ctx.view_cart_page.verify_products_in_cart(added_items)
    total_price = ctx.view_cart_page.get_cart_total_price_of_products()
    ctx.view_cart_page.click_checkout_button()

    ctx.view_cart_page.verify_products_in_cart(added_items)
    ctx.checkout_page.verify_products_total_amount(expected_total=total_price)
    ctx.checkout_page.click_place_order_button()

    card_details = Generators.generate_payment_card_details()
    ctx.payment_page.populate_payment_details(user, card_details)
    ctx.payment_page.click_pay_button()
    ctx.payment_page.verify_confirmed_order_success_message_is_visible()
    ctx.payment_page.click_continue_button()
