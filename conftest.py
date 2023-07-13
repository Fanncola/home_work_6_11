from selene import browser
import pytest
from utils import attach


@pytest.fixture(autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 776

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

