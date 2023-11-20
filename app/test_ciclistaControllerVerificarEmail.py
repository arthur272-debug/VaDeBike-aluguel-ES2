import unittest
from flask import Flask
from controllers.CiclistaController import ciclistaBp
from unittest.mock import patch
from services import CiclistaService

class TestCiclistaRouteVerificacaoEmail(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(ciclistaBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_verificacao_email_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        email_valido = "teste@example.com"

        # Sobrescrever o método de consulta para retornar True (email existe)
        with patch.object(CiclistaService.CiclistaService, 'consultar_ciclista_email', return_value=True):
            # Chame a rota /ciclista/existeEmail/<email> com o método GET
            resposta = self.client.get(f'/ciclista/existeEmail/{email_valido}')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "True")

    def test_realizar_verificacao_email_falha(self):
        # Configurar dados fictícios para um teste de falha
        email_invalido = "email@invalido"

        # Sobrescrever o método de consulta para retornar False (email não existe)
        with patch.object(CiclistaService.CiclistaService, 'consultar_ciclista_email', return_value=False):
            # Chame a rota /ciclista/existeEmail/<email> com o método GET
            resposta = self.client.get(f'/ciclista/existeEmail/{email_invalido}')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "False")

    def test_realizar_verificacao_email_sem_parametro(self):
        # Chame a rota /ciclista/existeEmail/<email> sem fornecer o email como parâmetro
        resposta = self.client.get('/ciclista/existeEmail/emailinvalido')

        # Verifique se a resposta é 400 Bad Request
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(resposta.get_data(as_text=True), "Email não enviado como parâmetro")

if __name__ == '__main__':
    unittest.main()
