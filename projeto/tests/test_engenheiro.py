import pytest

from projeto.models.endereco import CepError, Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.enum.uf import UnidadeFederativa
from projeto.models.funcionario import CpfError, RgError

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999","825.863.350-31","27.795.968-8","007",Setor.ENGENHARIA,7000.0,"1234567890")

#validando atributos

def test_id_valido(engenheiro_valido):
    assert engenheiro_valido.id == 18

def test_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "José Tigrão"

def test_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "9899-9999"

def test_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "bondedotigrão@gmail.com"

def test_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "alameda"

def test_numero_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "123"

def test_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "40.000-000"

def test_cidade_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "salvador"

def test_uf_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(engenheiro_valido):
    assert engenheiro_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(engenheiro_valido):
    assert engenheiro_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(engenheiro_valido):
    assert engenheiro_valido.dataNascimento == "24/09/1999"

def test_cpf_valido(engenheiro_valido):
    assert engenheiro_valido.cpf == "825.863.350-31"

def test_rg_valido(engenheiro_valido):
    assert engenheiro_valido.rg == "27.795.968-8"

def test_matricula_valido(engenheiro_valido):
    assert engenheiro_valido.matricula == "007"

def test_setor_valido(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA

def test_salario_valido(engenheiro_valido):
    assert engenheiro_valido.salario == 7000.0

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "1234567890"

#testando exceções
def test_id_tipo_errado(engenheiro_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Engenheiro("f", "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_id_valor_negativo(engenheiro_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Engenheiro(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_nome_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Engenheiro(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_salario_tipo_errado(engenheiro_valido):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, "7000.0","32575756")

def test_salario_negativo(engenheiro_valido):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, -7000.0,"32575756")

def test_cep_invalido(engenheiro_valido):
    with pytest.raises(CepError, match = "CEP inválido"):
        Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")
        
def test_rg_invalido(engenheiro_valido):
    with pytest.raises(RgError, match = "RG inválido"):
        Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-80", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_cpf_invalido(engenheiro_valido):
    with pytest.raises(CpfError, match = "CPF inválido"):
        Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-310", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")