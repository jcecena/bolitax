import pytest
from main import calcular_area_triangulo

def test_area_triangulo():
    resultado = calcular_area_triangulo(13, 3)
    assert resultado == pytest.approx(19.5, abs=0.01)