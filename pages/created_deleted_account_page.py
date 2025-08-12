from playwright.sync_api import Page

from pages.base_page import BasePage


class CreatedDeletedAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.ACCOUNT_CREATED_HEADING = page.get_by_test_id("account-created")
        self.ACCOUNT_DELETED_HEADING = page.get_by_test_id("account-deleted")
        self.CONTINUE_BUTTON = page.get_by_test_id("continue-button")

    def click_continue_button(self):
        self.click_on_element(self.CONTINUE_BUTTON)

    def verify_account_created_heading_is_visible(self):
        self.verify_element_is_visible(self.ACCOUNT_CREATED_HEADING)

    def verify_account_deleted_heading_is_visible(self):
        self.verify_element_is_visible(self.ACCOUNT_DELETED_HEADING)
