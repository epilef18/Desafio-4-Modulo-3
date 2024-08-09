import sys

def conversor():
    argumentos = sys.argv

    soles = float(argumentos[1])
    pesoargentino = float(argumentos[2])
    dolar = float(argumentos[3])
    pesochileno = float(argumentos[4])

    if pesochileno>0:
        print(f'Los {pesochileno} pesos equivalen a:')
    else:
        print("La cantidad de pesos chilenos debe ser un número positivo")

    if soles>0:
        sol = pesochileno*soles
        print(f'{sol} Soles')
    else:
        print("Las taza de conversión de sol debe ser un número positivo")

    if pesoargentino>0:
        pa = pesochileno*pesoargentino
        print(f'{pa} Pesos Argentinos')
    else:
        print("Las taza de conversión de peso argentino debe ser uun número positivos")
    
    if dolar>0:
        usd = pesochileno*dolar
        print(f'{usd} Dólares')
    else:
        print("Las tazas de conversión de dolar debe ser un número positivo")

conversor()