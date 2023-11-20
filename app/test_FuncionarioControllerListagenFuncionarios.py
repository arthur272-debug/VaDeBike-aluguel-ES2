import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from controllers.FuncionarioController import funcionarioBp
from unittest.mock import patch, MagicMock

class TestFuncionarioRouteListagem(unittest.TestCase):

    def setUp(self):
        
        self.app = Flask(__name__)
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    @patch('services.FuncionarioService.FuncionarioService.consultar_lista_funcionario')
    def test_realizar_listagem_funcionarios_sucesso(self, mock_consultar_lista_funcionario):
        # Configurar dados fictícios para um teste bem-sucedido
        funcionarios_mock = [
            MagicMock(senha='1234',cpf='123456789',email='arthur.andre@gmail.com',documento='cpf',funcao='analista de segurança',idade = 21,nome="Nome1",id=1),
            MagicMock(senha='1234566',cpf='1234567891011',email='arthur.andre235@gmail.com',documento='rg',funcao='analista de T.i',idade = 26,nome="Nome12",id=2),
        
            
        ]

        # Configurar o retorno do mock
        mock_consultar_lista_funcionario.return_value = funcionarios_mock

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, list)
        self.assertEqual(len(dados_resposta), len(funcionarios_mock))
        

    @patch('services.FuncionarioService.FuncionarioService.consultar_lista_funcionario')
    def test_realizar_listagem_funcionarios_nao_encontrado(self, mock_consultar_lista_funcionario):
        # Configurar o retorno do mock para uma lista vazia
        mock_consultar_lista_funcionario.return_value = []

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()