import unittest
from unittest.mock import MagicMock
from services import AluguelService


class TestVerificarBicicletaAlugada(unittest.TestCase):

    @unittest.skip("")
    def test_verificar_bicicleta_alugada_com_aluguel(self):
        # Configurar dados fictícios para um teste bem-sucedido
        id_ciclista = 1

        # Chame a função verificar_bicicleta_alugada
        resultado = AluguelService.AluguelService.verificar_bicicleta_alugada(
            id_ciclista)

        # Verifique se o resultado é Não-nulo
        self.assertIsNotNone(resultado)

    def test_verificar_bicicleta_alugada_sem_aluguel(self):
        # Configurar dados fictícios para um teste de falha
        id_ciclista_invalido = 999

        # Chame a função verificar_bicicleta_alugada
        resultado = AluguelService.AluguelService.verificar_bicicleta_alugada(
            id_ciclista_invalido)

        # Verifique se o resultado é None (ciclista não encontrado)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
