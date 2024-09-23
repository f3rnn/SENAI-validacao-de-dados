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

def test_atributo_id_valido(pessoa_valida):
    assert pessoa_valida.id == 18

def test_pessoa_id_negativo_retorna_mensagem(pessoa_valida):
    with pytest.raises(ValueError, match = "valor inválido"):
        Pessoa(-18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA))