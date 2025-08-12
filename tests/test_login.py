from context_config import WebContext
from factories.user_factory import UserFactory


def test_login_with_valid_credentials(ctx: WebContext):
    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.login_existing_user()

    ctx.navigation_bar.verify_nav_bar_link_is_visible("Logout")
    username = UserFactory.get_existing_user_username()
    ctx.navigation_bar.verify_logged_in_as_user(username)

def test_login_with_incorrect_credentials(ctx: WebContext):
    user = UserFactory().create_user()

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.populate_login_form(user.email, user.password)
    ctx.signup_login_page.click_login_button()

    ctx.signup_login_page.verify_incorrect_credentials_error_message_is_visible()
