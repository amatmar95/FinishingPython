from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
