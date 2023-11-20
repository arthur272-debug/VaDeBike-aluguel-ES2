import unittest
from flask import Flask
from controllers.FuncionarioController import funcionarioBp
from services import FuncionarioService
class TestFuncionarioRouteExclusao(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(funcionarioBp)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_realizar_exclusao_funcionario_sucesso(self):
        # Sobrescrever o método de exclusão para retornar True (exclusão bem-sucedida)
        FuncionarioService.FuncionarioService.deletar_funcionario = lambda funcionario_id: True

        # Chame a rota /funcionario/<funcionario_id> com o método DELETE
        resposta = self.client.delete('/funcionario/1')

        # Verifique se a resposta é 200 OK
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_data(as_text=True), "Dados removidos")

    def test_realizar_exclusao_funcionario_nao_encontrado(self):
        # Sobrescrever o método de exclusão para retornar False (funcionário não encontrado)
        FuncionarioService.FuncionarioService.deletar_funcionario = lambda funcionario_id: False

        # Chame a rota /funcionario/<funcionario_id> com o método DELETE
        resposta = self.client.delete('/funcionario/999')

        # Verifique se a resposta é 404 Not Found
        self.assertEqual(resposta.status_code, 404)

if __name__ == '__main__':
    unittest.main()