import unittest
from flask import Flask
from controllers.CiclistaController import ciclistaBp
from unittest.mock import MagicMock
from services import CiclistaService
from models.Ciclista import Nacionalidade, RespostaCadastro

class TestCiclistaRouteAtualizacao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(ciclistaBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_atualizacao_ciclista_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        ciclista_mock = MagicMock(email = "art.andre@gmail.com",nacionalidade = Nacionalidade.BRASILEIRA,nascimento="27/03/2022",nome="Tutu",senha="1234567",cpf="123456",numero="1235767",validade="23/09",pais="Brasil",urlFotoDocumento="http://192.168.1.5",cadastro=RespostaCadastro.ATIVO,id=1)

        # Sobrescrever o método de atualização para retornar dados fictícios
        CiclistaService.CiclistaService.atualizar_ciclista = lambda ciclista_id, ciclista_dto: ciclista_mock

        # Chame a rota /ciclista/<ciclista_id> com o método PUT
        dados_atualizacao_validos = {
            "nome": "Novo Nome",
            "nascimento": "01/01/2000",
            "cpf": "98765432100",
            "nacionalidade": "Brasileira",
            "numero": "123456789",
            "validade": "01/01/2023",
            "pais": "Brasil",
            "email": "novo_email@example.com",
            "urlFotoDocumento": "nova_url",
            "senha": "nova_senha"
        }
        resposta = self.client.put('/ciclista/1', json=dados_atualizacao_validos)

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["id"], ciclista_mock.id)
        self.assertEqual(dados_resposta["status"], ciclista_mock.cadastro.value)

    def test_realizar_atualizacao_ciclista_nao_encontrado(self):
        # Sobrescrever o método de atualização para retornar None (ciclista não encontrado)
        CiclistaService.CiclistaService.atualizar_ciclista = lambda ciclista_id, ciclista_dto: None

        # Chame a rota /ciclista/<ciclista_id> com o método PUT
        dados_atualizacao_invalidos = {
            "nome": "Novo Nome",
            "nascimento": "01/01/2000",
            "cpf": "98765432100",
            "nacionalidade": "Brasileira",
            "numero": "123456789",
            "validade": "01/01/2023",
            "pais": "Brasil",
            "email": "novo_email@example.com",
            "urlFotoDocumento": "nova_url",
            "senha": "nova_senha"
        }
        resposta = self.client.put('/ciclista/999', json=dados_atualizacao_invalidos)

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()