import mysql.connector
from mysql.connector import Error
from utils.db_config import db_config
from Model.Fornecedor import Fornecedor

class FornecedorController:
    
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados")
                return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def inserir_no_banco(self, fornecedor: Fornecedor):
        """Insere um novo fornecedor no banco de dados."""        
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = """INSERT INTO fornecedores (cnpj, nome_juridico, endereco, telefone, email, marca, id)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (fornecedor.get_CNPJ(), fornecedor.get_Nome_juridico(), fornecedor.get_Endereco(), 
                   fornecedor.get_Telefone(), fornecedor.get_Email(), fornecedor.get_Marca(), fornecedor.get_id())
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Fornecedor inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir o fornecedor: {e}")
        finally:
            cursor.close()
            conexao.close()

    def inserir_fornecedor(self):
        """Função para inserir fornecedores com confirmação para continuar inserindo."""
        while True:
            nome_juridico = input("Nome do fornecedor (ou digite 'sair' para voltar ao menu): ")
            if nome_juridico.lower() == 'sair':
                print("Voltando ao menu principal...")
                return
            
            cnpj = input("CNPJ do fornecedor: ")
            endereco = input("Endereço do fornecedor: ")
            telefone = input("Telefone do fornecedor: ")
            email = input("Email do fornecedor: ")
            marca = input("Marca do Fornecedor: ")
            id = input("ID do Fornecedor: ")
            
            fornecedor = Fornecedor(cnpj=cnpj, nome_juridico=nome_juridico, endereco=endereco, telefone=telefone, email=email, marca=marca, id=id)
            self.inserir_no_banco(fornecedor)
            
            if not self.continuar_inserir():
                break

    def continuar_inserir(self):
        """Pergunta ao usuário se ele deseja continuar inserindo registros."""        
        while True:
            resposta = input("Deseja inserir mais algum registro? (Sim/Não): ")
            if resposta.lower() == 'sim':
                return True
            elif resposta.lower() == 'não':
                return False
            else:
                print("Resposta inválida, tente novamente.")

    def verificar_cnpj_existente(self, cnpj):
        """Verifica se o CNPJ existe no banco de dados."""
        conexao = self.conectar()
        if not conexao:
            return False
        
        cursor = conexao.cursor()
        
        sql = "SELECT COUNT(*) FROM fornecedores WHERE cnpj = %s"
        cursor.execute(sql, (cnpj,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexao.close()
        
        return resultado[0] > 0

    def atualizar_fornecedor(self):
        """Atualiza um fornecedor existente no banco de dados, solicitando dados do usuário."""
        cnpj = input("Diga o CNPJ a atualizar: ")        

        if not self.verificar_cnpj_existente(cnpj):
            print("Erro: O CNPJ informado não existe no banco de dados.")
            return
        
        novo_cnpj = input("Novo CNPJ (pressione Enter para manter o mesmo): ") or cnpj
        nome_juridico = input("Novo nome jurídico (pressione Enter para manter o mesmo): ")
        endereco = input("Endereço do fornecedor (pressione Enter para manter o mesmo): ")
        telefone = input("Telefone do fornecedor (pressione Enter para manter o mesmo): ")
        email = input("Email do fornecedor (pressione Enter para manter o mesmo): ")
        marca = input("Nova marca (pressione Enter para manter o mesmo): ")
        id = input("Novo ID do Fornecedor(pressione Enter para manter o mesmo): ")

        fornecedor = Fornecedor(
            cnpj=novo_cnpj,
            nome_juridico=nome_juridico if nome_juridico else None,
            endereco=endereco if endereco else None,
            telefone=telefone if telefone else None,
            email=email if email else None,
            marca=marca if marca else None,
            id=id if id else None
        )
        
        self.atualizar_no_banco(cnpj, fornecedor)

    def atualizar_no_banco(self, cnpj, fornecedor: Fornecedor):
        """Atualiza um fornecedor existente no banco de dados."""
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = """UPDATE fornecedores
                 SET cnpj = %s, nome_juridico = %s, endereco = %s, telefone = %s, email = %s, marca = %s, id =%s
                 WHERE cnpj = %s"""  
        valores = (fornecedor.get_CNPJ(), fornecedor.get_Nome_juridico(), fornecedor.get_Endereco(),
                   fornecedor.get_Telefone(), fornecedor.get_Email(), fornecedor.get_Marca(), fornecedor.get_id(), cnpj)
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Fornecedor atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar o fornecedor: {e}")
        finally:
            cursor.close()
            conexao.close()

    def remover_fornecedor(self):
        """Remove um fornecedor do banco de dados, solicitando o CNPJ do usuário."""        
        cnpj = input("CNPJ do fornecedor a remover: ")
        self.remover_do_banco(cnpj)

    def remover_do_banco(self, cnpj):
        """Remove um fornecedor do banco de dados."""        
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = """DELETE FROM fornecedores WHERE cnpj = %s"""  
        
        try:
            cursor.execute(sql, (cnpj,))
            conexao.commit()
            print("Fornecedor removido com sucesso!")
        except Error as e:
            print(f"Erro ao remover o fornecedor: {e}")
        finally:
            cursor.close()
            conexao.close()

    def listar_fornecedores(self):
        """Lista todos os fornecedores do banco de dados."""        
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = "SELECT * FROM fornecedores"
        
        try:
            cursor.execute(sql)
            fornecedores = cursor.fetchall()
            if fornecedores:
                for f in fornecedores:
                    print(f)
            else:
                print("Nenhum fornecedor encontrado.")
        except Error as e:
            print(f"Erro ao listar fornecedores: {e}")
        finally:
            cursor.close()
            conexao.close()

    def obter_valor_total_pedidos_por_fornecedor(self):
        """Obtém o valor total de pedidos por fornecedor."""        
        conexao = self.conectar()
        if not conexao:
            return
        
        cursor = conexao.cursor()
        
        sql = """
        SELECT f.nome_juridico, SUM(p.valor) AS total_pedidos
        FROM fornecedores f
        JOIN pedidos p ON f.cnpj = p.cnpj
        GROUP BY f.nome_juridico
        """
        
        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for resultado in resultados:
                print(f"Fornecedor: {resultado[0]}, Total de Pedidos: {resultado[1]}")
            return resultados
        except Error as e:
            print(f"Erro ao obter valores totais de pedidos por fornecedor: {e}")
        finally:
            cursor.close()
            conexao.close()
