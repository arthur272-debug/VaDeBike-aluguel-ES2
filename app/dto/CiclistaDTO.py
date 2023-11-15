
class Passaporte:

    def __init__(self,numero:str,validade:str,pais:str):
        self.numero = numero
        self.validade = validade
        self.pais = pais
 

class CiclistaDto:

    def __init__(self,nome:str,nascimento:str,cpf:str,passaporte:object,nacionalidade,email:str,urlFotoDocumento:str,id:int,senha:str,cadastro):
        self.nome= nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.email = email
        self.urlFotoDocumento = urlFotoDocumento
        self.id = id
        self.senha = senha