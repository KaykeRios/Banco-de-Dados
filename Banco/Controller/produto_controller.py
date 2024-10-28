import mysql.connector
from mysql.connector import Error
from utils.db_config import db_config
from Model.Produtos import Produtos

class ProdutosController:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar(self):
        """Estabelece uma conexão com o banco de dados e retorna a conexão e o cursor."""
        try:
            conexao = mysql.connector.connect(**self.db_config)
            if conexao.is_connected():
                print("Conexão bem-sucedida ao banco de dados")
                return conexao, conexao.cursor()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None, None

    def verificar_id(self, produto_id):
        """Verifica se um produto com o ID fornecido existe no banco de dados."""
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return False
        cursor.execute("SELECT id FROM produtos WHERE id = %s", (produto_id,))
        existe = cursor.fetchone() is not None
        cursor.close()
        conexao.close()
        return existe

    def inserir_no_banco(self, produto: Produtos):
        """Insere um novo produto no banco de dados."""        
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        sql = """INSERT INTO produtos (nome, tipo, quantidade, id)
                 VALUES (%s, %s, %s, %s)"""
        valores = (produto.get_nome(), produto.get_tipo(), produto.get_quantidade(), produto.get_id())
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Produto inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir o produto: {e}")
        finally:
            cursor.close()
            conexao.close()

    def inserir_produto(self):
        """Função para inserir produtos com confirmação para continuar inserindo."""
        while True:
            nome = input("Digite o nome do Produto (ou 'sair' para voltar ao menu): ")
            if nome.lower() == 'sair':
                print("Voltando ao menu principal...")
                return      
            tipo = input("Tipo do Produto (manual, elétrico, etc): ")
            quantidade = int(input("Quantidade de produtos: "))
            id = int(input("ID do produto: ")) 
            
            produto = Produtos(nome=nome, tipo=tipo, quantidade=quantidade, id=id)
            self.inserir_no_banco(produto)
            
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

    def listar_produtos(self):
        """Lista todos os produtos da tabela produtos."""
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        try:
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            if not produtos:
                print("Nenhum produto encontrado.")
                return
            for produto in produtos:
                print(produto)
        except mysql.connector.Error as err:
            print(f"Erro ao listar produtos: {err}")
        finally:
            cursor.close()
            conexao.close()

    def atualizar_produto(self):
        """Atualiza um produto existente no banco de dados, solicitando dados do usuário."""
        produto_id = int(input("Diga o ID do produto a atualizar: "))        

        if not self.verificar_id(produto_id):
            print("Erro: O ID informado não existe no banco de dados.")
            return
        
        novo_nome = input("Novo nome (deixe em branco para não alterar): ") 
        novo_tipo = input("Novo tipo (deixe em branco para não alterar): ")
        nova_quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
        
        produto = Produtos(
            id=produto_id,
            nome=novo_nome if novo_nome else None,
            tipo=novo_tipo if novo_tipo else None,
            quantidade=int(nova_quantidade) if nova_quantidade else None
        )
        
        self.atualizar_no_banco(produto_id, produto)

    def atualizar_no_banco(self, produto_id, produto: Produtos):
        """Atualiza um produto existente no banco de dados."""
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        sql = """UPDATE produtos
                 SET nome = %s, tipo = %s, quantidade = %s
                 WHERE id = %s"""  
        valores = (produto.get_nome(), produto.get_tipo(), produto.get_quantidade(), produto_id)
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Produto atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar o produto: {e}")
        finally:
            cursor.close()
            conexao.close()

    def remover_produto(self):
        """Remove um produto da tabela produtos pelo seu ID."""  
        produto_id = int(input("Digite o ID do produto a ser removido: "))
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
            conexao.commit()
            print("Produto removido com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao remover produto: {err}")
        finally:
            cursor.close()
            conexao.close()

    def obter_itens_pedido(self):
        """Obtém os itens de um pedido específico."""  
        conexao, cursor = self.conectar()
        if not conexao or not cursor:
            return
        
        pedido_id = int(input("Digite o ID do pedido para obter os itens: "))
        sql = """
        SELECT p.nome, pi.quantidade, pi.preco
        FROM pedidos_itens pi
        JOIN produtos p ON pi.id_produto = p.id
        WHERE pi.id_pedido = %s
        """
        
        try:
            cursor.execute(sql, (pedido_id,))
            itens = cursor.fetchall()
            if itens:
                print(f"Itens do pedido {pedido_id}:")
                for item in itens:
                    print(f"Produto: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]}")
            else:
                print(f"Nenhum item encontrado para o pedido ID {pedido_id}.")
        except mysql.connector.Error as err:
            print(f"Erro ao obter itens do pedido: {err}")
        finally:
            cursor.close()
            conexao.close()
