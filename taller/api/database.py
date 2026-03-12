import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="root123",
        database="sistema_expedientes"
    )
    return connection