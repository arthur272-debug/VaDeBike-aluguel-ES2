from services import CiclistaService
from models import Bicicleta_fake,Aluguel # será substituido


lista_ciclista = CiclistaService.CiclistaService.Ciclista

alugueis_historico = []

class AluguelService:

    @staticmethod
    # integração aqui (pega a bicicleta aqui)
    def verificar_bicicleta_alugada(id_ciclista): 
        aluguel = None
        ciclista= None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                break
            ciclista = None

        if ciclista is None:
            return False

        bicicleta = Bicicleta_fake.bicicleta(ciclista.aluguel.bicicleta,"boa","3235","2022",100,"normal") # pega a informação de outro microsserviço
        if (aluguel is not None):
            return bicicleta
        else:
            return None


    @staticmethod
    def verificar_ciclista_aluguel(id_ciclista): 
        aluguel = None
        ciclista = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                return aluguel
          
        return ciclista==False
    
    @staticmethod
    def alugar_bicicleta(aluguel_dto): #integração aqui
       ciclista = None
       for ciclista in lista_ciclista:
           if ciclista.id == aluguel_dto.ciclista:
              if ciclista.aluguel is not None:
                  return None
              aluguel = Aluguel.Aluguel(aluguel_dto.ciclista,aluguel_dto.trancaInicio,aluguel_dto.bicicleta,aluguel_dto.horaInicio,aluguel_dto.trancaFim,aluguel_dto.horaFim,aluguel_dto.cobranca)
              ciclista.aluguel = aluguel
              break
           ciclista = None
        
       if ciclista is None:
          return ciclista
       
       # pega as informações dos outros microsserviços
       ciclista.aluguel.trancaInicio = aluguel_dto.trancaInicio
       ciclista.aluguel.bicicleta = len(alugueis_historico)+1 # muda -- fake
       ciclista.aluguel.horaInicio = 0
       ciclista.aluguel.cobranca = 0  
      
       return ciclista.aluguel
    
    @staticmethod
    def devolver_bicicleta(id_ciclista,id_tranca): #integração aqui
       aluguel = None
       for ciclista in lista_ciclista:
           if ciclista.id == id_ciclista:
              aluguel = ciclista.aluguel
              break
        
       if aluguel is None:
          return aluguel
       
       # pega as informações dos outros microsserviços
       aluguel.trancaFim =0 
       aluguel.horaFim = 0
       aluguel.cobranca = 0+ 30

       # informações do aluguel e pagamento serão repassadas para seus microsserviços respectivos
       alugueis_historico.append(aluguel)
       ciclista.aluguel = None
       return aluguel
    