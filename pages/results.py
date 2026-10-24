from playwright.sync_api import Page,expect
import pytest


class ResultsScreenUI(Page):
    def __init__(self, page):
        self.heading = page.get_by_role("heading", name="More results", exact=True)

    def ValidateTheVisibilityOfHeading(self):
        expect(self.heading).to_be_visible()