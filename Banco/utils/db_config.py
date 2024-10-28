import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Kyk1502',
    'database': 'dados'
}

def connect_to_database(config):
    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
connection = connect_to_database(db_config)

if connection:
    connection.close()
