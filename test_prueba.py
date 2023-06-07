import pytest
import prueba


def test_isisntance_error():
    assert "Error" == (prueba.calc("n", 7, "+"))
    assert "Error" == (prueba.calc((5, 5), 7, "+"))


def test_operand_error():
    assert "Error" == (prueba.calc(7, 7, "."))
    assert "Error" == (prueba.calc((5, 5), 7, "e"))


def test_sum():
    assert 12 == (prueba.calc(5, 7, "+"))
    assert 45 == (prueba.calc(40, 5, "+"))


def test_res():
    assert -2 == (prueba.calc(5, 7, "-"))
    assert 35 == (prueba.calc(40, 5, "-"))


def test_sum():
    assert 35 == (prueba.calc(5, 7, "*"))
    assert 200 == (prueba.calc(40, 5, "*"))


def test_sum():
    assert 2 == (prueba.calc(6, 3, "/"))
    assert 8 == (prueba.calc(40, 5, "/"))
