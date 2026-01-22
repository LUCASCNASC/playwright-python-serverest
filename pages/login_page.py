from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = '[data-testid="email"]'
        self.password_input = '[data-testid="senha"]'
        self.login_button = '[data-testid="entrar"]'

    def acessar(self, url):
        self.page.goto(url)

    def realizar_login(self, email, senha):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, senha)
        self.page.click(self.login_button)

    def validar_login(self):
        expect(
        self.page.get_by_text(
            "Este é seu sistema para administrar seu ecommerce.",
            exact=True
        )
        ).to_be_visible()

    def validar_senha_errada(self):
        expect(
        self.page.get_by_text(
            "Email e/ou senha inválidos",
            exact=True
        )
        ).to_be_visible()

    def validar_email_invalido(self):
        expect(
        self.page.get_by_text(
            "Email e/ou senha inválidos",
            exact=True
        )
        ).to_be_visible()

    def validar_email_senha_invalida(self):
        expect(
        self.page.get_by_text(
            "Email e/ou senha inválidos",
            exact=True
        )
        ).to_be_visible()
