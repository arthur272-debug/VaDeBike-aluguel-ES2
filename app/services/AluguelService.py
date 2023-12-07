from services import CiclistaService
from models import Aluguel
from datetime import datetime
import requests

lista_ciclista = CiclistaService.CiclistaService.Ciclista
# lista_tranca = []  # colocar a lista de trancas
alugueis_historico = []


class AluguelService:

    @staticmethod
    # integração aqui
    def verificar_bicicleta_alugada(id_ciclista):  # verificar aqui depois
        aluguel = None
        ciclista = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                break
            ciclista = None

        if ciclista is None:
            return False

        id_bicicleta = ciclista.aluguel.bicicleta
        bicicleta = requests.get(
            url=f'https://va-de-bike-equipamentos-hbkxpua2za-uc.a.run.app/bicicleta/{id_bicicleta}')
        if bicicleta.status_code == 404:
            return None
        else:
            return bicicleta.json

    @staticmethod
    def verificar_ciclista_aluguel(id_ciclista):
        aluguel = None
        ciclista = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                return aluguel

        return ciclista == False

    @staticmethod
    def alugar_bicicleta(aluguel_dto):
        ciclista = None
        tranca = None

        if tranca is None:
            return "ErroTranca"
        id_bicicleta = aluguel_dto.bicicleta
        bicicleta = requests.get(
            url=f'https://va-de-bike-equipamentos-hbkxpua2za-uc.a.run.app/bicicleta/{id_bicicleta}')
        dados_bicicleta = bicicleta.json()
        status_bicicleta = dados_bicicleta.get('status')
        if (status_bicicleta == "em reparo"):
            return "BicicletaReparo"

        # usar o método de aluguel e da bicicleta
        for ciclista in lista_ciclista:
            if (ciclista.id == aluguel_dto.ciclista) and (ciclista.cadastro.value == "ATIVO"):
                # verificar no debug
                if AluguelService.verificar_ciclista_aluguel(ciclista.id):
                    aluguel = Aluguel.Aluguel(aluguel_dto.ciclista, aluguel_dto.trancaInicio, bicicleta,
                                              aluguel_dto.horaInicio, aluguel_dto.trancaFim, aluguel_dto.horaFim, aluguel_dto.cobranca, aluguel_dto.cartao)
                    ciclista.aluguel = aluguel
                    break
            ciclista = None

        if ciclista is None:
            return ciclista

        # realizacao da cobranca
        ciclista.aluguel.cobranca = 10

        administradora = AluguelService.enviar_administradora_cartao(
            ciclista.aluguel.cobranca, ciclista.cartao)
        if administradora == False:
            return "PagamentoNaoFeito"

        # registra os dados do aluguel
        hora_atual = datetime.now()  # pega a hora atual
        hora_int = hora_atual.hour
        ciclista.aluguel.horaInicio = hora_int
        aluguel.cartao = ciclista.cartao
        # bicicleta.status = muda o status da bicicleta - endpoint aqui
        # altera o status da tranca para "livre"

        email_enviado = AluguelService.enviar_email_ciclista(ciclista.email)
        return ciclista.aluguel

    @staticmethod
    def devolver_bicicleta(id_ciclista, id_tranca):  # integração aqui
        aluguel = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                break

        if aluguel is None:
            return aluguel

        # pega as informações dos outros microsserviços
        aluguel.trancaFim = 0
        aluguel.horaFim = 0
        aluguel.cobranca = 0 + 30

        # informações do aluguel e pagamento serão repassadas para seus microsserviços respectivos
        alugueis_historico.append(aluguel)
        ciclista.aluguel = None
        return aluguel

    # métodos da integração - vai ter os endpoints aqui??? -  do mesmo formato que os do Controller?
