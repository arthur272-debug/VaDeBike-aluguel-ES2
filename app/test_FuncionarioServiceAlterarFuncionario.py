import unittest
from services import FuncionarioService 
from dto import FuncionarioDTO

class TestCiclistaServiceAtualizar(unittest.TestCase):

    def setUp(self):
        
        funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario)
        

    def test_atualizarFuncionario_existente(self):
        
        funcionario2 = FuncionarioDTO.FuncionarioDto("12345678","12345678910111213","tutu.andreee@gmail.com","cpf","Sênior de T.I.",22,"Tutu",2)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario2)

        
        resultado = FuncionarioService.FuncionarioService.atualizarFuncionario(1, funcionario2)
        
        self.assertIsNotNone(resultado)

        self.assertEqual(resultado.nome, "Tutu")
        self.assertEqual(resultado.idade, 22)
        self.assertEqual(resultado.cpf, "12345678910111213")
        self.assertEqual(resultado.funcao, "Consultor de T.I.")
        self.assertEqual(resultado.documento, "cpf")
        self.assertEqual(resultado.email, "tutu.andre@gmail.com")
        self.assertEqual(resultado.senha, "12345678")

    def test_atualizarFuncionario_inexistente(self):
        
         funcionario3 = FuncionarioDTO.FuncionarioDto("12345678","12345678910111213","tutu.andre345@gmail.com","cpf","Consultor de T.I.",21,"Arthur",2)
         FuncionarioService.FuncionarioService.funcionarios.append(funcionario3)
       
         resultado = FuncionarioService.FuncionarioService.atualizarFuncionario(999, funcionario3)

         self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()