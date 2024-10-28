import mysql.connector
from utils import db_config

class RelatorioFornecedores:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            conexao = mysql.connector.connect(**self.db_config)
            return conexao
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    def gerar_relatorio(self):
        """Gera o relatório de fornecedores e exibe suas informações."""
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = "SELECT cnpj, nome_juridico, endereco, telefone, email, marca FROM fornecedores"
        
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            if not resultados:
                print("Nenhum fornecedor encontrado.")
            else:
                print("Relatório de Fornecedores:")
                for fornecedor in resultados:
                    print(f"CNPJ: {fornecedor[0]}, Nome: {fornecedor[1]}, Endereço: {fornecedor[2]}, "
                          f"Telefone: {fornecedor[3]}, Email: {fornecedor[4]}, Marca: {fornecedor[5]}")
        
        except mysql.connector.Error as err:
            print(f"Erro ao consultar o banco de dados: {err}")
        
        finally:
            cursor.close()
            conexao.close()

    def menu_principal(self):
        """Menu principal para retornar ao menu inicial."""
        while True:
            self.gerar_relatorio()
            voltar = input("Pressione 'Enter' para voltar ao menu principal...")
            if voltar == "":
                break


if __name__ == "__main__":
    relatorio = RelatorioFornecedores(db_config)
    relatorio.menu_principal()
