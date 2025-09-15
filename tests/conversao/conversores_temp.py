
def converter_temperatura (valor: float, de_escala: str, para_escala: str):
    
    # Validação para letra maiúscula -- DE-ESCALA
    # CELSIUS
    if de_escala.upper != "CELSIUS":
        raise ValueError("Escala de temperatura inválida.")
    # FAHRENHEIT
    if de_escala.upper != "FAHRENHEIT":
        raise ValueError("Escala de temperatura inválida.")
    # KELVIN
    if de_escala.upper != "KELVIN":
        raise ValueError("Escala de temperatura inválida.")

    # Validação para letra maiúscula -- PARA-ESCALA
    # CELSIUS
    if para_escala.upper != "CELSIUS":
        raise ValueError("Escala de temperatura inválida.")
    # FAHRENHEIT
    if para_escala.upper != "FAHRENHEIT":
        raise ValueError("Escala de temperatura inválida.")
    # KELVIN
    if para_escala.upper != "KELVIN":
        raise ValueError("Escala de temperatura inválida.")
    

    # O valor para a escala KELVIN não pode ser abaixo do zero absoluto
    if de_escala == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa.")
    

    # CONVERSÃO
    # kelvin para celsius
    if de_escala == "KELVIN" and para_escala == "CELSIUS":
        return valor - 273

    if de_escala == "KELVIN" and para_escala =="FAHRENHEIT":
        return (valor - 273) * 1.8 + 32
    
    if de_escala == "CELSIUS" and para_escala == "KELVIN":
        return valor + 273
    
    if de_escala == "CELSIUS" and para_escala == "FAHRENHEIT":
        return valor * 1.8 + 32
    
    if de_escala == "FAHRENHEIT" and para_escala == "CELSIUS":
        return (valor - 32) / 1.8
    
    if de_escala == "FAHRENHEIT" and para_escala == "KELVIN":
        return (valor - 32) * 5/9 + 273
    
    # Se as escalas de origem e destino forem as mesmas, deve retornar o valor original.
    if de_escala == "CELSIUS" and para_escala == "CELSIUS":
        return valor
    
    if de_escala == "FAHRENHEIT" and para_escala == "FAHRENHEIT":
        return valor
    
    if de_escala == "KELVIN" and para_escala == "KELVIN":
        return valor
    
    