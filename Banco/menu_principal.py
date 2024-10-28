
import mysql.connector
from Controller.fornecedor_controller import FornecedorController
from Controller.produto_controller import ProdutosController
from Model.Fornecedor import Fornecedor
from Model.Produtos import Produtos
from utils.db_config import db_config
from utils.splash_screen import exibir_splash_screen
from relatorios.relatorio_fornecedores import RelatorioFornecedores
from relatorios.relatorio_produtos import RelatorioProdutos

def escolher_tipo():
    while True:
        print("\nEscolha o tipo de registro:")
        print("1. Fornecedor")
        print("2. Produto")
        
        escolha = input("Escolha uma opção (1-2): ")
        
        if escolha == '1':
            return 'fornecedor'
        elif escolha == '2':
            return 'produto'
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu():
    exibir_splash_screen()
    fornecedor_controller = FornecedorController(db_config)
    produtos_controller = ProdutosController(db_config)

    while True:
        print("*************************************")
        print("\nMenu Principal:")
        print("1. Relatórios")
        print("2. Inserir Registros")
        print("3. Remover Registros")
        print("4. Atualizar Registros")
        print("5. Fechar o Sistema")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            menu_relatorios(fornecedor_controller, produtos_controller)
        
        elif escolha == '2':
            tipo = escolher_tipo()
            if tipo == 'fornecedor':
                fornecedor_controller.inserir_fornecedor()
            elif tipo == 'produto': 
                produtos_controller.inserir_produto()
        elif escolha == '3':
            tipo = escolher_tipo()
            if tipo == 'fornecedor':                
                fornecedor_controller.remover_fornecedor()
            elif tipo == 'produto':                
                produtos_controller.remover_produto()
        elif escolha == '4':
            tipo = escolher_tipo()
            if tipo == 'fornecedor':                
                fornecedor_controller.atualizar_fornecedor()
                
            elif tipo == 'produto':                
                produtos_controller.atualizar_produto()
        
        elif escolha == '5':
            print("Fechando o sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

def menu_relatorios(fornecedor_controller, produtos_controller):
    while True:
        print("\nEscolha um relatório:")
        print("1. Relatório de Fornecedores")
        print("2. Relatório de Produtos")
        print("3. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            relatorio_fornecedores = RelatorioFornecedores(fornecedor_controller.db_config)
            relatorio_fornecedores.gerar_relatorio()  
        elif escolha == '2':
            relatorio_produtos = RelatorioProdutos(produtos_controller.db_config)
            relatorio_produtos.gerar_relatorio()  
        elif escolha == '3':
            print("Voltando ao menu principal...")
            return
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    exibir_menu()
