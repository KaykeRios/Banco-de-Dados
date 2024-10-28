class Fornecedor:
    def __init__(self, cnpj, nome_juridico, marca, endereco=None, telefone=None, email=None, id=None):
        self.cnpj = cnpj
        self.nome_juridico = nome_juridico
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.marca = marca
        self.id = id

    def get_CNPJ(self):
        return self.cnpj

    def get_Nome_juridico(self):
        return self.nome_juridico

    def get_Endereco(self):
        return self.endereco

    def get_Telefone(self):
        return self.telefone

    def get_Email(self):
        return self.email
    
    def get_Marca(self):
        return self.marca
    
    def get_id(self):
        return self.id
    
    def set_CNPJ(self, cnpj):
        self.cnpj = cnpj

    def set_Nome_juridico(self, nome_juridico):
        self.nome_juridico = nome_juridico

    def set_Endereco(self, endereco):
        self.endereco = endereco

    def set_Telefone(self, telefone):
        self.telefone = telefone

    def set_Email(self, email):
        self.email = email

    def set_Marca(self,marca):
        self.marca = marca

    def set_id(self,id):
        self.id = id

    def to_string(self) -> str:        
        return (
            f"CNPJ: {self.get_CNPJ()} | "
            f"Nome_juridico: {self.get_Nome_juridico().capitalize()} | "
            f"Endereço: {self.get_Endereco()} | "
            f"Telefone: {self.get_Telefone()} | "
            f"E-mail: {self.get_Email()} | "
            f"Marca: {self.get_Marca()} | "
            f"ID: {self.get_id()} "
        )
