import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from services import FuncionarioService
from controllers.FuncionarioController import funcionarioBp
from dto import FuncionarioDTO

class TestFuncionarioRouteListagem(unittest.TestCase):

    def setUp(self):
        
        self.app = Flask(__name__)
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_listagem_funcionarios_sucesso(self):
        
        funcionarios_list = []
        funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        funcionario2 = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        funcionarios_list.append(funcionario)
        funcionarios_list.append(funcionario2)

        # Sobrescrever o método de consulta para retornar dados fictícios
        FuncionarioService.FuncionarioService.consultar_lista_funcionario = lambda: funcionarios_list

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 200 OK e se contém os dados esperados
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertIsInstance(dados_resposta, list)
        self.assertEqual(len(dados_resposta), len(funcionarios_list))
        # Adicione mais verificações conforme necessário

    def test_realizar_listagem_funcionarios_nao_encontrado(self):
        # Sobrescrever o método de consulta para retornar uma lista vazia
        FuncionarioService.FuncionarioService.consultar_lista_funcionario = lambda: []

        # Chame a rota /funcionario com o método GET
        resposta = self.client.get('/funcionario')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()