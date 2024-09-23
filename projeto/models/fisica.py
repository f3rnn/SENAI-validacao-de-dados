from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.pessoa import Pessoa
from projeto.models.enum.genero import Genero


class Fisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,
                 sexo:Genero,estadoCivil:EstadoCivil,dataNascimento:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nSexo: {self.sexo}"
            f"\nEstado civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.dataNascimento}"
            )
