from context_config import WebContext
from utilities.generators import Generators


def test_product_quantity_in_cart(ctx: WebContext):
    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    ctx.all_products_page.click_product_view_button(product_number)
    ctx.product_detail_page.verify_all_product_details_are_visible()
    product_name = ctx.product_detail_page.get_product_name()
    ctx.product_detail_page.adjust_product_quantity(quantity=str(product_number))
    ctx.product_detail_page.click_add_to_cart_button()
    ctx.all_products_page.click_view_cart_link()
    ctx.view_cart_page.verify_product_quantity_in_cart(product_name, str(product_number))
