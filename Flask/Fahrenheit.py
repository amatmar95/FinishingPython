#Crea un algoritmo que convierta grados Celsius a Fahrenheit.

def Fahrenheit(celsius):
    celsius=float(celsius)
    fahrenheit = (celsius * 1.8) + 32

    return "La temperatura en fahrenheit es: {n:5.2f}".format(n=fahrenheit)


if __name__ == "__main__":
    celsius = float(input("Introduzca la temperatura en grados Celsius: "))
    temperatura = Fahrenheit(celsius)
    print(temperatura)
