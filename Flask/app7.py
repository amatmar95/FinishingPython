from flask import Flask, request, jsonify

app = Flask(__name__)

def par_impar(n):
    if n % 2 == 0:
        resultado = ("El numero es par")
    else:
        resultado = ("El numero es impar")
    return resultado

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
