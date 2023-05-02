from flask import Flask,request
import Fahrenheit

app = Flask(__name__)

@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular Fahrenheit</title>
    </head>
    <body>
        <h1>Calculadora Fahrenheit</h1>
        <form method="post" action="/validar">
            <label for="temperatura">Temperatura:</label>
            <input type="number" name="celsius" id="celsius">
            <br>
            <input type="submit" value="Calcular">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     celsius= request.form["celsius"]
     resultado=Fahrenheit.Fahrenheit(celsius)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora Fahrenheit</title>
    </head>
    <body>
        <h1>Fahrenheit calculados</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """
if __name__ == "__main__":
    app.run()