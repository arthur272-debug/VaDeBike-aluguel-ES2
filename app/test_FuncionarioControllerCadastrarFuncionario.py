import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from controllers.FuncionarioController import funcionarioBp

class TestFuncionarioRoute(unittest.TestCase):

    def setUp(self):
        
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_cadastro_sucesso(self):
        
        dados_validos = {
            "senha": "senha123",
            "confirmação_senha": "senha123",
            "cpf": "12345678900",
            "email": "teste@example.com",
            "documento": "documento123",
            "funcao": "Desenvolvedor",
            "idade": 25,
            "nome": "Nome Teste"
        }

        
        resposta = self.client.post('/funcionario', json=dados_validos)

        
        self.assertEqual(resposta.status_code, 200)
        dados_resposta = resposta.get_json()
        self.assertEqual(dados_resposta["senha"], dados_validos["senha"])
        self.assertEqual(dados_resposta["email"], dados_validos["email"])
        

    def test_realizar_cadastro_falha(self):
       
        dados_invalidos = {
            "senha": "senha123",
            "confirmação_senha": "senha456",  # Aqui a confirmação é diferente da senha
            "cpf": "12345678900",
            "email": "teste@example.com",
            "documento": "documento123",
            "funcao": "Desenvolvedor",
            "idade": "25",  # Aqui a idade não é um inteiro
            "nome": "Nome Teste"
        }

        
        resposta = self.client.post('/funcionario', json=dados_invalidos)

        
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()