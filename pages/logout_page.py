from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = '[data-testid="logout"]'


    def realizar_logout(self):
        self.page.click(self.logout_button)

    def validar_logout(self):
        expect(
        self.page.get_by_text(
            "Login",
            exact=True
        )
        ).to_be_visible()
