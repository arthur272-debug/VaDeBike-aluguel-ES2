import unittest
from services import FuncionarioService
from dto import FuncionarioDTO

class TestFuncionarioServiceCadastro(unittest.TestCase):

    def test_cadastrarFuncionario(self):
        
        funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        resultado = FuncionarioService.FuncionarioService.cadastrarFuncionario(funcionario)

        self.assertIn(resultado, FuncionarioService.FuncionarioService.funcionarios)

        self.assertEqual(resultado.id, len(FuncionarioService.FuncionarioService.funcionarios))

if __name__ == '__main__':
    unittest.main()

