import pytest

@pytest.fixture
def navigation(page):
    page.goto("https://www.amazon.com/ref=nav_logo")
