import random
import string

def gerar_usuario():
    sufixo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    return {
        "nome": f"User {sufixo}",
        "email": f"user_{sufixo}@mail.com",
        "password": "123456",
        "administrador": "true"
    }
