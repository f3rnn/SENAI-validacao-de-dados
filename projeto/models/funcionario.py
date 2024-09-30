from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.pessoafisica import Fisica

class RgError(Exception):
    pass

class CpfError(Exception):
    pass

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco,
                 sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str,
                 cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}"
            )
    
    def _verificar_salario(self, salario):
        if not isinstance (salario, float):
            raise TypeError("o salário precisa ser um número real")
        if salario < 0:
            raise ValueError("salário não pode ser negativo")
        return salario
    
    def _verificar_cpf(self, cpf):
        if len(cpf) > 14:
            raise CpfError("CPF inválido")
        return cpf
    
    def _verificar_rg(self, rg):
        if len(rg) > 12:
            raise RgError("RG inválido")
        return rg

    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)