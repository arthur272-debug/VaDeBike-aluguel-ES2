from models import Nacionalidade

class CiclistaDto:

    def __init__(self,nome:str,nascimento:str,cpf:str,passaporte:object,nacionalidade,email:str,urlFotoDocumento:str,id:int):
        self.nome= nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.email = email
        self.urlFotoDocumento = urlFotoDocumento
        self.id = id