import pytest
from projeto.models.endereco import Endereco
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    return Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA)
     
def test_atributo_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "alameda"

def test_atributo_numero_valido(endereco_valido):
    assert endereco_valido.numero == "123"

def test_atributo_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "ali na esquina"

def test_atributo_cep_valido(endereco_valido):
    assert endereco_valido.cep == "40.000-000"

def test_atributo_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "salvador"
