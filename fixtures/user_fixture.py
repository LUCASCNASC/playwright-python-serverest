import pytest
from utils.data_factory import gerar_usuario
from services.usuarios_service import criar_usuario

@pytest.fixture(scope="session")
def usuario():
    payload = gerar_usuario()
    response = criar_usuario(payload)

    return {
        "email": payload["email"],
        "password": payload["password"],
        "_id": response["_id"]
    }
