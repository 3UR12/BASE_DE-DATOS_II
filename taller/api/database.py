import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3307,
            user='root',
            password='root123',
            database='sistema_expedientes'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None







#
#
#def get_connection():
#   connection = mysql.connector.connect(
#        host="localhost",
#       port=3307,
#        user="root",
#        password="root123",
#        database="sistema_expedientes"
#    )
#    return connection