import mysql.connector
from utils.db_config import db_config
from Controller.produto_controller import ProdutosController

class RelatorioProdutos:
    def __init__(self, db_config):
        self.db_config = db_config
        self.controller = ProdutosController(db_config)

    def conectar(self):
        """Estabelece uma conexão com o banco de dados e retorna a conexão e o cursor."""
        try:
            conexao = mysql.connector.connect(**self.db_config)
            if conexao.is_connected():
                return conexao, conexao.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None, None

    def gerar_relatorio(self):
        """Gera o relatório de produtos e exibe suas informações."""
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        sql = "SELECT id, nome, tipo, quantidade FROM produtos"  # Removida a vírgula extra
        
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            if not resultados:
                print("Nenhum dado encontrado para o relatório de produtos.")
            else:
                print("Relatório de Produtos:")
                for produto in resultados:
                    print(f"id: {produto[0]}, nome: {produto[1]}, tipo: {produto[2]}, quantidade: {produto[3]}")  # Corrigido o plural

        except mysql.connector.Error as err:
            print(f"Erro ao consultar o banco de dados: {err}")
        
        finally:
            cursor.close()
            conexao.close()

    def menu_principal(self):
        """Menu principal para gerar relatórios."""
        while True:
            self.gerar_relatorio()
            voltar = input("Pressione 'Enter' para voltar ao menu principal...")
            if voltar == "":
                break

if __name__ == "__main__":
    relatorio = RelatorioProdutos(db_config)
    relatorio.menu_principal()
