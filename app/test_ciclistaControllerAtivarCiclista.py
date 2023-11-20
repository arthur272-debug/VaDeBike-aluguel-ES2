import unittest
from flask import Flask
from controllers.CiclistaController import ciclistaBp
from unittest.mock import MagicMock
from services import CiclistaService
from models.Ciclista import Nacionalidade, RespostaCadastro

class TestCiclistaRouteAtivacao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(ciclistaBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_ativacao_ciclista_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        ciclista_mock = MagicMock(email = "art.andre@gmail.com",nacionalidade = Nacionalidade.BRASILEIRA,nascimento="27/03/2022",nome="Tutu",senha="1234567",cpf="123456",numero="1235767",validade="23/09",pais="Brasil",urlFotoDocumento="http://192.168.1.5",cadastro=RespostaCadastro.CONFIRMACAO,id=1)

        # Sobrescrever o método de consulta para retornar dados fictícios
        CiclistaService.CiclistaService.consultar_ciclista = lambda ciclista_id: ciclista_mock

        # Chame a rota /ciclista/<ciclista_id>/ativar com o método POST
        resposta = self.client.post('/ciclista/1/ativar')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["id"], ciclista_mock.id)
        self.assertEqual(dados_resposta["status"], ciclista_mock.cadastro.value)  # Considerando que "ATIVO" é o valor esperado

    def test_realizar_ativacao_ciclista_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar None (ciclista não encontrado)
        CiclistaService.CiclistaService.consultar_ciclista = lambda ciclista_id: None

        # Chame a rota /ciclista/<ciclista_id>/ativar com o método POST
        resposta = self.client.post('/ciclista/999/ativar')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

    def test_realizar_ativacao_ciclista_invalido(self):
        # Configurar dados fictícios para um teste de ativação inválida
        ciclista_mock = MagicMock(email = "art.andre@gmail.com",nacionalidade = Nacionalidade.BRASILEIRA,nascimento="27/03/2022",nome="Tutu",senha="1234567",cpf="123456",numero="1235767",validade="23/09",pais="Brasil",urlFotoDocumento="http://192.168.1.5",cadastro=RespostaCadastro.ATIVO,id=1)


        # Sobrescrever o método de consulta para retornar dados fictícios
        CiclistaService.CiclistaService.consultar_ciclista = lambda ciclista_id: ciclista_mock

        # Chame a rota /ciclista/<ciclista_id>/ativar com o método POST
        resposta = self.client.post('/ciclista/1/ativar')

        # Verifique se a resposta é 422 Unprocessable Entity
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()
