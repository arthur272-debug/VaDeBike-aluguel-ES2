import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from controllers.CartaoController import cartaoBp
from unittest.mock import MagicMock
from services import CartaoService

class TestCartaoRouteAtualizacao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(cartaoBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_atualizacao_cartao_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        cartao_mock = MagicMock(nomeTitular="Titular Antigo",numero="1234567890123456",validade="12-23",cvv="123",id=1)

        # Sobrescrever o método de consulta para retornar dados fictícios
        CartaoService.CartaoService.alterar_cartao = lambda ciclista_id, cartao_dto: cartao_mock

        # Chame a rota /cartaoDeCredito/<ciclista_id> com o método PUT
        dados_atualizados = {
            "nomeTitular": "Arthur Andre",
            "numero": "1111222233334444",
            "validade": "01-25",
            "cvv": "456"
        }
        resposta = self.client.put('/cartaoDeCredito/1', json=dados_atualizados)

        # Verifique se a resposta é 200 OK
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "Dados atualizados")

    def test_realizar_atualizacao_cartao_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar None (cartão não encontrado)
        CartaoService.CartaoService.alterar_cartao = lambda ciclista_id, cartao_dto: None

        # Chame a rota /cartaoDeCredito/<ciclista_id> com o método PUT
        dados_atualizados = {
            "nomeTitular": "Tutu",
            "numero": "1111222233334444",
            "validade": "01-25",
            "cvv": "456"
        }
        resposta = self.client.put('/cartaoDeCredito/999', json=dados_atualizados)

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

    def test_realizar_atualizacao_cartao_invalido(self):
        # Configurar dados fictícios para um teste de atualização inválida (validade sem '-')
        cartao_mock = MagicMock(
            nomeTitular="Titular Antigo",
            numero="1234567890123456",
            validade="12-23",
            cvv="123",
            id=1
        )

        # Sobrescrever o método de consulta para retornar dados fictícios
        CartaoService.CartaoService.alterar_cartao = lambda ciclista_id, cartao_dto: cartao_mock

        # Chame a rota /cartaoDeCredito/<ciclista_id> com o método PUT
        dados_atualizados = {
            "nomeTitular": "Titular Novo",
            "numero": "1111222233334444",
            "validade": "0125",  # Validade sem '-'
            "cvv": "456"
        }
        resposta = self.client.put('/cartaoDeCredito/1', json=dados_atualizados)

        # Verifique se a resposta é 422 Unprocessable Entity
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()
