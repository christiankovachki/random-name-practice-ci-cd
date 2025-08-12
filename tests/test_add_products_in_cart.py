from context_config import WebContext
from utilities.generators import Generators


def test_add_products_in_cart(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.verify_all_products_heading_is_visible()

    all_products_count = ctx.all_products_page.get_products_count()
    count_of_products_to_be_added = Generators.generate_random_int(
        min_int=1,
        max_int=all_products_count)
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=count_of_products_to_be_added)

    ctx.view_cart_page.verify_products_in_cart(added_items)
