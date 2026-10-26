from playwright.sync_api import Page
import pytest

from Utils import jsonHandling
from pages.authorization import LoginPage

@pytest.mark.smoke
def test_login_rejects_unknown_email(page: Page, navigation) -> None:
    login_page = LoginPage(page)
    credentials = jsonHandling.json_credentials("testData//creds.json")
    login_page.submit_email(credentials["username"])
    login_page.submit_password(credentials["password"])
    login_page.expect_unknown_account_error()