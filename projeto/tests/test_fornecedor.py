import pytest

from projeto.models.endereco import CepError, Endereco
from projeto.models.enum.uf import UnidadeFederativa
from projeto.models.fornecedores import Fornecedor


@pytest.fixture
def fornecedor_valido():
        return Fornecedor(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")

#validando atributos
def test_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 18

def test_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "José Tigrão"

def test_telefone_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "9899-9999"

def test_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "bondedotigrão@gmail.com"

def test_logradouro_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "alameda"

def test_numero_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.numero == "123"

def test_complemento_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "40.000-000"

def test_cidade_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "salvador"

def test_uf_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_cnpj_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "68.582.878/0001-16"

def test_inscricao_estadual_valida(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "5277216-46"

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Hardware"

#testando exceções
def test_id_tipo_errado(fornecedor_valido):
    with pytest.raises(TypeError, match = "o id deve ser um número inteiro"):
        Fornecedor("f", "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")

def test_id_valor_negativo(fornecedor_valido):
    with pytest.raises(ValueError, match = "o id não pode ser um número negativo"):
        Fornecedor(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")

def test_nome_vazio(fornecedor_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Fornecedor(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")

def test_cep_invalido(fornecedor_valido):
    with pytest.raises(CepError, match = "CEP inválido"):
        Fornecedor(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")
