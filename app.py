from flask import Flask, jsonify

@app.route('/health')
def health_check():
    return jsonify(status="healthy"), 200
app = Flask(__name__)
@app.route('/health')
def health_check():
    return jsonify(status="healthy"), 200
@app.route('/')
def home():
    return jsonify({"message": "Validación de Saldos Activa"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
