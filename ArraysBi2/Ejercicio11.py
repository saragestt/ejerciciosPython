#Deseamos realizar un programa de cambio de divisas. Para ello debemos almacenar
#en una tabla, los valores de equivalencia en euros. Son los siguientes:
#- Dólar 0,82 euros.
#- Libra esterlina, 1,072 euros.
#- Yen, 0,0075 euros.
#- Dirham, 0.084 euros.
#Capturamos por teclado la cantidad monetaria de la divisa correspondiente y la pasamos
#a la divisa que se nos indique.
#En un primer paso se pedirá : ¿Qué moneda tienes? y Cantidad
#En un segundo paso se pedirá: ¿Qué moneda quieres? Y se mostrará la cantidad
#resultante.

def convertirDivisa(cantidad, moneda_actual, valorMonedas):
    monedas = ["Dólar", "Libra esterlina", "Yen", "Dirham"]
    aEuros = [0.82, 1.072, 0.0075, 0.084]

    nombreMonedas = monedas.index(moneda_actual)
    valorMonedas = monedas.index(valorMonedas)
    euros = cantidad * aEuros[nombreMonedas]
    monedaConvertida = euros / aEuros[valorMonedas]

    return monedaConvertida

nombreMonedas = input("¿Qué moneda tienes? (Dólar, Libra esterlina, Yen, Dirham): ")
cantidad = float(input(f"¿Cuántos {nombreMonedas} tienes? "))
valorMonedas = input("¿Qué moneda quieres? (Dólar, Libra esterlina, Yen, Dirham): ")

resultado = convertirDivisa(cantidad, nombreMonedas, valorMonedas)

print(f"{cantidad} {nombreMonedas} son {resultado} {valorMonedas}")