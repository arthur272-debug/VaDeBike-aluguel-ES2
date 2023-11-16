import unittest
from services import FuncionarioService 
from dto import FuncionarioDTO

class TestFuncionarioServiceConsultarLista(unittest.TestCase):

    def setUp(self):
         funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
         funcionario2 = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
         FuncionarioService.FuncionarioService.funcionarios.append(funcionario)
         FuncionarioService.FuncionarioService.funcionarios.append(funcionario2)


    def test_consultarListaFuncionario(self):
        # Chame a função consultarListaFuncionario
        lista_funcionarios = FuncionarioService.FuncionarioService.consultarListaFuncionario()

        # Verifique se o resultado é uma lista
        self.assertIsInstance(lista_funcionarios, list)

        # Verifique se a lista contém os funcionários esperados
        self.assertEqual(len(lista_funcionarios), len(FuncionarioService.FuncionarioService.funcionarios))
        for funcionario, funcionario_resultado in zip(FuncionarioService.FuncionarioService.funcionarios, lista_funcionarios):
            self.assertEqual(funcionario.nome, funcionario_resultado.nome)
            self.assertEqual(funcionario.funcao, funcionario_resultado.funcao)
            self.assertEqual(funcionario.id, funcionario_resultado.id)

if __name__ == '__main__':
    unittest.main()