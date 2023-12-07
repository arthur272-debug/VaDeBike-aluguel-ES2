from services import CiclistaService
from models import Cartao
import requests


class CartaoService:

    @staticmethod  #
    def alterar_cartao(id_ciclista, cartao_dto):
        ciclista = None
        cartao = None

        cartao_validado = requests.post(
            url='https://microservice-externo-hbkxpua2za-uc.a.run.app/validaCartaoDeCredito', json={'nomeTitular': 'ciclista_dto[nomeTitular]', 'numero': 'ciclista_dto[numero]', 'validade': 'ciclista_dto[validade]', 'cvv': 'ciclista_dto[cvv]'})

        if cartao_validado.status_code == 422:
            return "ErroCartao"

        for ciclista in CiclistaService.CiclistaService.Ciclista:
            if ciclista.id == id_ciclista:
                cartao = ciclista.cartao
                break
        if cartao is not None:
            cartao_novo = Cartao.cartao(
                cartao_dto.nomeTitular, cartao_dto.numero, cartao_dto.validade, cartao_dto.cvv)

            cartao.nomeTitular = cartao_novo.nomeTitular
            cartao.numero = cartao_novo.numero
            cartao.validade = cartao_novo.validade
            cartao.cvv = cartao_novo.cvv

        return cartao

    @staticmethod
    def consultar_cartao(id_ciclista):
        cartao = None
        for ciclista in CiclistaService.CiclistaService.Ciclista:
            if ciclista.id == id_ciclista:
                cartao = ciclista.cartao
                break
        return cartao
