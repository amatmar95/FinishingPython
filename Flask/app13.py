from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_area_volumen(lado):
    area = 6 * lado * lado
    volumen = lado * lado * lado
    return area, volumen

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
