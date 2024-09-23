from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,
                 sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nprotocolo de atendimento: {self.protocoloAtendimento}")