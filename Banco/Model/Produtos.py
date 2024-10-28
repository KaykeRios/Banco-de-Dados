from Model.Fornecedor import Fornecedor

class Produtos:
    def __init__(self, 
                 nome: str = None, 
                 tipo: str = None,  
                 quantidade: int = None, 
                 id: int = None,
                 fornecedor_id: Fornecedor = None
                 ):
        self.set_nome(nome)
        self.set_tipo(tipo)
        self.set_quantidade(quantidade)
        self.set_id(id)
        self.set_fornecedor_id(fornecedor_id)

    def set_nome(self, nome: str):
        self.nome = nome

    def set_tipo(self, tipo: str):
        self.tipo = tipo    

    def set_quantidade(self, quantidade: int):
        self.quantidade = quantidade

    def set_id(self, id: int):
        self.id = id
    
    def set_fornecedor_id(self, fornecedor_id: int):
        self.fornecedor_id = fornecedor_id
    
    def get_nome(self) -> str:
        return self.nome

    def get_tipo(self) -> str:
        return self.tipo
        
    def get_quantidade(self) -> int:
        return self.quantidade

    def get_id(self) -> int:
        return self.id
    
    def get_fornecedor_id(self) -> int:
        return self.fornecedor_id

    def to_string(self) -> str:
        return (
            f"Nome: {self.get_nome().capitalize()} | "
            f"Tipo: {self.get_tipo()} | "
            f"Quantidade: {self.get_quantidade()} | "
            f"ID: {self.get_id()} | "
            f"Fornecedor_id: {self.get_fornecedor_id()}"
        )