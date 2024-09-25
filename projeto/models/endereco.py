from projeto.models.enum.uf import UnidadeFederativa

class CepError(Exception):
    pass

class Endereco:
    def __init__(self,logradouro:str,numero:str,complemento:str,cep:str,cidade:str,uf:UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = self._verificar_cep(cep)
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUF: {self.uf.nome}"
        )
    
    def _verificar_cep(self, cep):
        if len(cep) > 10:
            raise CepError("CEP inválido")
        return cep