from context_config import WebContext
from factories.user_factory import UserFactory


def test_logout(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.login_existing_user()

    username = UserFactory.get_existing_user_username()
    ctx.navigation_bar.verify_logged_in_as_user(username)

    ctx.navigation_bar.click_nav_bar_link_by_name("Logout")

    ctx.navigation_bar.verify_nav_bar_link_is_not_visible("Logout")
    ctx.navigation_bar.verify_nav_bar_link_is_not_visible("Delete Account")
    ctx.navigation_bar.verify_nav_bar_link_is_visible("Signup / Login")
    ctx.signup_login_page.verify_login_form_content_is_visible()
