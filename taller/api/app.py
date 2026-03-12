from flask import Flask, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensaje": "API del sistema de expedientes funcionando"}

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)