from pathlib import Path
from typing import Union

from playwright.sync_api import Page, Locator, expect, Dialog


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_on_element(self, element: Union[str, Locator], timeout: float = 10000, force: bool = False) -> None:
        locator = self._get_locator(element)
        locator.click(timeout=timeout, force=force)

    def hover_over_element(self, element: Union[str, Locator], timeout: int = 10000, force: bool = False) -> None:
        locator = self._get_locator(element)
        locator.hover(timeout=timeout, force=force)

    def type_text_in_input_field(self, element: Union[str, Locator], value: str, timeout: float = 10000) -> None:
        locator = self._get_locator(element)
        locator.fill(value, timeout=timeout)

    def check_checkbox(self, element: Union[str, Locator], timeout: float = 10000, force: bool = False) -> None:
        locator = self._get_locator(element)
        locator.check(timeout=timeout, force=force)

    def uncheck_checkbox(self, element: Union[str, Locator], timeout: float = 10000, force: bool = False) -> None:
        locator = self._get_locator(element)
        locator.uncheck(timeout=timeout, force=force)

    def is_checkbox_checked(self, element: Union[str, Locator], timeout: float = 10000) -> bool:
        locator = self._get_locator(element)
        return locator.is_checked(timeout=timeout)

    def select_dropdown_option(self, element: Union[str, Locator], value: str, timeout: float = 10000) -> None:
        locator = self._get_locator(element)
        locator.select_option(value, timeout=timeout)

    def upload_file(self, element: Union[str, Locator], file_path: str, timeout: int = 10000) -> None:
        locator = self._get_locator(element)

        with self.page.expect_file_chooser() as fc_info:
            self.click_on_element(locator)

        file_input = fc_info.value
        file_input.set_files(file_path, timeout=timeout)

    def accept_dialog(self, expected_text: str = None):
        def handle_dialog(dialog: Dialog):
            if expected_text and expected_text not in dialog.message:
                raise ValueError(
                    f"Dialog text mismatch. Expected: '{expected_text}', Got: '{dialog.message}'")
            dialog.accept()
        self.page.once("dialog", handle_dialog)

    def dismiss_dialog(self, expected_text: str = None):
        def handle_dialog(dialog: Dialog):
            if expected_text and expected_text not in dialog.message:
                raise ValueError(
                    f"Dialog text mismatch. Expected: '{expected_text}', Got: '{dialog.message}'")
            dialog.dismiss()
        self.page.once("dialog", handle_dialog)

    def get_current_url(self) -> str:
        return self.page.url

    def get_element_text_content(self, element: Union[str, Locator], timeout: int = 10000) -> str:
        locator = self._get_locator(element)
        return locator.text_content(timeout=timeout).strip()

    def verify_element_is_visible(self, element: Union[str, Locator], timeout: float = 10000) -> None:
        locator = self._get_locator(element)
        expect(locator).to_be_visible(timeout=timeout)

    def verify_element_is_not_visible(self, element: Union[str, Locator], timeout: float = 10000) -> None:
        locator = self._get_locator(element)
        expect(locator).not_to_be_visible(timeout=timeout)

    def verify_element_text(self, element: Union[str, Locator], expected_text: str, timeout: float = 5000) -> None:
        locator = self._get_locator(element)
        expect(locator).to_have_text(expected_text, timeout=timeout)

    def verify_element_contains_text(self, element: Union[str, Locator], expected_text: str, timeout: float = 5000) -> None:
        locator = self._get_locator(element)
        expect(locator).to_contain_text(expected_text, timeout=timeout)

    def _get_locator(self, element: Union[str, Locator]) -> Locator:
        return self.page.locator(element) if isinstance(element, str) else element
