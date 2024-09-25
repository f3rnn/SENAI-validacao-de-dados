import pytest

from projeto.models.cliente import Cliente
from projeto.models.endereco import CepError, Endereco
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.uf import UnidadeFederativa


@pytest.fixture
def cliente_valido():
    return Cliente(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,"24/09/1999",1123)

#validando atributos
def test_atributo_nome_valido(cliente_valido):
    assert cliente_valido.nome == "José Tigrão"

def test_atributo_id_valido(cliente_valido):
    assert cliente_valido.id == 18

def test_atributo_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "9899-9999"

def test_atributo_email_valido(cliente_valido):
    assert cliente_valido.email == "bondedotigrão@gmail.com"

def test_logradouro_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "alameda"

def test_numero_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "123"

def test_complemento_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "40.000-000"

def test_cidade_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "salvador"

def test_uf_valido(cliente_valido):
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(cliente_valido):
    assert cliente_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(cliente_valido):
    assert cliente_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "24/09/1999"

def test_protocolo_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloAtendimento == 1123


#testando exceções
def test_id_tipo_errado(cliente_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Cliente("f", "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",1123)

def test_id_valor_negativo(cliente_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Cliente(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",1123)

def test_nome_vazio(cliente_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Cliente(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",1123)

def test_cep_invalido(cliente_valido):
    with pytest.raises(CepError, match = "CEP inválido"):
        Cliente(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", 1123)

