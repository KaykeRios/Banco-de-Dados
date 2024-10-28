import mysql.connector
from mysql.connector import Error
import pandas as pd

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """Estabelece a conexão com o banco de dados MySQL."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão com o MySQL foi bem-sucedida!")
        except Error as e:
            print(f"Erro ao se conectar ao MySQL: {e}")

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o MySQL fechada.")

    def write(self, query, data):
        """Insere dados no banco de dados usando uma query parametrizada."""
        if not self.connection or not self.connection.is_connected():
            print("Erro: Conexão não estabelecida.")
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()
            print("Dados inseridos com sucesso.")
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            cursor.close()

    def SQLToDataFrame(self, query):
        """Executa uma consulta SQL e retorna um DataFrame do pandas."""
        if not self.connection or not self.connection.is_connected():
            print("Erro: Conexão não estabelecida.")
            return None
        
        try:
            df = pd.read_sql(query, self.connection)
            return df
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fechar_conexao()

if __name__ == "__main__":
    with MySQLConnection(
        host='localhost',
        user='root',
        password='jgscb2o2+1',
        database='estoque'
    ) as conexao_mysql:
        
        insert_query = "INSERT INTO estoque (coluna1, coluna2) VALUES (%s, %s)"
        data = ('valor1', 'valor2')
        conexao_mysql.write(insert_query, data)
        
        select_query = "SELECT * FROM dados"
        df = conexao_mysql.SQLToDataFrame(select_query)
        print(df)
