import unittest
from flask import Flask
from controllers.FuncionarioController import funcionarioBp
from services import FuncionarioService
from unittest.mock import MagicMock


class TestFuncionarioRouteBusca(unittest.TestCase):

    def setUp(self):
        FuncionarioService.FuncionarioService.funcionarios.clear
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_busca_funcionario_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        funcionario_mock = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com",
                                     documento="cpf", funcao="analista de segurança", idade=21, nome="Nome1", id=1)

        # Sobrescrever o método de consulta para retornar dados fictícios
        FuncionarioService.FuncionarioService.consultar_funcionario = lambda funcionario_id: funcionario_mock

        # Chame a rota /funcionario/<funcionario_id> com o método GET
        resposta = self.client.get('/funcionario/1')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["idade"], funcionario_mock.idade)
        self.assertEqual(dados_resposta["nome"], funcionario_mock.nome)
        self.assertEqual(dados_resposta["id"], funcionario_mock.id)
        self.assertEqual(dados_resposta["cpf"], funcionario_mock.cpf)
        self.assertEqual(dados_resposta["email"], funcionario_mock.email)
        self.assertEqual(dados_resposta["funcao"], funcionario_mock.funcao)
        self.assertEqual(dados_resposta["senha"], funcionario_mock.senha)

    def test_realizar_busca_funcionario_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar None (funcionário não encontrado)
        FuncionarioService.FuncionarioService.consultar_funcionario = lambda funcionario_id: None

        # Chame a rota /funcionario/<funcionario_id> com o método GET
        resposta = self.client.get('/funcionario/999')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)


if __name__ == '__main__':
    unittest.main()
