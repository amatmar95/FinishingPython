# Codigo que calcule el area y volumen de un cubo dado su lado

def principal():
    # Entrada
    lado = float(input("Lado del cubo:"))

    # Proceso
    area = 6 * lado * lado
    volumen = lado * lado * lado

    # Salida
    print(f"Area del cubo:{area}")
    print(f"Volumen del cubo:{volumen}")

if __name__ == '__main__':
   principal()