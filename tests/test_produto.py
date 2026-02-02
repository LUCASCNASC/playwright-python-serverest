def test_cadastro_produto(browser, usuario):
    context = browser.new_context()
    page = context.new_page()

    # LOGIN
    page.goto("https://front.serverest.dev/login")
    page.fill('[data-testid="email"]', usuario["email"])
    page.fill('[data-testid="senha"]', usuario["password"])
    page.click('[data-testid="entrar"]')
    page.wait_for_url("**/home")

    # CADASTRO PRODUTO
    page.goto("https://front.serverest.dev/admin/cadastrarprodutos")
    page.wait_for_selector('[data-testid="nome"]')

    page.fill('[data-testid="nome"]', "Produto Teste")
    page.fill('[data-testid="preco"]', "100")
    page.fill('[data-testid="descricao"]', "Produto criado via teste")
    page.get_by_label("Quantidade").fill("10")

    page.get_by_role("button", name="Cadastrar").click()

    # ✅ valida sucesso de forma confiável
    assert page.locator("text=sucesso").is_visible()

    # ✅ valida que produto realmente existe na lista
    page.goto("https://front.serverest.dev/admin/listarprodutos")
    assert page.locator("text=Produto Teste").is_visible()
