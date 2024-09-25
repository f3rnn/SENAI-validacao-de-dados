from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,
                 sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str,
                 cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crea = crea

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
                )
    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)
    
    def _verificar_cep(self, cep):
        return super()._verificar_cep(cep)
    
    def _verificar_rg(self, rg):
        return super()._verificar_rg(rg)
    
    def _verificar_cpf(self, cpf):
        return super()._verificar_cpf(cpf)
    
    def _verificar_salario(self, salario):
        return super()._verificar_salario(salario)