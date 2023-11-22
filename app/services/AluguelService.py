from services import CiclistaService
from models import Bicicleta_fake # será substituido

lista_ciclista = CiclistaService.CiclistaService.Ciclista

alugueis_historico = []

class AluguelService:


    @staticmethod
    def verificar_bicicleta_alugada(id_ciclista): # integração aqui (pega a bicicleta aqui)
        aluguel = None
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
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                return aluguel
                
        return False
    
    @staticmethod
    def alugar_bicicleta(aluguel_dto): #integração aqui
       ciclista = None
       for ciclista in lista_ciclista:
           if ciclista.id == aluguel_dto.ciclista:
              if ciclista.aluguel is not None:
                  return None
              ciclista.aluguel = aluguel_dto
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
    
    @staticmethod #verificar aqui
    def devolver_bicicleta(id_ciclista,id_tranca): #integração aqui
       #ciclista = None
       id_tranca = 0 # será alterado pela integração
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
    