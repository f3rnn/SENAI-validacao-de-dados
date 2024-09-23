from projeto.models.endereco import Endereco

class Pessoa:
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    def __str__(self) -> str:
        return (
            f"\nnome: {self.nome}"
            f"\ntelefone: {self.telefone}"
            f"\nemail: {self.email}"
            f"\nendereço: {self.endereco}"
        )