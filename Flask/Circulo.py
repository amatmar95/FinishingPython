#Calcula el área y perímetro de un círculo dado su radio.

import math

def Circulo(radio):
        radio= float(radio)
        areaCirculo = radio ** 2 * math.pi
        perimetroCirculo = radio * 2 * math.pi

        return "El area del circulo es: {n:5.2f} y el perimetro es {m:5.2f}".format(n=areaCirculo,m=perimetroCirculo)

if __name__ == "__main__":
    radio = float(input("Introduzca el radio del circulo: "))
    circulo = Circulo(radio)
    print(circulo)