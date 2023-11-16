import unittest
from services import FuncionarioService
from dto import FuncionarioDTO

class TestFuncionarioServiceDeletar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario)

    def test_deletarFuncionario_existente(self):
        # Chame a função deletarFuncionario para um ID existente
        resultado = FuncionarioService.FuncionarioService.deletarFuncionario(1)

        # Verifique se o resultado é True (o funcionário foi removido)
        self.assertTrue(resultado)

        # Verifique se o funcionário foi removido da lista
        self.assertEqual(len(FuncionarioService.FuncionarioService.funcionarios), 0)

    def test_deletarFuncionario_inexistente(self):
        # Chame a função deletarFuncionario para um ID que não existe
        resultado = FuncionarioService.FuncionarioService.deletarFuncionario(999)

        # Verifique se o resultado é False (o funcionário não foi removido)
        self.assertFalse(resultado)

        # Verifique se o tamanho da lista permanece inalterado
        self.assertEqual(len(FuncionarioService.FuncionarioService.funcionarios), 1)

if __name__ == '__main__':
    unittest.main()