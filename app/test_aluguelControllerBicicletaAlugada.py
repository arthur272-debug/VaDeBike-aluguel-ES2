import unittest
from flask import Flask
from controllers.AluguelController import aluguelBp
from unittest.mock import MagicMock
from services import AluguelService

class TestAluguelRouteConsultaBicicletaAlugada(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(aluguelBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.config['WTF_CSRF_ENABLED'] = False

    def test_consulta_bicicleta_alugada_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        bicicleta_mock = MagicMock(id=1,marca="Marca1",modelo="Modelo1",ano=2022,status="Alugada")

        # Sobrescrever o método de verificação para retornar dados fictícios
        AluguelService.AluguelService.verificar_bicicleta_alugada = lambda ciclista_id: bicicleta_mock

        # Chame a rota /ciclista/<ciclista_id>/bicicletaAlugada com o método GET
        resposta = self.client.get('/ciclista/1/bicicletaAlugada')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["id"], bicicleta_mock.id)
        self.assertEqual(dados_resposta["marca"], bicicleta_mock.marca)
        self.assertEqual(dados_resposta["modelo"], bicicleta_mock.modelo)
        self.assertEqual(dados_resposta["ano"], bicicleta_mock.ano)
        self.assertEqual(dados_resposta["status"], bicicleta_mock.status)

    def test_consulta_bicicleta_alugada_nao_encontrado(self):
        # Sobrescrever o método de verificação para retornar False (bicicleta não encontrada)
        AluguelService.AluguelService.verificar_bicicleta_alugada = lambda ciclista_id: False

        # Chame a rota /ciclista/<ciclista_id>/bicicletaAlugada com o método GET
        resposta = self.client.get('/ciclista/1/bicicletaAlugada')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

    def test_consulta_bicicleta_alugada_vazio(self):
        # Sobrescrever o método de verificação para retornar None (sem bicicleta alugada)
        AluguelService.AluguelService.verificar_bicicleta_alugada = lambda ciclista_id: None

        # Chame a rota /ciclista/<ciclista_id>/bicicletaAlugada com o método GET
        resposta = self.client.get('/ciclista/1/bicicletaAlugada')

        # Verifique se a resposta é "Vazio" e o status é 200 OK
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "Vazio")

if __name__ == '__main__':
    unittest.main()
