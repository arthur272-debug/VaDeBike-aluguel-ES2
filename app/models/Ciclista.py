from enum import Enum

class Nacionalidade(Enum):

    BRASILEIRA= "BRASILEIRA"
    ESTRANGEIRA= "ESTRANGEIRA"

class Ciclista:

    def __init__(self,nome:str,nascimento:str,cpf:str,passaporte:object,nacionalidade,email:str,urlFotoDocumento:str,id:int):
        self.nome= nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.email = email
        self.urlFotoDocumento = urlFotoDocumento
        self.id = id