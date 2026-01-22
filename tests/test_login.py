from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_login_sucesso(page):
    login = LoginPage(page)
    login.acessar("https://front.serverest.dev/login")
    login.realizar_login("testelucas@qa.com", "@LucasQA01")
    login.validar_login()

    
def test_login_email_invalido(page):
    login = LoginPage(page)
    login.acessar("https://front.serverest.dev/login")
    login.realizar_login("emailinvalido@qa.com", "@LucasQA01")
    login.validar_senha_errada()

def test_login_senha_invalida(page):
    login = LoginPage(page)
    login.acessar("https://front.serverest.dev/login")
    login.realizar_login("testelucas@qa.com", "senhaerrada")
    login.validar_senha_errada()

def test_login_email_senha_invalida(page):
    login = LoginPage(page)
    login.acessar("https://front.serverest.dev/login")
    login.realizar_login("emailinvalido@qa.com", "senhaerrada")
    login.validar_email_senha_invalida()