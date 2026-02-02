import pytest
from playwright.sync_api import sync_playwright
from utils.data_factory import gerar_usuario
from services.usuarios_service import criar_usuario


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def usuario():
    payload = gerar_usuario()
    response = criar_usuario(payload)

    return {
        "email": payload["email"],
        "password": payload["password"],
        "_id": response["_id"]
    }
