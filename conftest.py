import os
from typing import Dict, Any

import allure
import pytest
import logging
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, sync_playwright, Page
from context_config import WebContext

logger = logging.getLogger("playwright_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chromium",
        choices=["chromium", "firefox", "webkit"]
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False
    )
    parser.addoption(
        "--slowmo",
        type=int,
        default=0
    )
    parser.addoption(
        "--url",
        default=os.getenv("BASE_URL")
    )

@pytest.fixture(scope="session")
def browser(request: FixtureRequest):
    print()
    browser_name = request.config.getoption("--browser")

    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-qa")
        browser_types = {
            "firefox": p.firefox,
            "webkit": p.webkit,
            "chromium": p.chromium
        }
        browser_type = browser_types.get(browser_name.lower(), p.chromium)
        try:
            logger.info(f"Launching {browser_name.title()} browser...")
            browser = browser_type.launch(
                headless=request.config.getoption("--headless"),
                slow_mo=request.config.getoption("--slowmo"),
            )
            yield browser
        finally:
            browser.close()
            logger.info(f"Closed {browser_name.title()} browser...")

@pytest.fixture
def browser_context(browser: Browser, request: FixtureRequest):
    logger.info("Creating browser context...")

    context_options: Dict[str, Any] = {
        "ignore_https_errors": True,
        "viewport": {"width": 1920, "height": 1080},
    }

    browser_context = browser.new_context(**context_options)
    browser_context.set_default_navigation_timeout(timeout=30000)

    try:
        yield browser_context
    finally:
        browser_context.clear_cookies()
        browser_context.clear_permissions()
        browser_context.close()
        logger.info("Closed browser context...")

@pytest.fixture
def page(browser_context: BrowserContext, request: FixtureRequest):
    test_name = request.node.nodeid.split('::')[-1]
    logger.info(f"Starting test: {test_name}")

    page = browser_context.new_page()
    logger.info("Creating a new page...")
    page.goto(request.config.getoption("--url"))
    page.wait_for_selector(selector=".nav.navbar-nav", state="visible")
    consent_button = page.get_by_label(text="Consent", exact=True)
    if consent_button.is_visible():
        consent_button.click()
    try:
        yield page
    finally:
        if page and not page.is_closed():
            page.close()
            print()
            logger.info("Closed page...")

@pytest.fixture
def ctx(page: Page):
    context = WebContext(page)
    yield context

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        logger.info("Test completed with status: ")

        if report.longrepr:
            logger.error(f"Test failure details: {report.longrepr}")

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )
