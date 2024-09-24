import pytest

from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.uf import UnidadeFederativa


@pytest.fixture
def cliente_valido():
    return Cliente(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,"24/09/1999",1123)

def test_atributo_nome_valido(cliente_valido):
    assert cliente_valido.nome == "José Tigrão"

def test_atributo_id_valido(cliente_valido):
    assert cliente_valido.id == 18

def test_atributo_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "9899-9999"

def test_atributo_email_valido(cliente_valido):
    assert cliente_valido.email == "bondedotigrão@gmail.com"