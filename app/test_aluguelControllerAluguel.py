import unittest
from flask import Flask
from controllers.AluguelController import aluguelBp
from unittest.mock import MagicMock
from services import AluguelService

class TestAluguelRouteRealizarAluguel(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(aluguelBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.config['WTF_CSRF_ENABLED'] = False

    def test_realizar_aluguel_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        aluguel_mock = MagicMock(
            bicicleta="Bicicleta1",
            horaInicio="10:00",
            trancaFim="TrancaFim1",
            horaFim="12:00",
            cobranca=50.0,
            ciclista="Ciclista1",
            trancaInicio="TrancaInicio1"
        )

        # Sobrescrever o método de aluguel para retornar dados fictícios
        AluguelService.AluguelService.alugar_bicicleta = lambda aluguel_dto: aluguel_mock

        # Chame a rota /aluguel com o método POST
        resposta = self.client.post('/aluguel', json={"ciclista": "Ciclista1", "trancaInicio": "TrancaInicio1"})

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["bicicleta"], aluguel_mock.bicicleta)
        self.assertEqual(dados_resposta["horaInicio"], aluguel_mock.horaInicio)
        self.assertEqual(dados_resposta["trancaFim"], aluguel_mock.trancaFim)
        self.assertEqual(dados_resposta["horaFim"], aluguel_mock.horaFim)
        self.assertEqual(dados_resposta["cobranca"], aluguel_mock.cobranca)
        self.assertEqual(dados_resposta["ciclista"], aluguel_mock.ciclista)
        self.assertEqual(dados_resposta["trancaInicio"], aluguel_mock.trancaInicio)

    def test_realizar_aluguel_invalido(self):
        # Sobrescrever o método de aluguel para retornar None (aluguel inválido)
        AluguelService.AluguelService.alugar_bicicleta = lambda aluguel_dto: None

        # Chame a rota /aluguel com o método POST
        resposta = self.client.post('/aluguel', json={"ciclista": "Ciclista1", "trancaInicio": "TrancaInicio1"})

        # Verifique se a resposta é 422 Unprocessable Entity
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()
