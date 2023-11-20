import unittest
from services import FuncionarioService
from unittest.mock import MagicMock

class TestFuncionarioServiceConsultarLista(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        funcionario_mock1 = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com", documento="cpf",funcao="analista de segurança", idade=21, nome="Nome1", id=1)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario_mock1)
        funcionario_mock2 = MagicMock(senha="1234567689", cpf="1234567892343", email="tutu.andre@gmail.com", documento="rg",funcao="analista de T.I.", idade=25, nome="Nome5", id=2)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario_mock2)

    def test_consultarListaFuncionario(self):
        # Chame a função consultarListaFuncionario
        lista_funcionarios = FuncionarioService.FuncionarioService.consultar_lista_funcionario()

        # Verifique se o resultado é uma lista
        self.assertIsInstance(lista_funcionarios, list)

        # Verifique se a lista contém os funcionários esperados
        self.assertEqual(len(lista_funcionarios), len(FuncionarioService.FuncionarioService.funcionarios))
        for funcionario, funcionario_resultado in zip(FuncionarioService.FuncionarioService.funcionarios, lista_funcionarios):
            # Certifique-se de que os atributos do objeto mock foram acessados corretamente
            self.assertEqual(funcionario.cpf, funcionario_resultado.cpf)
            self.assertEqual(funcionario.documento, funcionario_resultado.documento)
            self.assertEqual(funcionario.email, funcionario_resultado.email)
            self.assertEqual(funcionario.funcao, funcionario_resultado.funcao)
            self.assertEqual(funcionario.idade, funcionario_resultado.idade)
            self.assertEqual(funcionario.nome, funcionario_resultado.nome)
            self.assertEqual(funcionario.id, funcionario_resultado.id)

if __name__ == '__main__':
    unittest.main()
