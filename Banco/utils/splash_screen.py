import mysql.connector
from utils.db_config import db_config

class FornecedorController:
    def __init__(self, db_config):
        self.db_config = db_config

    def contar_fornecedores(self):
        try:
            conexao = mysql.connector.connect(**self.db_config)
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM fornecedores")
            return cursor.fetchone()[0]
        except mysql.connector.Error as err:
            print(f"Erro ao consultar o banco de dados: {err}")
            return 0
        finally:
            cursor.close()
            conexao.close()

class ProdutosController:
    def __init__(self, db_config):
        self.db_config = db_config

    def contar_produtos(self):
        try:
            conexao = mysql.connector.connect(**self.db_config)
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM produtos")
            return cursor.fetchone()[0]
        except mysql.connector.Error as err:
            print(f"Erro ao consultar o banco de dados: {err}")
            return 0
        finally:
            cursor.close()
            conexao.close()

def exibir_splash_screen():
    fornecedor_controller = FornecedorController(db_config)
    produtos_controller = ProdutosController(db_config)
    total_fornecedores = fornecedor_controller.contar_fornecedores()
    total_produtos = produtos_controller.contar_produtos()


    print("*************************************")
    print("        Bem-vindo ao Sistema         ")
    print("Sistema de Gerenciamento de Estoque")
    print("Máquinas Elétricas e Ferramentas Manuais")
    print("*************************************")
    print("Criado Por: Kayke, João Guilherme")
    print("Periodo: 2024/2")
    print("Professor: Howard Cruz Roatti")
    print("Diciplina: Banco De Dados")
    print("*************************************")
    print(f"Total de Fornecedores: {total_fornecedores}")
    print(f"Total de Produtos: {total_produtos}")
    print("\nCarregando o sistema, aguarde...")

if __name__ == "__main__":
    exibir_splash_screen()
