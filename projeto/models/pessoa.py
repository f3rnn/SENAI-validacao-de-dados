from projeto.models.endereco import Endereco

class Pessoa:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self.__verificar_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    def __str__(self) -> str:
        return (
            f"\nid: {self.id}"
            f"\nnome: {self.nome}"
            f"\ntelefone: {self.telefone}"
            f"\nemail: {self.email}"
            f"\nendereço: {self.endereco}"
        )
    
    def __verificar_id(self, id):
        if id < 0:
            raise ValueError("valor inválido")
        if not isinstance(id, int):
            raise TypeError("valor inválido")
        return id