from projeto.models.endereco import Endereco
from projeto.models.pessoajuridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,
                 cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nproduto: {self.produto}")
    
    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)
    
    def _verificar_cep(self, cep):
        return super()._verificar_cep(cep)