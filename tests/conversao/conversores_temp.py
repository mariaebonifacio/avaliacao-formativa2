
def converter_temperatura (valor: float, de_escala: str, para_escala: str):
    
    # Transformar em letra maiúscula
    de_escala == de_escala.upper()
    para_escala == para_escala.upper()
    

    # Validação para letra maiúscula -- DE-ESCALA / PARA-ESCALA
    escalas_validas = {"CELSIUS", "FAHRENHEIT", "KELVIN"}
    if de_escala not in escalas_validas or para_escala not in escalas_validas:
        raise ValueError("Escala de temperatura inválida.")
    
    # Se os dois forem iguais, retorna o valor (ex: kelvin == kelvin)
    if de_escala == para_escala:
        return valor


    # O valor para a escala KELVIN não pode ser abaixo do zero absoluto
    if de_escala == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa.")

    # CONVERSÃO
    # kelvin para celsius
    if de_escala == "KELVIN" and para_escala == "CELSIUS":
        return valor - 273
    # Kelvin para Fahrenheit
    if de_escala == "KELVIN" and para_escala =="FAHRENHEIT":
        return (valor - 273) * 1.8 + 32
    # Celsius para Kelvin
    if de_escala == "CELSIUS" and para_escala == "KELVIN":
        return valor + 273
    # Celsius para Fahrenheit
    if de_escala == "CELSIUS" and para_escala == "FAHRENHEIT":
        return valor * 1.8 + 32
    # Fahrenheit para Celsius
    if de_escala == "FAHRENHEIT" and para_escala == "CELSIUS":
        return (valor - 32) / 1.8
    # Fahrenheit para Kelvin
    if de_escala == "FAHRENHEIT" and para_escala == "KELVIN":
        return (valor - 32) * 5/9 + 273
    
    