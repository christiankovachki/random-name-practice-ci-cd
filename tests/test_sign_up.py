from context_config import WebContext
from factories.user_factory import UserFactory


def test_sign_up_with_valid_credentials(ctx: WebContext):
    user = UserFactory().create_user()

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_page.signup_new_user(user)

    ctx.created_deleted_account_page.verify_account_created_heading_is_visible()
    ctx.created_deleted_account_page.click_continue_button()

    ctx.navigation_bar.verify_nav_bar_link_is_visible("Logout")
    ctx.navigation_bar.verify_logged_in_as_user(user.username)

    ctx.navigation_bar.click_nav_bar_link_by_name("Delete Account")
    ctx.created_deleted_account_page.verify_account_deleted_heading_is_visible()
    ctx.created_deleted_account_page.click_continue_button()

def test_sign_up_with_existing_email(ctx: WebContext):
    user = UserFactory().create_user()
    existing_email = UserFactory.get_existing_user_email()

    ctx.navigation_bar.click_nav_bar_link_by_name("Signup / Login")
    ctx.signup_login_page.populate_signup_form(user.username, existing_email)
    ctx.signup_login_page.click_signup_button()

    ctx.signup_login_page.verify_existing_email_error_message_is_visible()
