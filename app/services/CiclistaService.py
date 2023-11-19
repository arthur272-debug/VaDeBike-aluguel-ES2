from models import Ciclista

class CiclistaService:

    Ciclista = []

    @staticmethod
    def cadastrar_ciclista(ciclista_dto):
        idCiclista = len(CiclistaService.Ciclista)+1
        ciclista_dto.id=idCiclista
        ciclista =Ciclista.Ciclista(ciclista_dto.nome,ciclista_dto.nascimento,ciclista_dto.cpf,ciclista_dto.passaporte,ciclista_dto.nacionalidade,ciclista_dto.email,ciclista_dto.urlFotoDocumento,ciclista_dto.id,ciclista_dto.senha,ciclista_dto.cadastro)
        CiclistaService.Ciclista.append(ciclista)
        return ciclista
    
    @staticmethod
    def consulta_ciclista(ciclista_id):
        for ciclista in CiclistaService.Ciclista: 
            if ciclista.id==ciclista_id:
                return ciclista
        return None
    
    def consultar_ciclista_email(email):
        for ciclista_email in CiclistaService.Ciclista: 
            if ciclista_email.email==email:
                return True
        return False
    
    @staticmethod
    def atualizar_ciclista(ciclista_id,ciclista_dto): 
        ciclista=CiclistaService.consulta_ciclista(ciclista_id)
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
    def confirmar_email(ciclista_email):
        for ciclista in CiclistaService.Ciclista:
            if ciclista.email ==ciclista_email:
                return True 
        return False