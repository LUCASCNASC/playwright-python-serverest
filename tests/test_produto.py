import uuid

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

    nome_produto = f"Produto QA {uuid.uuid4().hex[:6]}"

    page.fill('[data-testid="nome"]', nome_produto)
    page.fill('[data-testid="preco"]', "100")
    page.fill('[data-testid="descricao"]', "Produto criado via teste")
    page.get_by_label("Quantidade").fill("10")

    with page.expect_response("**/produtos") as response_info:
        page.get_by_role("button", name="Cadastrar").click()

    response = response_info.value
    assert response.status == 201
