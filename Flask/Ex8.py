# Codigo que determine si un año es bisiesto o no

def principal():
    # Entrada
    anoBisiesto = int(input("Please type a year:"))

    # Proceso
    def bisiesto(n):
        if n % 4 != 0:
            resultado = False
        elif n % 100 != 0:
            resultado = True
        elif n % 400 != 0:
            resultado = False
        else:
            resultado = True
        return resultado

    # Salida
    print(bisiesto(anoBisiesto))

if __name__ == '__main__':
   principal()