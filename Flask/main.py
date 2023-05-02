from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return """
    <!doctype html>
    <html>
    <head>
    <title>Ejercicios con Flask</title>
    </head>
     <body>
    <h1>Bienvenido al menú de ejercicios de algoritmos</h1>
    <p>Seleccione una opcion: </p>
    <ul>
      <li><a href="/Ejercicio2">Ejercicio 2</a></li>
      <li><a href="/ejercicio2">Ejercicio 2</a></li>
      <li><a href="/ejercicio3">Ejercicio 3</a></li>
      <li><a href="/ejercicio4">Ejercicio 4</a></li>
      <li><a href="/ejercicio5">Ejercicio 5</a></li>
      <li><a href="/ejercicio6">Ejercicio 6</a></li>
    </ul>
  </body>
</html>
"""

@app.route('/Ejercicio2')
def Ejercicio2():
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














# from flask import Flask,request
# from Ejercicio2_app import Salario

# app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Ejercicios con Flask</title>
#     </head>
#     <body>
#         <h1>Seleccione un ejercicio:</h1>
#             <form method="get" action="/appEj06">
#                 <input  type="submit" value="Ejercicio 1 - Salario">
#             </form>
#             <form method="get" action="/appEj07">
#                 <input  type="submit" value="Ejercicio 2 - ">
#             </form>
#             <form method="get" action="/appEj08">
#                 <input  type="submit" value="Ejercicio 3 - ">
#             </form>
#             <form method="get" action="/appEj11">
#                 <input  type="submit" value="Ejercicio 4 - ">
#             </form>
#             <form method="get" action="/appEj12">
#                 <input  type="submit" value="Ejercicio 5 - ">
#             </form>
#             <form method="get" action="/appEj13">
#                 <input  type="submit" value="Ejercicio 6 - ">
#             </form>
#     </body>
#     </html>
#     """

# @app.route('/validar', methods=['POST'])
# def validar():
#     salarioBase= request.form["salariobase"]
#     pagasExtras= request.form["pagasextras"]
#     complementos= request.form["complementos"]
#     otrosConceptosRetributivos= request.form["otrosconceptos"]
#     irpf= request.form["irpf"]
#     seguridadSocial= request.form["seguridadsocial"]
#     resultado=Salario.Salario(salarioBase,pagasExtras,complementos,otrosConceptosRetributivos,irpf,seguridadSocial)
#     return f"""
# <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Calculadora salario bruto y neto</title>
#     </head>
#     <body>
#         <h1>Salario calculado</h1>
#         <p>{resultado}</p>
#     </body>
#     </html>
#         """
# if __name__ == "__main__":
#     app.run()












