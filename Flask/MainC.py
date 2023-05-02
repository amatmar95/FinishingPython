import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to the exercises!</h1>
        <p>Choose an exercise:</p>
        <ul>
            <li><a href="/bisiesto">Bisiesto</a></li>
            <li><a href="/par-impar">Par o Impar</a></li>
            <li><a href="/area-volumen">Area y Volumen</a></li>
            <li><a href="/Salario">Salario</a></li>
            <li><a href="/celsius_to_fahrenheit">Fahrenheit</a></li>
            <li><a href="/circulo">Circulo</a></li>
        </ul>
    '''

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

@app.route('/bisiesto', methods=['GET', 'POST'])
def bisiesto_endpoint():
    if request.method == 'POST':
        ano = int(request.form['ano'])
        resultado = bisiesto(ano)
        return jsonify({'resultado': resultado})
    else:
        return '''
            <form method="post">
                <label for="ano">Ingrese un año:</label>
                <input type="number" id="ano" name="ano" required>
                <button type="submit">Enviar</button>
            </form>
        '''

def par_impar(n):
    if n % 2 == 0:
        resultado = ("El numero es par")
    else:
        resultado = ("El numero es impar")
    return resultado

@app.route('/par-impar', methods=['GET', 'POST'])
def par_impar_endpoint():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        resultado = par_impar(numero)
        return jsonify({'resultado': resultado})
    else:
        return '''
            <form method="post">
                <label for="numero">Ingrese un número:</label>
                <input type="number" id="numero" name="numero" required>
                <button type="submit">Enviar</button>
            </form>
        '''

def calcular_area_volumen(lado):
    area = 6 * lado * lado
    volumen = lado * lado * lado
    return area, volumen

@app.route('/area-volumen', methods=['GET', 'POST'])
def area_volumen_endpoint():
    if request.method == 'POST':
        lado = float(request.form['lado'])
        area, volumen = calcular_area_volumen(lado)
        return jsonify({'area': area, 'volumen': volumen})
    else:
        return '''
            <form method="post">
                <label for="lado">Ingrese la longitud de un lado:</label>
                <input type="number" step="any" id="lado" name="lado" required>
                <button type="submit">Calcular</button>
            </form>
        '''

def Salario(salarioBase, pagasExtras, complementos, otrosConceptosRetributivos, irpf, seguridadSocial):
    salarioBase = float(salarioBase)
    pagasExtras = float(pagasExtras)
    complementos = float(complementos)
    otrosConceptosRetributivos = float(otrosConceptosRetributivos)
    irpf = float(irpf) / 100
    seguridadSocial = float(seguridadSocial) / 100

    salarioBruto = salarioBase + pagasExtras + complementos + otrosConceptosRetributivos
    deducciones = (irpf * salarioBruto) + (seguridadSocial * salarioBruto)
    deducciones = float(deducciones)
    salarioNeto = salarioBruto - deducciones

    return salarioBruto, salarioNeto

@app.route('/Salario', methods=['GET', 'POST'])
def salario_endpoint():
    if request.method == 'POST':
        salarioBase = request.form['salarioBase']
        pagasExtras = request.form['pagasExtras']
        complementos = request.form['complementos']
        otrosConceptosRetributivos = request.form['otrosConceptosRetributivos']
        irpf = request.form['irpf']
        seguridadSocial = request.form['seguridadSocial']
        resultado = Salario(salarioBase, pagasExtras, complementos, otrosConceptosRetributivos, irpf, seguridadSocial)
        return jsonify({'resultado': resultado})
    else:
        return '''
            <form method="post">
                <label for="salarioBase">Salario Base:</label>
                <input type="number" step="any" id="salarioBase" name="salarioBase" required><br><br>
                <label for="pagasExtras">Pagas Extras:</label>
                <input type="number" step="any" id="pagasExtras" name="pagasExtras" required><br><br>
                <label for="complementos">Complementos:</label>
                <input type="number" step="any" id="complementos" name="complementos" required><br><br>
                <label for="otrosConceptosRetributivos">Otros Conceptos Retributivos:</label>
                <input type="number" step="any" id="otrosConceptosRetributivos" name="otrosConceptosRetributivos" required><br><br>
                <label for="irpf">IRPF:</label>
                <input type="number" step="any" id="irpf" name="irpf" required><br><br>
                <label for="seguridadSocial">Seguridad Social:</label>
                <input type="number" step="any" id="seguridadSocial" name="seguridadSocial" required><br><br>
                <button type="submit">Calcular Salario</button>
            </form>
        '''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

@app.route('/celsius_to_fahrenheit', methods=['GET', 'POST'])
def celsius_to_fahrenheit_endpoint():
    if request.method == 'POST':
        celsius = float(request.form['celsius'])
        fahrenheit = celsius_to_fahrenheit(celsius)
        return jsonify({'fahrenheit': fahrenheit})
    else:
        return '''
            <form method="post">
                <label for="celsius">Enter temperature in Celsius:</label>
                <input type="number" step="any" id="celsius" name="celsius" required>
                <button type="submit">Convert</button>
            </form>
        '''
def circulo(radio):
    radio = float(radio)
    area_circulo = radio ** 2 * math.pi
    perimetro_circulo = radio * 2 * math.pi
    return jsonify({
        'area': area_circulo,
        'perimetro': perimetro_circulo
    })

@app.route('/circulo', methods=['GET', 'POST'])
def circulo_endpoint():
    if request.method == 'POST':
        radio = float(request.form['radio'])
        return circulo(radio)
    else:
        return '''
            <form method="post">
                <label for="radio">Introduzca el radio del círculo:</label>
                <input type="number" step="any" id="radio" name="radio" required>
                <button type="submit">Calcular</button>
            </form>
        '''
if __name__ == '__main__':
    app.run(debug=True)
