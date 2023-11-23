import unittest
from unittest.mock import MagicMock
from models import Ciclista
from services import AluguelService

class TestAlugarBicicleta(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.contador = 1
        ciclista = Ciclista.Ciclista(
            nome="Arthur",
            nascimento="27/03/2002",
            cpf="122323",
            passaporte=None,
            nacionalidade="Brasileiro",
            email="arthur.andre",
            urlFotoDocumento="https",
            id=self.contador,
            senha="12356",
            cadastro=None,
            cartao=None,
            aluguel=None
        )
        AluguelService.lista_ciclista.append(ciclista)

    def test_alugar_bicicleta_ciclista_nao_encontrado(self):
        # Configurar dados fictícios para um teste de falha
        aluguel_dto_invalido = MagicMock(
            ciclista=1000,
            trancaInicio=1234,
            bicicleta=1,
            horaInicio=0,
            trancaFim=0,
            horaFim=0,
            cobranca=0
        )

        # Chame a função alugar_bicicleta
        resultado = AluguelService.AluguelService.alugar_bicicleta(aluguel_dto_invalido)

        # Verifique se o resultado é None (ciclista não encontrado)
        self.assertIsNone(resultado)

    def test_alugar_bicicleta_sucesso(self):
         # Chame a função alugar_bicicleta
        aluguel_dto_valido = MagicMock(
            ciclista=self.contador,
            trancaInicio=1234,
            bicicleta=1,
            horaInicio=0,
            trancaFim=0,
            horaFim=0,
            cobranca=0
        )

        resultado = AluguelService.AluguelService.alugar_bicicleta(aluguel_dto_valido)

        # Verifique se o resultado é Não-nulo
        self.assertIsNotNone(resultado)

        # Verifique se as informações do aluguel foram atualizadas corretamente
        self.assertEqual(resultado.trancaInicio, aluguel_dto_valido.trancaInicio)
        self.assertEqual(resultado.bicicleta, 1)  # assumindo que len(alugueis_historico) + 1 é igual a 1
        self.assertEqual(resultado.horaInicio, 0)
        self.assertEqual(resultado.cobranca, 0)

    def test_alugar_bicicleta_sucesso_alugada(self):
        # Chame a função alugar_bicicleta
        aluguel_dto_valido = MagicMock(
            ciclista=1,
            trancaInicio=1234,
            bicicleta=1,
            horaInicio=0,
            trancaFim=0,
            horaFim=0,
            cobranca=0
        )

        # Chame a função alugar_bicicleta
        resultado = AluguelService.AluguelService.alugar_bicicleta(aluguel_dto_valido)

        # Verifique se o resultado é None (ciclista já está alugando)
        self.assertIsNone(resultado)

    
if __name__ == '__main__':
    unittest.main()
