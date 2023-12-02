import unittest
from services import FuncionarioService
from unittest.mock import MagicMock


class TestFuncionarioServiceConsultar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        FuncionarioService.FuncionarioService.funcionarios.clear
        funcionario_mock1 = MagicMock(senha="1234", cpf="123456789", email="arthur.andre@gmail.com",
                                      documento="cpf", funcao="analista de segurança", idade=21, nome="Nome1", id=1)
        funcionario_mock2 = MagicMock(senha="1234567689", cpf="1234567892343", email="tutu.andre@gmail.com",
                                      documento="rg", funcao="analista de T.I.", idade=25, nome="Nome5", id=2)
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock1)
        FuncionarioService.FuncionarioService.funcionarios.append(
            funcionario_mock2)

    def test_consultarFuncionario_existente(self):
        # Chame a função consultarFuncionario para um ID existente
        resultado = FuncionarioService.FuncionarioService.consultar_funcionario(
            1)

        # Verifique se o resultado não é None
        self.assertIsNotNone(resultado)

        # Verifique se os atributos do funcionário correspondem ao esperado
        self.assertEqual(resultado.id, 1)

    def test_consultarFuncionario_inexistente(self):
        # Chame a função consultarFuncionario para um ID que não existe
        resultado = FuncionarioService.FuncionarioService.consultar_funcionario(
            999990)

        # Verifique se o resultado é None
        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
