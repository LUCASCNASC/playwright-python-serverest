import requests

BASE_URL = "https://serverest.dev"

def criar_usuario(payload):
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )
    response.raise_for_status()
    return response.json()
