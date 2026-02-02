def test_login_sucesso(browser, usuario):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://front.serverest.dev/login")

    page.fill('[data-testid="email"]', usuario["email"])
    page.fill('[data-testid="senha"]', usuario["password"])
    page.click('[data-testid="entrar"]')

    page.wait_for_url("**/home")

    assert page.locator("text=Bem Vindo").is_visible()
