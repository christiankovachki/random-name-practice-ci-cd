from context_config import WebContext
from utilities.generators import Generators


def test_product_detail_content(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.verify_all_products_heading_is_visible()

    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1, max_int=all_products_count)
    ctx.all_products_page.click_product_view_button(product_number)

    ctx.product_detail_page.verify_all_product_details_are_visible()
