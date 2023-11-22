import unittest
from flask import Flask
from controllers.CiclistaController import ciclistaBp
from models.Ciclista import Nacionalidade, RespostaCadastro

class TestCiclistaControllerCadastro(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(ciclistaBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_cadastro_sucesso(self):
        # Dados válidos para um teste bem-sucedido
        dados_validos = {"nome": "NomeCiclista","nascimento": "01/01/2000","cpf": "12345678901","numero": "Passaporte123","validade": "10/10/2030","pais": "Brasil","nacionalidade": "Brasileira","email": "ciclista@example.com","urlFotoDocumento": "https://example.com/foto","senha": "senha123"}

        # Chame a rota /ciclista com o método POST
        resposta = self.client.post('/ciclista', json=dados_validos)

        # Verifique se a resposta é 201 Created
        self.assertEqual(resposta.status_code, 201)
        
        # Verifique se a resposta contém os dados esperados
        dados_resposta = resposta.get_json()
        self.assertEqual(dados_resposta['status'], RespostaCadastro.CONFIRMACAO.value)

    def test_realizar_cadastro_falha(self):
        # Dados inválidos para um teste de falha
        # Aqui a nacionalidade é diferente do padrão
        dados_invalidos = {"nome": "NomeCiclista","nascimento": "01/01/2000","cpf": "12345678901","numero": "Passaporte123","validade": "10/10/2030","pais": "Brasil","nacionalidade": "Americana","email": "ciclista@example.com","urlFotoDocumento": "https://example.com/foto","senha": "senha456"} 

        # Chame a rota /ciclista com o método POST
        resposta = self.client.post('/ciclista', json=dados_invalidos)

        # Verifique se a resposta é 422 Unprocessable Entity
        self.assertEqual(resposta.status_code, 422)

if __name__ == '__main__':
    unittest.main()
