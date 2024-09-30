import pytest

from projeto.models.funcionario import RgError, CpfError
from projeto.models.endereco import Endereco, CepError
from projeto.models.advogado import Advogado
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture

def advogado_valido():
    return Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")

#validando atributos

def test_id_valido(advogado_valido):
    assert advogado_valido.id == 18

def test_nome_valido(advogado_valido):
    assert advogado_valido.nome == "José Tigrão"

def test_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "9899-9999"

def test_email_valido(advogado_valido):
    assert advogado_valido.email == "bondedotigrao@gmail.com"

def test_logradouro_valido(advogado_valido):
    assert advogado_valido.endereco.logradouro == "alameda"

def test_numero_valido(advogado_valido):
    assert advogado_valido.endereco.numero == "123"

def test_complemento_valido(advogado_valido):
    assert advogado_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(advogado_valido):
    assert advogado_valido.endereco.cep == "40.000-000"

def test_cidade_valido(advogado_valido):
    assert advogado_valido.endereco.cidade == "salvador"

def test_uf_valido(advogado_valido):
    assert advogado_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(advogado_valido):
    assert advogado_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(advogado_valido):
    assert advogado_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(advogado_valido):
    assert advogado_valido.dataNascimento == "24/09/1999"

def test_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "825.863.350-31"

def test_rg_valido(advogado_valido):
    assert advogado_valido.rg == "27.795.968-8"

def test_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "007"

def test_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO

def test_salario_valido(advogado_valido):
    assert advogado_valido.salario == 7000.0

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "32575756"

#testando exceções
def test_id_tipo_errado(advogado_valido):
    with pytest.raises(TypeError, match = "o id deve ser um número inteiro"):
        Advogado(18.3, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")

def test_id_valor_negativo(advogado_valido):
    with pytest.raises(ValueError, match = "o id não pode ser um número negativo"):
        Advogado(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")

def test_nome_vazio(advogado_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Advogado(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")

def test_salario_tipo_errado(advogado_valido):
    with pytest.raises(TypeError, match = "o salário precisa ser um número real"):
        Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, "7000.0","32575756")

def test_salario_negativo(advogado_valido):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, -7000.0,"32575756")

def test_cep_invalido(advogado_valido):
    with pytest.raises(CepError, match = "CEP inválido"):
        Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")
        
def test_rg_invalido(advogado_valido):
    with pytest.raises(RgError, match = "RG inválido"):
        Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-80", "007", Setor.JURIDICO, 7000.0,"32575756")

def test_cpf_invalido(advogado_valido):
    with pytest.raises(CpfError, match = "CPF inválido"):
        Advogado(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-310", "27.795.968-8", "007", Setor.JURIDICO, 7000.0,"32575756")