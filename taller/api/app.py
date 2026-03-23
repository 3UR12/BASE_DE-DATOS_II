from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)


@app.route('/')
def home():
    return "API de Sistema de Expedientes funcionando"


# =========================
# GET - Obtener todos
# =========================
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(usuarios)


# =========================
# GET - Obtener uno
# =========================
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id,))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404


# =========================
# POST - Crear usuario
# =========================

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    required_fields = ['nombre', 'usuario', 'password', 'rol']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO usuarios (nombre, usuario, password, rol)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        data['nombre'],
        data['usuario'],
        data['password'],
        data['rol']
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Usuario creado correctamente"}), 201

'''
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()

    # Validar JSON
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    # Validar campos
    required_fields = ['nombre', 'usuario', 'password', 'rol']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO usuarios (nombre, usuario, password, rol)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        data['nombre'],
        data['usuario'],
        data['password'],
        data['rol']
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Usuario creado correctamente"}), 201
'''

# =========================
# PUT - Actualizar usuario
# =========================
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()

    # Validar JSON
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    # Validar campos
    required_fields = ['nombre', 'usuario', 'password', 'rol']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE usuarios
        SET nombre=%s, usuario=%s, password=%s, rol=%s
        WHERE id_usuario=%s
    """

    values = (
        data['nombre'],
        data['usuario'],
        data['password'],
        data['rol'],
        id
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Usuario actualizado correctamente"})


# =========================
# DELETE - Eliminar usuario
# =========================
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Usuario eliminado correctamente"})


if __name__ == '__main__':
    app.run(debug=True)

















'''
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

    '''