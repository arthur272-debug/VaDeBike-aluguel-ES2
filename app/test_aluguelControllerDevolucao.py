import unittest
from flask import Flask
from controllers.AluguelController import aluguelBp
from unittest.mock import MagicMock
from services import AluguelService

class TestAluguelRouteRealizarDevolucao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(aluguelBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.config['WTF_CSRF_ENABLED'] = False

    def test_realizar_devolucao_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        devolucao_mock = MagicMock(
            bicicleta="Bicicleta1",
            horaInicio="10:00",
            trancaFim="TrancaFim1",
            horaFim="12:00",
            cobranca=50.0,
            ciclista="Ciclista1",
            trancaInicio="TrancaInicio1"
        )

        # Sobrescrever o método de devolucao para retornar dados fictícios
        AluguelService.AluguelService.devolver_bicicleta = lambda idBicicleta, idTranca: devolucao_mock

        # Chame a rota /devolucao com o método POST
        resposta = self.client.post('/devolucao', json={"idBicicleta": 1, "idTranca": 1})

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["cobranca"], devolucao_mock.cobranca)
        self.assertEqual(dados_resposta["ciclista"], devolucao_mock.ciclista)
        self.assertEqual(dados_resposta["trancaInicio"], devolucao_mock.trancaInicio)
        self.assertEqual(dados_resposta["bicicleta"], devolucao_mock.bicicleta)
        self.assertEqual(dados_resposta["horaInicio"], devolucao_mock.horaInicio)
        self.assertEqual(dados_resposta["trancaFim"], devolucao_mock.trancaFim)
        self.assertEqual(dados_resposta["horaFim"], devolucao_mock.horaFim)

    def test_realizar_devolucao_invalido(self):
        # Sobrescrever o método de devolucao para retornar None (devolucao inválida)
        AluguelService.AluguelService.devolver_bicicleta = lambda idBicicleta, idTranca: None

        # Chame a rota /devolucao com o método POST
        resposta = self.client.post('/devolucao', json={"idBicicleta": 1, "idTranca": 1})

        # Verifique se a resposta é 422 Unprocessable Entity
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()
