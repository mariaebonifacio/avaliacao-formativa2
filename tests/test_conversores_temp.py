import pytest
from conversao.conversores_temp import converter_temperatura

# Caminho feliz = retorna um valor
#   TESTE COM PARAMETRIZE
@pytest.mark.parametrize(
    "valor, de_escala, para_escala, espero",
    [
        (32, "KELVIN", "CELSIUS", -241.15),
        (32, "KELVIN", "FAHRENHEIT", -402.07),
        (32, "CELSIUS", "KELVIN", 305.15),
        (32, "CELSIUS", "FAHRENHEIT", 89.60),
        (32, "FAHRENHEIT", "CELSIUS", 0),
        (32, "FAHRENHEIT", "KELVIN", 273.15),
        (32, "KELVIN", "KELVIN", 32),
        (32, "CELSIUS", "CELSIUS", 32),
        (32, "FAHRENHEIT", "FAHRENHEIT", 32)

    ],
    ids=["Kelvin para Celsius",
         "Kelvin para Fahrenheit",
         "Celsius para Kelvin",
         "Celsius para Fahrenheit",
         "Fahrenheit para Celsius",
         "Fahrenheit para Kelvin",
         "Kelvin para Kelvin",
         "Celsius para Celsius",
         "Fahrenheit para Fahrenheit"]
)
# função para converter temperatura pelo caminho feliz (retorna um valor)
def test_converter_temperatura_caminho_feliz(valor, de_escala, para_escala, espero):
    resultado = converter_temperatura(valor, de_escala, para_escala)
    assert resultado == pytest.approx(espero, 0.01)

# função para teste de valor errado na converção da temperatura 
def test_converter_temperatura_valor_errado_de_escala():
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(32, "ABOBRINHA", "KELVIN")

# TESTE DE ValueError COM PARAMETRIZE
@pytest.mark.parametrize(
    "valor, de_escala, para_escala, tipo_erro, texto_erro",
    [
        # Testando valores incorretos
        (100, "abobrinha", "CELSIUS", ValueError, "Escala de temperatura inválida"),
        (100, "KELVIN", "", ValueError, "Escala de temperatura inválida"),
        (100, "", "", ValueError, "Escala de temperatura inválida"),
        # Testando valores negativos para kelvin
        (-10, "KELVIN", "CELSIUS", ValueError, "Temperatura em KELVIN não pode ser negativa.")
    ],
    ids=[
        # Testando valores incorretos
        "Valor incorreto em de_escala",
        "Valor incorreto em para_escala",
        "Valor incorreto em ambas as escalas",
        "Valor incorreto para Kelvin"
    ]
)
def test_temperatura_caminho_errado(valor, de_escala, para_escala, tipo_erro, texto_erro):
    with pytest.raises(tipo_erro, match=texto_erro):
        converter_temperatura(valor, de_escala, para_escala)


