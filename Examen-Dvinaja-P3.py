from flask import Flask, jsonify
import platform
import requests

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def obtener_info_sistema():
    info_sistema = {
        "nombre": platform.system(),
        "version": platform.version(),
        "arquitectura": platform.architecture()[0]
    }
    return jsonify(info_sistema)

def obtener_info_sistema_desde_api():
    url_api = "http://192.168.137.57:5000/info"  

    try:
        response = requests.get(url_api)
        if response.status_code == 200:
            datos = response.json()
            print("Datos del sistema operativo:")
            print("Nombre:", datos["nombre"])
            print("Versión:", datos["version"])
            print("Arquitectura:", datos["arquitectura"])
        else:
            print("Error al obtener los datos del sistema. Código de estado:", response.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    obtener_info_sistema_desde_api()
    app.run(debug=True)

    app.run(debug=True)