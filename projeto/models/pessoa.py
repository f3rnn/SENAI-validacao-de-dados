from projeto.models.endereco import Endereco
from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
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
    
    def _verificar_id(self, id):
        if not isinstance(id, int):
            raise TypeError("o id deve ser um número inteiro")
        if id < 0:
            raise ValueError("o id não pode ser um número negativo")
        return id
    
    def _verificar_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("o nome não pode estar em branco")
        return nome

    def _verificar_cep(self, cep):
        return super._verificar_cep(cep)