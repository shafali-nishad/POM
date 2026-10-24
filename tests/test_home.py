from playwright.sync_api import Page, expect
import pytest

from pages.home import HomePage



@pytest.mark.smoke
def test_HomeScreenUI(page: Page,navigation) -> None:
    homePageObj= HomePage(page)
    #expect(page.get_by_role("link", name="Amazon", exact=True)).to_be_visible()
    homePageObj.ValidateTheVisibilityOfLogo()
    # expect(page.get_by_role("searchbox", name="Search Amazon")).to_be_visible()
    homePageObj.ValidateTheVisibilityOfSeachBox()
    homePageObj.ValidateTheVisibilityOfCart()
    # expect(page.get_by_role("link", name="items in cart")).to_be_visible()