import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from controllers.CartaoController import cartaoBp
from unittest.mock import MagicMock
from services import CartaoService

class TestCartaoRouteConsulta(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(cartaoBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_consulta_cartao_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        cartao_mock = MagicMock(id=1,nomeTitular="Titular Teste",numero="1234567890123456",validade="12/23",cvv="123")

        # Sobrescrever o método de consulta para retornar dados fictícios
        CartaoService.CartaoService.consultar_cartao = lambda ciclista_id: cartao_mock

        # Chame a rota /cartaoDeCredito/<ciclista_id> com o método GET
        resposta = self.client.get('/cartaoDeCredito/1')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["id"], cartao_mock.id)
        self.assertEqual(dados_resposta["nomeTitular"], cartao_mock.nomeTitular)
        self.assertEqual(dados_resposta["numero"], cartao_mock.numero)
        self.assertEqual(dados_resposta["validade"], cartao_mock.validade)
        self.assertEqual(dados_resposta["cvv"], cartao_mock.cvv)

    def test_realizar_consulta_cartao_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar None (cartão não encontrado)
        CartaoService.CartaoService.consultar_cartao = lambda ciclista_id: None

        # Chame a rota /cartaoDeCredito/<ciclista_id> com o método GET
        resposta = self.client.get('/cartaoDeCredito/999')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()
