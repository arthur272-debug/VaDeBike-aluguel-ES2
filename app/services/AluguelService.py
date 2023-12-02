from services import CiclistaService
from models import Aluguel
from datetime import datetime

lista_ciclista = CiclistaService.CiclistaService.Ciclista
lista_tranca = []  # colocar a lista de trancas
alugueis_historico = []


class AluguelService:

    @staticmethod
    # integração aqui (pega a bicicleta aqui)
    def verificar_bicicleta_alugada(id_ciclista):
        aluguel = None
        ciclista = None
        for ciclista in lista_ciclista:
            if ciclista.id == id_ciclista:
                aluguel = ciclista.aluguel
                break
            ciclista = None

        if ciclista is None:
            return False

        # pega a informação de outro microsserviço
        # bicicleta = Bicicleta_fake.bicicleta(
         #   ciclista.aluguel.bicicleta, "boa", "3235", "2022", 100, "normal")
        aluguel = None  # mudar aqui
        if (aluguel is not None):
            return None  # bicicleta
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

        return ciclista == False

    @staticmethod
    def alugar_bicicleta(aluguel_dto):
        ciclista = None
        tranca = None
        for tranca in lista_tranca:  # pegar a lista de tranca
            if tranca == aluguel_dto.trancaInicio:
                break

        if tranca is None:
            return "ErroTranca"

        # verifica se tem bicicleta na tranca(integração) -- exceção aqui
        # return  "BicicletaNaoExiste"
        bicicleta = 0  # pega a bicicleta através do número da tranca

        if (bicicleta.status.value == "em reparo"):
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

    @staticmethod
    def enviar_administradora_cartao(cobranca, cartao):

        # chama o endpoint de externos
        # faz um if de lógica sobre o endpoint
        # registra na fila de cobranca, caso o pagamento não for aprovado
        return True

    @staticmethod
    def enviar_email_ciclista(email):
        # chama o endpoint de enviar email
        # faz a parte do if - tem
        return True
