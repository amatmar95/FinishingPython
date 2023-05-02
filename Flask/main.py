#Menú principal
import os
from Ejercicio2_app import EjercicioSalario
#from Salario import Salario
#from ejercicio2 import ejercicio2
#from ejercicio4 import ejercicio4
#from ejercicio5 import ejercicio5
#from ejercicio6 import ejercicio6


while True:
    os.system("cls") #Limpia la pantalla cada vez que se vuelve al menú
    print("Bienvenido/a al Menú principal. Este programa recoge todos los ejercicios de Algoritmos. Seleccione el algoritmo que desea usar de la lista.")
    print("1 - Cálculo de letra DNI.")
    print("2 - Cálculo del salario")
    print("4 - Área y perímetro de un círculo")
    print("5 - Ordenación de números enteros.")
    print("6 - Conversor de Farenheit a Celsius")
    print("7 - Determinar si un número es par o impar")
    
    
    try:
        opcion = int(input("Introduzca el número del algoritmo que quiere usar o introduzca 0 para cerrar el programa: "))
    except Exception:
        print("No ha seleccionado un ejercicio válido")

    if opcion == 0: 
        input("Gracias por usar el programa. Pulse ENTER para salir.")
        break
    elif opcion == 1:
        EjercicioSalario()
    # elif opcion == 2:
    #     ejercicio2() 
    # elif opcion == 4:
    #     ejercicio4()   
    # elif opcion == 5:
    #     ejercicio5()  
    # elif opcion == 6:
    #     ejercicio6()   
    # elif opcion == 7:
    #     ejercicio7()  
    
    else:
        "No ha seleccionado un número correcto"
    input("Pulsa Enter para continuar.")