import pytest

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enum.estadocivil import EstadoCivil
from projeto.models.enum.genero import Genero
from projeto.models.enum.setores import Setor
from projeto.models.enum.uf import UnidadeFederativa

@pytest.fixture

def engenheiro_valido():
    return Engenheiro(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999","825.863.350-31","27.795.968-8","007",Setor.ENGENHARIA,7000,"1234567890")
