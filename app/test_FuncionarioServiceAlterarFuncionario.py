import unittest
from services import FuncionarioService
from unittest.mock import Mock


class TestCiclistaServiceAtualizar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        FuncionarioService.FuncionarioService.funcionarios.clear
        funcionario_mock1 = Mock(cpf="1234567800", documento="12345678910", email="arthur.andre@gmail.com",
                                      funcao="Analista de T.I.", idade=21, nome="Arthur", id=1, senha="senha123")
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock1)

    def test_atualizarFuncionario_existente(self):
        # Chame a função atualizarFuncionario para um ID existente
        funcionario_mock2 = Mock(cpf="12345678", documento="cpf", email="tutu.andreee@gmail.com",
                                      funcao="Sênior de T.I.", idade=22, nome="Tutu", id=2, senha="nova_senha")
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock2)

        resultado = FuncionarioService.FuncionarioService.atualizar_funcionario(
            1, funcionario_mock2)

        # Verifique se o resultado não é None
        self.assertIsNotNone(resultado)

        # Verifique se os atributos do funcionário correspondem ao esperado
        self.assertEqual(resultado.nome, "Tutu")
        self.assertEqual(resultado.idade, 22)
        self.assertEqual(resultado.cpf, "12345678")
        self.assertEqual(resultado.documento, "cpf")
        self.assertEqual(resultado.funcao, "Sênior de T.I.")
        self.assertEqual(resultado.documento, "cpf")
        self.assertEqual(resultado.email, "tutu.andreee@gmail.com")
        self.assertEqual(resultado.senha, "nova_senha")

    def test_atualizarFuncionario_inexistente(self):
        # Chame a função atualizarFuncionario para um ID que não existe
        funcionario_mock3 = Mock(cpf="12345678", documento="12345678910111213", email="tutu.andre345@gmail.com",
                                      funcao="Consultor de T.I.", idade=21, nome="Arthur", id=0, senha="outra_senha")
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock3)

        resultado = FuncionarioService.FuncionarioService.atualizar_funcionario(
            9999999999, funcionario_mock3)

        # Verifique se o resultado é None
        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
