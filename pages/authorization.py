from playwright.sync_api import Page, expect
import pytest

class LoginPage:
    def __init__(self, page: Page) -> None:
        self.sign_in_link = page.get_by_role(
            "link", name="Hello, sign in Account & Lists"
        )
        self.email_input = page.get_by_role(
            "textbox", name="Enter mobile number or email"
        )
        self.continue_button = page.get_by_role("button", name="Continue")
        self.password_tab =page.get_by_role("textbox", name="Password")
        self.button = page.get_by_role("button", name="Sign in", exact=True)
        # self.error_message = page.get_by_text("Your email or password was incorrect. Please try again.",exact=True)
        self.error_message = page.get_by_role("alert")

    def submit_email(self, email: str) -> None:
        self.sign_in_link.click()
        self.email_input.fill(email)
        self.continue_button.click()

    # def submit_password(self, password: str) -> None:
    #     self.password_tab.click()
    #     self.password_tab.fill("Welcome@02")
    #     # self.page.pause()
    #     print("Before Sign in click", flush=True)
    #     self.button.click()
    #     print("After Sign in click", flush=True)
    #     self.page.pause()

    def submit_password(self, password: str) -> None:
        self.password_tab.fill("")  # Clear the field first.
        self.password_tab.press_sequentially(password, delay=100)
        expect(self.password_tab).to_have_value(password)
        self.button.click()

    def expect_unknown_account_error(self) -> None:
        expect(self.error_message).to_contain_text(
            "Your password is incorrect. Try again."
        )