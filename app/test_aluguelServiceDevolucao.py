import unittest  #talvez será alterado
from unittest.mock import MagicMock
from models import Ciclista, Bicicleta_fake
from services import AluguelService

class TestDevolverBicicleta(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes

        self.contador = +1
        aluguel_exemplo = MagicMock(ciclista=self.contador,trancaInicio=1234,bicicleta=1,horaInicio=0,trancaFim=0,horaFim=0,cobranca=0)

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
            aluguel=aluguel_exemplo
        )
        AluguelService.lista_ciclista.append(ciclista)

    def test_devolver_bicicleta_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        
        aluguel_exemplo2 = MagicMock(ciclista=self.contador,trancaInicio=1234567,bicicleta=1,horaInicio=65,trancaFim=80,horaFim=70,cobranca=10)

        ciclista = Ciclista.Ciclista(
            nome="Arthur",
            nascimento="27/03/2002",
            cpf="122323",
            passaporte=None,
            nacionalidade="Brasileiro",
            email="arthur.andre",
            urlFotoDocumento="https",
            id=4,
            senha="12356",
            cadastro=None,
            cartao=None,
            aluguel=aluguel_exemplo2
        )
        AluguelService.lista_ciclista.append(ciclista)

        # Chame a função devolver_bicicleta com os dados fictícios
        resultado = AluguelService.AluguelService.devolver_bicicleta(4, 1233)

        # Verifique se o resultado é não nulo
        self.assertIsNotNone(resultado)

        # Verifique se as informações do aluguel foram atualizadas corretamente
        self.assertEqual(resultado.trancaFim, 0)
        self.assertEqual(resultado.horaFim, 0)
        self.assertEqual(resultado.cobranca, 30)  

        # Verifique se o aluguel foi adicionado à lista de histórico
        self.assertIn(resultado, AluguelService.alugueis_historico)

        # Verifique se o ciclista não está mais alugando
        self.assertIsNone(ciclista.aluguel)

    def test_devolver_bicicleta_ciclista_nao_encontrado(self):
        # Configurar dados fictícios para um teste onde o ciclista não é encontrado
        id_ciclista = 999
        id_tranca = 1234

        # Sobrescrever o método de verificar_bicicleta_alugada para retornar None
        AluguelService.AluguelService.verificar_bicicleta_alugada = lambda id_ciclista: None

        # Chame a função devolver_bicicleta com os dados fictícios
        resultado = AluguelService.AluguelService.devolver_bicicleta(id_ciclista, id_tranca)

        # Verifique se o resultado é None (ciclista não encontrado)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
