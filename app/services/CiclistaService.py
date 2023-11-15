from models import Ciclista

class CiclistaService:

    Ciclista = []

    @staticmethod
    def cadastrarCiclista(ciclista_dto):
        idCiclista = len(CiclistaService.Ciclista)+1
        ciclista_dto.id=idCiclista
        ciclista =Ciclista.Ciclista(ciclista_dto.nome,ciclista_dto.nascimento,ciclista_dto.cpf,ciclista_dto.passaporte,ciclista_dto.nacionalidade,ciclista_dto.email,ciclista_dto.urlFotoDocumento,ciclista_dto.id,ciclista_dto.senha,ciclista_dto.cadastro)
        CiclistaService.Ciclista.append(ciclista)
        return ciclista
    
    @staticmethod
    def consultarCiclista(idCiclista):
        for ciclista in CiclistaService.Ciclista: 
            if ciclista.id==idCiclista:
                return ciclista
        return None
    
    @staticmethod
    def atualizarCiclista(idCiclista,ciclista_dto): # ver a parte da nacionalidade
        ciclista=CiclistaService.consultarCiclista(idCiclista)
        if ciclista is not None:
            ciclista.nome = ciclista_dto.nome
            ciclista.nascimento= ciclista_dto.nascimento
            ciclista.cpf = ciclista_dto.cpf
            ciclista.passaporte = ciclista_dto.passaporte
            ciclista.nacionalidade = ciclista_dto.nacionalidade
            ciclista.email = ciclista_dto.email
            ciclista.urlFotoDocumento = ciclista_dto.urlFotoDocumento
            ciclista.senha = ciclista_dto.senha
            return ciclista
        return None
    
    @staticmethod
    def confirmarEmail(ciclistaEmail):
        for ciclista in CiclistaService.Ciclista:
            if ciclista.email ==ciclistaEmail:
                return True 
        return False