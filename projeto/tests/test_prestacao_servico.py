import pytest

from projeto.models.endereco import CepError, Endereco
from projeto.models.enum.uf import UnidadeFederativa
from projeto.models.prestacaoservico import PrestacaoServico


@pytest.fixture
def prestacao_servico_valida():
        return PrestacaoServico(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","01/09/23","01/09/24")

#validando atributos
def test_id_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.id == 18

def test_nome_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.nome == "José Tigrão"

def test_telefone_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.telefone == "9899-9999"

def test_email_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.email == "bondedotigrão@gmail.com"

def test_logradouro_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.logradouro == "alameda"

def test_numero_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.numero == "123"

def test_complemento_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.complemento == "ali na esquina"

def test_cep_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.cep == "40.000-000"

def test_cidade_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.cidade == "salvador"

def test_uf_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.endereco.uf == UnidadeFederativa.BAHIA

def test_cnpj_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.cnpj == "68.582.878/0001-16"

def test_inscricao_estadual_valida(prestacao_servico_valida):
    assert prestacao_servico_valida.inscricaoEstadual == "5277216-46"

def test_inicio_contrato_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.contratoInicio == "01/09/23"

def test_fim_contrato_valido(prestacao_servico_valida):
    assert prestacao_servico_valida.contratoFim == "01/09/24"

#testando exceções
def test_id_tipo_errado(prestacao_servico_valida):
    with pytest.raises(TypeError, match = "o id deve ser um número inteiro"):
        PrestacaoServico("f", "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","01/09/23","01/09/24")

def test_id_valor_negativo(prestacao_servico_valida):
    with pytest.raises(ValueError, match = "o id não pode ser um número negativo"):
        PrestacaoServico(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","01/09/23","01/09/24")

def test_nome_vazio(prestacao_servico_valida):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        PrestacaoServico(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","01/09/23","01/09/24")

def test_cep_invalido(prestacao_servico_valida):
    with pytest.raises(CepError, match = "CEP inválido"):
        PrestacaoServico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","01/09/23","01/09/24")