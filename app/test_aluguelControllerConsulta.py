import unittest
from flask import Flask
from controllers.AluguelController import aluguelBp
from services import AluguelService

class TestAluguelRouteConsultaPermiteAluguel(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(aluguelBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.config['WTF_CSRF_ENABLED'] = False

    def test_consulta_permite_aluguel_false(self):
        # Sobrescrever o método de verificação para retornar False
        AluguelService.AluguelService.verificar_ciclista_aluguel = lambda ciclista_id: 1

        # Chame a rota /ciclista/<ciclista_id>/permiteAluguel com o método GET
        resposta = self.client.get('/ciclista/1/permiteAluguel')

        # Verifique se a resposta é "False" e o status é 200 OK
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "False")

    def test_consulta_permite_aluguel_true(self):
        # Sobrescrever o método de verificação para retornar True
        AluguelService.AluguelService.verificar_ciclista_aluguel = lambda ciclista_id: None

        # Chame a rota /ciclista/<ciclista_id>/permiteAluguel com o método GET
        resposta = self.client.get('/ciclista/1/permiteAluguel')

        # Verifique se a resposta é "True" e o status é 200 OK
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "True")

    def test_consulta_permite_aluguel_nao_encontrado(self):
        # Sobrescrever o método de verificação para retornar None (ciclista não encontrado)
        AluguelService.AluguelService.verificar_ciclista_aluguel = lambda ciclista_id: False

        # Chame a rota /ciclista/<ciclista_id>/permiteAluguel com o método GET
        resposta = self.client.get('/ciclista/999/permiteAluguel')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()
