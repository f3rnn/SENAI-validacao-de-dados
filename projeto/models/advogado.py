from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,
                  sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str,
                    cpf: str, rg: str, matricula: str, setor: Setor, salario: float,
                    oab:str) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.oab = oab

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nOAB: {self.oab}"
                )