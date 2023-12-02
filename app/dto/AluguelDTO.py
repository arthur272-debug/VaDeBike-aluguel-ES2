class AluguelDto:

    def __init__(self, ciclista: int, trancaInicio: int, bicicleta: int, horaInicio: int, trancaFim: int, horaFim: int, cobranca: int, cartao: object):
        self.ciclista = ciclista
        self.trancaInicio = trancaInicio
        self.bicicleta = bicicleta
        self.horaInicio = horaInicio
        self.trancaFim = trancaFim
        self.horaFim = horaFim
        self.cobranca = cobranca
        self.cartao = cartao
