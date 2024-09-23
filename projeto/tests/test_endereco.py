import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    return Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA)
     
def test_atributo_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "alameda"

def test_atributo_cep_valido(endereco_valido):
    assert endereco_valido.cep == "40.000-000"