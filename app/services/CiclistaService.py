from models import Ciclista
from services import CartaoService
import requests


class CiclistaService:

    Ciclista = []
    Confirmacao = []

    @staticmethod
    def cadastrar_ciclista(ciclista_dto):  # integração aqui - feita
        idCiclista = len(CiclistaService.Ciclista)+1
        ciclista_dto.id = idCiclista
        email_valido = CiclistaService.confirmar_email(ciclista_dto.email)
        if email_valido == True or '@' not in ciclista_dto.email:
            return "EmailInvalido"

        ciclista = Ciclista.Ciclista(ciclista_dto.nome, ciclista_dto.nascimento, ciclista_dto.cpf, ciclista_dto.passaporte, ciclista_dto.nacionalidade,
                                     email_valido, ciclista_dto.urlFotoDocumento, ciclista_dto.id, ciclista_dto.senha, ciclista_dto.cadastro, ciclista_dto.cartao, ciclista_dto.aluguel)
        CiclistaService.Ciclista.append(ciclista)
        return ciclista

    @staticmethod
    def consultar_ciclista(ciclista_id):
        for ciclista in CiclistaService.Ciclista:
            if ciclista.id == ciclista_id:
                return ciclista
        return None

    def consultar_ciclista_email(email):
        for ciclista_email in CiclistaService.Ciclista:
            if ciclista_email.email == email:
                return True
        return False

    @staticmethod
    def atualizar_ciclista(ciclista_id, ciclista_dto):  # integração aqui - feita
        ciclista = CiclistaService.consultar_ciclista(ciclista_id)
        cartao_valido = CartaoService.CartaoService.alterar_cartao(
            ciclista_id, ciclista_dto.cartao)

        if cartao_valido == "ErroCartao":
            return cartao_valido

        email_valido = CiclistaService.confirmar_email(ciclista_dto.email)
        if email_valido == True or '@' not in ciclista_dto.email:
            return "EmailInvalido"

        if ciclista is not None:
            ciclista_atualizado = Ciclista.Ciclista(ciclista_dto.nome, ciclista_dto.nascimento, ciclista_dto.cpf, ciclista_dto.passaporte, ciclista_dto.nacionalidade,
                                                    ciclista_dto.email, ciclista_dto.urlFotoDocumento, ciclista_dto.id, ciclista_dto.senha, ciclista_dto.cadastro, cartao_valido, ciclista_dto.aluguel)
            ciclista.nome = ciclista_atualizado.nome
            ciclista.nascimento = ciclista_atualizado.nascimento
            ciclista.cpf = ciclista_atualizado.cpf
            ciclista.passaporte = ciclista_atualizado.passaporte
            ciclista.nacionalidade = ciclista_atualizado.nacionalidade
            ciclista.email = ciclista_atualizado.email
            ciclista.urlFotoDocumento = ciclista_atualizado.urlFotoDocumento
            ciclista.senha = ciclista_atualizado.senha
            return ciclista
        return None

    @staticmethod
    def confirmar_email(ciclista_email):
        for ciclista in CiclistaService.Ciclista:
            if ciclista.email == ciclista_email:
                return True
        return False
