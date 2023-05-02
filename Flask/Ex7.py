# Codigo que determine si es par o impar
def principal():
    # Entrada
    numero = int(input("Please type your number:"))

    # Proceso
    def par_impar(n):
        if n % 2 == 0:
            resultado = ("El numero es par")
        else:
            resultado = ("El numero es impar")
        return resultado

    # Salida
    print(par_impar(numero))

if __name__ == '__main__':
   principal()