
from backend.main import calcular_quebra_tecnica


def test_calculo_quebra_tecnica_10_porcento():
    # Sala de 4m x 5m = 20m²
    # Com 10% de perda técnica deve dar 22.0m²

    resultado = calcular_quebra_tecnica(4.0, 5.0)

    assert resultado == 22.0


def test_calculo_valores_decimais():
    # Quarto de 3.5m x 4.2m = 14.7m²
    # Com 10% = 16.17m²

    resultado = calcular_quebra_tecnica(3.5, 4.2)

    assert resultado == 16.17
