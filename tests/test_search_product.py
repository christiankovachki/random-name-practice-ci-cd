from context_config import WebContext
from utilities.generators import Generators


def test_search_for_product_single_result(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.verify_all_products_heading_is_visible()

    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    ctx.all_products_page.click_product_view_button(product_number)
    product_name = ctx.product_detail_page.get_product_name()
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.populate_search_input(product_name)
    ctx.all_products_page.click_search_button()

    ctx.searched_products_page.verify_searched_products_heading_is_visible()
    ctx.searched_products_page.verify_search_results(product_name)


def test_search_for_product_multiple_results(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Products")
    ctx.all_products_page.verify_all_products_heading_is_visible()

    product = "Jeans"
    ctx.all_products_page.populate_search_input(product)
    ctx.all_products_page.click_search_button()

    ctx.searched_products_page.verify_searched_products_heading_is_visible()
    ctx.searched_products_page.verify_search_results(product, exact_match=False)
