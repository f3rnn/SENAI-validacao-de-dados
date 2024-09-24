import pytest

from projeto.models.endereco import Endereco
from projeto.models.enum.uf import UnidadeFederativa
from projeto.models.fornecedores import Fornecedor


@pytest.fixture
def fornecedor_valido():
        return Fornecedor(18, "José Tigrão", "9899-9999", "bondedotigrão@gmail.com",
                    Endereco("alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA),
                    "68.582.878/0001-16","5277216-46","Hardware")