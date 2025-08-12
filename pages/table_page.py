import time

from playwright.sync_api import Page, Locator, expect

from pages.base_page import BasePage


class Table(BasePage):
    def __init__(self, page: Page, table_locator: str):
        self.page = page
        self.table_locator = page.locator(table_locator)
        self.table_head_locator = "thead"
        self.table_body_locator = "tbody"
        self.table_row_locator = "tr"
        self.table_cell_locator = "td"
        self.delete_button_locator = "tbody .cart_delete"
        self.empty_table_message_locator = "#empty_cart"
        # self.page = page
        # self.table_locator = table_locator
        # self.table = page.locator(table_locator)
        # self.table_head_locator = ".ant-table-thead"
        # self.table_row_locator = ".ant-table-row"
        # self.table_cell_locator = ".ant-table-cell"
        # self.expand_button_locator = ".ant-table-row-expand-icon"
        # self.empty_table_message_locator = ".ant-empty-description"
        # self.row_identifier_key = "data-row-key"
        # self.__nested_table_locator = "{} .ant-table-expanded-row div[id*='{}']"
        # self.loading_spinners = [".ant.spin", ".ant.spin-dot", ".ant-spin-spinning"]

    def get_headers(self) -> list[str]:
        try:
            headers = self.table_locator.locator(self.table_head_locator)
            header_text = headers.first.inner_text()
            return [h.strip() for h in header_text.split('\t')]
        except TimeoutError:
            raise ValueError("Unable to find table headers")

    def get_all_rows(self) -> Locator:
        return self.table_locator.locator(self.table_body_locator).locator(
            self.table_row_locator)

    def get_row_by_index(self, index: int) -> Locator:
        rows = self.get_all_rows()
        if not rows:
            raise ValueError("No rows found in the table")
        if index < 0 or index >= rows.count():
            raise ValueError(f"Index {index} is out of bounds for the table")
        return rows.nth(index)

    def get_row(self, row_value: str, timeout: int = 30, poll_interval: float = 0.1) -> Locator:
        rows = self.get_all_rows()
        if not rows:
            raise ValueError("No rows found in the table")
        rows.first.wait_for(state="visible")
        deadline = time.time() + timeout
        while time.time() < deadline:
            row = rows.filter(has_text=row_value, visible=True)
            if not row.count():
                self.scroll_table_down(rows.last, poll_interval)
                rows = self.get_all_rows()
                continue
            return row
        raise TimeoutError("Timeout: Table did not load rows in time.")

    def get_row_cells(self, row_value: str) -> Locator:
        return self.get_row(row_value).locator(self.table_cell_locator)

    def get_cell(self, row_value: str, column_name: str) -> Locator:
        headers = self.get_headers()
        try:
            column_index = headers.index(column_name)
        except ValueError:
            raise ValueError(f"Column '{column_name}' not found")

        cells = self.get_row_cells(row_value)
        return cells.nth(column_index)

    def get_column_cells(self, column_name: str) -> list[Locator]:
        headers = self.get_headers()
        try:
            column_index = headers.index(column_name)
        except ValueError:
            raise ValueError(f"Column '{column_name}' not found")

        rows = self.get_all_rows()
        if not rows:
            raise ValueError("No rows found in the table")

        return [row.locator(f"td:nth-child({column_index + 1})") for row in rows.all()]

    def scroll_table_down(self, scroll_target: Locator, poll_interval: float = 0.1):
        scroll_target.hover(force=True)
        self.page.mouse.wheel(0, 60)
        self.page.wait_for_timeout(poll_interval)

    def verify_table_empty(self, timeout=5000):
        self.verify_element_is_visible(
            self.page.locator(self.empty_table_message_locator),
            timeout=timeout)
