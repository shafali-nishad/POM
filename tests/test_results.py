from playwright.sync_api import Page, expect
import pytest
from pages.home import HomePage
from  pages.results import ResultsScreenUI


@pytest.mark.smoke
def test_resultsScreenUI(page: Page, navigation) -> None:
    homePageObj= HomePage(page)
    homePageObj.ValidateTheVisibilityOfLogo()
    homePageObj.fill_searchbox()
    #page.get_by_role("searchbox", name="Search Amazon").fill("iphone")
    homePageObj.button_click()
    #page.get_by_role("button", name="Go", exact=True).click()
    resultPageObj = ResultsScreenUI(page)
    resultPageObj.ValidateTheVisibilityOfHeading()
    #expect(page.get_by_role("heading", name="More results", exact=True)).to_be_visible()




