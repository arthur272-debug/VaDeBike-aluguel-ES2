import unittest
from services import FuncionarioService
from unittest.mock import MagicMock

FuncionarioService.FuncionarioService.funcionarios.clear


class TestFuncionarioServiceDeletar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes

        funcionario_mock = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com",
                                     documento="cpf", funcao="analista de segurança", idade=21, nome="Nome1", id=1)
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock)

    def test_deletarFuncionario_existente(self):
        # Chame a função deletarFuncionario para um ID existente
        resultado = FuncionarioService.FuncionarioService.deletar_funcionario(
            1)

        # Verifique se o resultado é True (o funcionário foi removido)
        self.assertTrue(resultado)

        # Verifique se o funcionário foi removido da lista
        self.assertEqual(
            len(FuncionarioService.FuncionarioService.funcionarios), 0)

    def test_deletarFuncionario_inexistente(self):
        # Chame a função deletarFuncionario para um ID que não existe
        resultado = FuncionarioService.FuncionarioService.deletar_funcionario(
            999)

        # Verifique se o resultado é False (o funcionário não foi removido)
        self.assertFalse(resultado)

        # Verifique se o tamanho da lista permanece inalterado
        self.assertEqual(
            len(FuncionarioService.FuncionarioService.funcionarios), 1)


if __name__ == '__main__':
    unittest.main()
