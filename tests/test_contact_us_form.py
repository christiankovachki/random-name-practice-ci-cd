from context_config import WebContext
from factories.user_factory import UserFactory
from utilities.generators import Generators
from utilities.file_helper import FileHelper


def test_submit_contact_us_form(ctx: WebContext):
    #raise NotImplementedError("Need adjustments after line 27")
    user = UserFactory().create_user()

    ctx.navigation_bar.click_nav_bar_link_by_name("Contact us")
    ctx.contact_us_page.verify_get_in_touch_heading_is_visible()

    subject = Generators.generate_random_subject()
    message = Generators.generate_random_text()
    ctx.contact_us_page.populate_contact_us_form_details(user.first_name,
                                                         user.email,
                                                         subject,
                                                         message)

    file_to_upload_path = FileHelper.get_upload_path("logo.png", "images")
    ctx.contact_us_page.upload_contact_us_form_file(file_to_upload_path)
    ctx.base_page.accept_dialog()
    ctx.contact_us_page.click_submit_button()

    ctx.contact_us_page.verify_success_alert_is_visible()
    ctx.contact_us_page.click_home_button()

    # expected_url = os.getenv("BASE_URL")
    # Move assertion to POM
    # expect(ctx.page).to_have_url(expected_url)
