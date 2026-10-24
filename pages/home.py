from playwright.sync_api import Page,expect

class HomePage():
    def __init__(self, page):
        self.logo = page.get_by_role("link", name="Amazon", exact=True)
        self.searchbox = page.get_by_role("searchbox", name="Search Amazon")
        self.cart = page.get_by_role("link", name="items in cart")
        self.button = page.get_by_role("button", name="Go", exact=True)

    def ValidateTheVisibilityOfLogo(self):
        expect(self.logo).to_be_visible()

    def ValidateTheVisibilityOfSeachBox(self):
        expect(self.searchbox).to_be_visible()

    def fill_searchbox(self):
        self.searchbox.fill("iphone")

    def ValidateTheVisibilityOfCart(self):
        expect(self.cart).to_be_visible()

    def button_click(self):
        self.button.click()