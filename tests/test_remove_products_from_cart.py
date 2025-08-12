from context_config import WebContext
from utilities.generators import Generators


def test_remove_products_from_cart(ctx: WebContext):
    all_products_count = ctx.all_products_page.get_products_count()
    product_number = Generators.generate_random_int(min_int=1,
                                                    max_int=all_products_count)
    added_items = ctx.all_products_page.add_products_in_cart(
        number_of_products=product_number)
    ctx.view_cart_page.delete_products_in_cart(added_items)
    ctx.view_cart_page.verify_cart_is_empty()
