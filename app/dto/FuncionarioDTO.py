class FuncionarioDto:
    
    def __init__(self,senha:str,cpf:float,email:str,documento:str,funcao:str,idade:int,nome:str):
        self.senha= senha
        self.cpf= cpf
        self.email= email
        self.documento= documento
        self.funcao= funcao
        self.idade = idade
        self.nome = nome