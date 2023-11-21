from services import CiclistaService

lista_ciclista = CiclistaService.CiclistaService.Ciclista

alugueis_historico = []

class AluguelService:

# usado também para ver se o ciclista tem bicicleta alugada ou não
    @staticmethod
    def verificar_ciclista_aluguel(id_ciclista): 
        ciclista = None
        aluguel = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                break
        return aluguel
    
    @staticmethod
    def alugar_bicicleta(id_ciclista,aluguel_dto): #integração aqui
       ciclista = None
       aluguel = None
       for ciclista in lista_ciclista:
           if ciclista.id == id_ciclista:
              aluguel = ciclista.aluguel
              break
        
       if aluguel is None:
          return aluguel
       
       # pega as informações dos outros microsserviços
       aluguel.ciclista = id_ciclista
       aluguel.trancaInicio = aluguel_dto.trancaInicio
       aluguel.bicicleta = len(alugueis_historico)+1 # muda -- fake
       aluguel.horaInicio = 0
       aluguel.cobranca = 0  
      
       return aluguel
    
    @staticmethod #verificar aqui
    def devolver_bicicleta(id_ciclista,id_tranca): #integração aqui
       ciclista = None
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

       # informações do aluguel e pagamento serão repassadas para seus microsserviços responsáveis
       alugueis_historico.append(aluguel)
       ciclista.aluguel = None
       return aluguel
    