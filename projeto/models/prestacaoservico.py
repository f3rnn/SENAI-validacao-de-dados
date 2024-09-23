from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,
                 cnpj: str, inscricaoEstadual: str, contratoInicio: str, contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\ninicio do contrato: {self.contratoInicio}"
                f"\nfim do contraro: {self.contratoFim}")