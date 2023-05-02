#Crea un algoritmo que convierta grados Celsius a Fahrenheit.

def Salario(salarioBase,pagasExtras,complementos,otrosConceptosRetributivos,irpf,seguridadSocial):
    salarioBase = float(salarioBase)
    pagasExtras = float(pagasExtras)
    complementos = float(complementos)
    otrosConceptosRetributivos = float(otrosConceptosRetributivos)
    irpf = float(irpf)/100
    seguridadSocial = float(seguridadSocial)/100

    salarioBruto = salarioBase + pagasExtras + complementos + otrosConceptosRetributivos
    deducciones = (irpf * salarioBruto) + (seguridadSocial * salarioBruto)
    deducciones = float (deducciones)
    salarioNeto = salarioBruto - deducciones

    return "El salario bruto es:{n:5.2f} y el salario neto es: {m:5.2f}".format(n=salarioBruto,m=salarioNeto) 


if __name__ == "__main__":
    salarioBase = float(input("Introduce el salario base: "))
    pagasExtras = float(input("Introduce las pagas extras: "))
    complementos = float(input("Introduce los complementos: "))
    otrosConceptosRetributivos = float(input("Introduce otros conceptos retributivos: "))
    irpf = float(input("Introduzca el  irpf: ")) / 100.0
    seguridadSocial = float(input("Introduzca la retención para la seguridad social: ")) / 100.0
    salario = Salario(salarioBase,pagasExtras,complementos,otrosConceptosRetributivos,irpf,seguridadSocial)
    print(salario)
