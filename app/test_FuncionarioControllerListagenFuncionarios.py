import unittest
from flask import Flask
from services import FuncionarioService
from controllers.FuncionarioController import funcionarioBp
from unittest.mock import MagicMock

FuncionarioService.FuncionarioService.funcionarios.clear


class TestFuncionarioRouteListagem(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_listagem_funcionarios_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido

        funcionario_mock1 = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com",
                                      documento="cpf", funcao="analista de segurança", idade=21, nome="Nome1", id=1)
        funcionario_mock2 = MagicMock(senha="123456", cpf="12345678910", email="arthur.andre@gmailfdfdf.com",
                                      documento="rg", funcao="analista de T.I,", idade=27, nome="Nome3", id=2)

        funcionarios_mock = [funcionario_mock1, funcionario_mock2]

        # Sobrescrever o método de consulta para retornar dados fictícios
        FuncionarioService.FuncionarioService.consultar_lista_funcionario = lambda: funcionarios_mock

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, list)
        self.assertEqual(len(dados_resposta), len(funcionarios_mock))

    def test_realizar_listagem_funcionarios_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar uma lista vazia
        FuncionarioService.FuncionarioService.consultar_lista_funcionario = lambda: []

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)


if __name__ == '__main__':
    unittest.main()
