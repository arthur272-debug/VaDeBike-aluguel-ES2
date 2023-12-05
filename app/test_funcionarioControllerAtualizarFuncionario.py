import unittest
from flask import Flask
from controllers.FuncionarioController import funcionarioBp
from services import FuncionarioService
from unittest.mock import MagicMock


class TestFuncionarioRouteAtualizacao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        FuncionarioService.FuncionarioService.funcionarios.clear
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_atualizacao_funcionario_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        funcionario_mock = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com",
                                     documento="cpf", funcao="analista de segurança", idade=21, nome="Nome1", id=1)

        # Sobrescrever o método de atualização para retornar dados fictícios
        FuncionarioService.FuncionarioService.atualizar_funcionario = lambda funcionario_id, funcionario_dto: funcionario_mock

        # Dados fictícios para a atualização
        dados_atualizacao = {
            "senha": "senha123",
            "confirmação_senha": "senha123",
            "cpf": "12345678900",
            "email": "teste@.com",
            "documento": "documento123",
            "funcao": "Desenvolvedor",
            "idade": 25,
            "nome": "Nome Teste"
        }

        # Chame a rota /funcionario/<funcionario_id> com o método PUT e dados válidos
        resposta = self.client.put('/funcionario/1', json=dados_atualizacao)

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, dict)
        self.assertEqual(dados_resposta["senha"], funcionario_mock.senha)
        self.assertEqual(dados_resposta["cpf"], funcionario_mock.cpf)
        self.assertEqual(dados_resposta["email"], funcionario_mock.email)
        self.assertEqual(dados_resposta["id"], funcionario_mock.id)
        self.assertEqual(dados_resposta["funcao"], funcionario_mock.funcao)
        self.assertEqual(dados_resposta["idade"], funcionario_mock.idade)
        self.assertEqual(dados_resposta["nome"], funcionario_mock.nome)

    @unittest.skip("")
    def test_realizar_atualizacao_funcionario_nao_encontrado(self):
        # Sobrescrever o método de atualização para retornar None (funcionário não encontrado)
        FuncionarioService.atualizar_funcionario = lambda funcionario_id, funcionario_dto: None

        # Dados fictícios para a atualização
        dados_atualizacao = {
            "senha": "senha123",
            "confirmação_senha": "senha123",
            "cpf": "12345678900",
            "email": "teste@example.com",
            "documento": "documento123",
            "funcao": "Desenvolvedor",
            "idade": 25,
            "nome": "Tutu"
        }

        # Chame a rota /funcionario/<funcionario_id> com o método PUT e dados válidos
        resposta = self.client.put('/funcionario/999', json=dados_atualizacao)

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

    def test_realizar_atualizacao_funcionario_invalido(self):

        # Dados fictícios para a atualização com ID inválido (não inteiro)
        dados_atualizacao_invalido = {
            "senha": "senha123",
            "confirmação_senha": "senha123",
            "cpf": "12345678900",
            "email": "teste@example.com",
            "documento": "documento123",
            "funcao": "Desenvolvedor",
            "idade": "25",
            "nome": "Arthur"
        }

        # Chame a rota /funcionario/<funcionario_id> com o método PUT e dados inválidos
        resposta = self.client.put(
            '/funcionario/1', json=dados_atualizacao_invalido)

        # Verifique se a resposta é 422 Unprocessable Entity (dados inválidos)
        self.assertEqual(resposta.status_code, 422)


if __name__ == '__main__':
    unittest.main()
