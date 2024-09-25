import pytest

from projeto.models.endereco import CepError, Endereco
from projeto.models.funcionario import CpfError, RgError
from projeto.models.medico import Medico
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture

def medico_valido():
    return Medico(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999","825.863.350-31","27.795.968-8","007",Setor.SAUDE,7000.0,"BA2135712357")

#validando atributos

def test_id_valido(medico_valido):
    assert medico_valido.id == 18

def test_nome_valido(medico_valido):
    assert medico_valido.nome == "José Tigrão"

def test_telefone_valido(medico_valido):
    assert medico_valido.telefone == "9899-9999"

def test_email_valido(medico_valido):
    assert medico_valido.email == "bondedotigrão@gmail.com"

def test_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "alameda"

def test_numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "123"

def test_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "ali na esquina"

def test_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "40.000-000"

def test_cidade_valido(medico_valido):
    assert medico_valido.endereco.cidade == "salvador"

def test_uf_valido(medico_valido):
    assert medico_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(medico_valido):
    assert medico_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(medico_valido):
    assert medico_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(medico_valido):
    assert medico_valido.dataNascimento == "24/09/1999"

def test_cpf_valido(medico_valido):
    assert medico_valido.cpf == "825.863.350-31"

def test_rg_valido(medico_valido):
    assert medico_valido.rg == "27.795.968-8"

def test_matricula_valido(medico_valido):
    assert medico_valido.matricula == "007"

def test_setor_valido(medico_valido):
    assert medico_valido.setor == Setor.SAUDE

def test_salario_valido(medico_valido):
    assert medico_valido.salario == 7000.0

def test_crea_valido(medico_valido):
    assert medico_valido.crm == "BA2135712357"

#testando exceções
def test_id_tipo_errado(medico_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Medico("f", "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_id_valor_negativo(medico_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Medico(-18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_nome_vazio(medico_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Medico(18, "", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_salario_tipo_errado(medico_valido):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Medico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, "7000.0","32575756")

def test_salario_negativo(medico_valido):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Medico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, -7000.0,"32575756")

def test_cep_invalido(medico_valido):
    with pytest.raises(CepError, match = "CEP inválido"):
        Medico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-0000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")
        
def test_rg_invalido(medico_valido):
    with pytest.raises(RgError, match = "RG inválido"):
        Medico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-31", "27.795.968-80", "007", Setor.ENGENHARIA, 7000.0,"32575756")

def test_cpf_invalido(medico_valido):
    with pytest.raises(CpfError, match = "CPF inválido"):
        Medico(18, "José Tigrão", "9899-9999", "bondedotigrao@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", "825.863.350-310", "27.795.968-8", "007", Setor.ENGENHARIA, 7000.0,"32575756")