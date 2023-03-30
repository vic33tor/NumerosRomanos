import pytest

from NumerosRomanos import NumerosRomanos


@pytest.fixture
def numeros():
    yield NumerosRomanos()


def test_I(numeros):
    assert numeros.numero("I") == 1


def test_V(numeros):
    assert numeros.numero("V") == 5


def test_X(numeros):
    assert numeros.numero("X") == 10


def test_L(numeros):
    assert numeros.numero("L") == 50


def test_C(numeros):
    assert numeros.numero("C") == 100


def test_IV(numeros):
    assert numeros.numero("IX") == 9


def test_num_dos_o_mas_nums(numeros):
    assert numeros.numero("XXXIV") == 34
