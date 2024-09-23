import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA))
    return pessoa 

def test_atributo_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "José Tigrão"