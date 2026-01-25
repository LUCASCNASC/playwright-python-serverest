from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout_sucesso(page):
    login = LoginPage(page)
    login.acessar("https://front.serverest.dev/login")
    login.realizar_login("testelucas@qa.com", "@LucasQA01")
    login.validar_login()
    logout = LogoutPage(page)
    logout.realizar_logout()
    logout.validar_logout()

    
