from services import CiclistaService

ciclista_lista = CiclistaService.CiclistaService.Ciclista

class CartaoService:

    @staticmethod
    def alterar_cartao(id_ciclista,cartao_dto):
        ciclista= None
        
        for ciclista in ciclista_lista: 
            if ciclista.id==id_ciclista:
               cartao = ciclista.cartao
               break
        if cartao is not None:
            cartao.nomeTitular = cartao_dto.nomeTitular
            cartao.numero = cartao_dto.numero
            cartao.validade = cartao_dto.validade
            cartao.cvv = cartao_dto.cvv
            
        return cartao
    
    @staticmethod
    def consultar_cartao(id_ciclista):
        cartao= None
        for ciclista in ciclista_lista: 
            if ciclista.id==id_ciclista:
               cartao = ciclista.cartao
               break
        return cartao
