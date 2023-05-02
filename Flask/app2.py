
from flask import Flask,request
import Salario


app = Flask(__name__)

@app.route('/Ejercicio2')
#@app.route('/index')

def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular salario</title>
    </head>
    <body>
        <h1>Calculadora salario</h1>
        <form method="post" action="/validar">
            <label for="salariobase">Salario base: </label>
            <input type="number" name="salariobase" id="salariobase">
            <br>
            <label for="pagasextras">Pagas extras: </label>
            <input type="number" name="pagasextras" id="pagasextras">
            <br>
            <label for="complementos">Complementos: </label>
            <input type="number" name="complementos" id="complementos">
            <br>
            <label for="otrosconceptos">Otros conceptos retributivos: </label>
            <input type="number" name="otrosconceptos" id="otrosconceptos">
            <br>
            <label for="irpf">Irpf: </label>
            <input type="number" name="irpf" id="irpf">
            <br>
            <label for="seguridadsocial">Seguridad social: </label>
            <input type="number" name="seguridadsocial" id="seguridadsocial">
            <br>
            <input type="submit" value="Calcular">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
    salarioBase= request.form["salariobase"]
    pagasExtras= request.form["pagasextras"]
    complementos= request.form["complementos"]
    otrosConceptosRetributivos= request.form["otrosconceptos"]
    irpf= request.form["irpf"]
    seguridadSocial= request.form["seguridadsocial"]
    resultado=Salario.Salario(salarioBase,pagasExtras,complementos,otrosConceptosRetributivos,irpf,seguridadSocial)
    return f"""
<!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora salario bruto y neto</title>
    </head>
    <body>
        <h1>Salario calculado</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """
if __name__ == "__main__":
    app.run()