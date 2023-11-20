import unittest
from services import FuncionarioService
from unittest.mock import MagicMock

class TestFuncionarioServiceCadastro(unittest.TestCase):

    def test_cadastrarFuncionario(self):
        # Chame a função cadastrarFuncionario com um objeto MagicMock simulando um DTO
        funcionario_mock = MagicMock(cpf="1234567800",documento="12345678910",email="arthur.andre@gmail.com",funcao="Analista de T.I.",idade=21,nome="Arthur",id=1,senha="senha123")
        resultado = FuncionarioService.FuncionarioService.cadastrar_funcionario(funcionario_mock)

        # Verifique se o resultado está na lista de funcionários
        self.assertIn(resultado, FuncionarioService.FuncionarioService.funcionarios)

        # Verifique se o ID do resultado corresponde ao esperado
        self.assertEqual(resultado.id, len(FuncionarioService.FuncionarioService.funcionarios))

if __name__ == '__main__':
    unittest.main()


