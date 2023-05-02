from Flask import Flask,request
import Circulo

app = Flask(__name__)

@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular área y perímetro</title>
    </head>
    <body>
        <h1>Calcular área y perímetro de círculo</h1>
        <form method="post" action="/validar">
            <label for="radio">Radio: </label>
            <input type="number" name="radio" id="radio">
            <br>
            <input type="submit" value="Calcular">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     radio= request.form["radio"]
     resultado=Circulo.Circulo(radio)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular área y perímetro de círculo</title>
    </head>
    <body>
        <h1>Área y perímetro calculados</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """
if __name__ == "__main__":
    app.run()