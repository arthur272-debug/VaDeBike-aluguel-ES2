import unittest
from flask import Flask
from controllers.CiclistaController import ciclistaBp
from unittest.mock import MagicMock
from services import CiclistaService
from models.Ciclista import Nacionalidade, RespostaCadastro

class TestCiclistaRouteBusca(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(ciclistaBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_busca_ciclista_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        
        ciclista_mock = MagicMock(email = "art.andre@gmail.com",nacionalidade = Nacionalidade.BRASILEIRA,nascimento="27/03/2022",nome="Tutu",senha="1234567",cpf="123456",numero="1235767",validade="23/09",pais="Brasil",urlFotoDocumento="endereco.url",cadastro=RespostaCadastro.ATIVO,id=1)

        # Sobrescrever o método de consulta para retornar dados fictícios
        CiclistaService.CiclistaService.consultar_ciclista = lambda ciclista_id: ciclista_mock

        # Chame a rota /ciclista/<ciclista_id> com o método GET
        resposta = self.client.get('/ciclista/1')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["id"], ciclista_mock.id)
        print(dados_resposta["status"])
        print(ciclista_mock.cadastro)
        print('dfdfdf')
        self.assertEqual(dados_resposta["status"], ciclista_mock.cadastro.value)

    def test_realizar_busca_ciclista_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar None (ciclista não encontrado)
        CiclistaService.CiclistaService.consultar_ciclista = lambda ciclista_id: None

        # Chame a rota /ciclista/<ciclista_id> com o método GET
        resposta = self.client.get('/ciclista/999')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()
