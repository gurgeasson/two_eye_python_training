import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def stealth_context():
    """Create a stealth-enabled browser context."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-infobars",
                "--disable-dev-shm-usage",
            ],
        )

        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            timezone_id="Europe/London",
            locale="en-GB",
            color_scheme="light",
            viewport={"width": 1366, "height": 768},
        )

        # Hide Playwright automation fingerprints
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """)

        yield context

        context.close()
        browser.close()

@pytest.fixture
def page(stealth_context):
    """Provides a new page for each test."""
    page = stealth_context.new_page()
    yield page
    page.close()
