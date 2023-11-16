import unittest
from services import FuncionarioService
from dto import FuncionarioDTO

class TestFuncionarioServiceConsultar(unittest.TestCase):

    def setUp(self):
        
        funcionario = FuncionarioDTO.FuncionarioDto("1234567800","12345678910","arthur.andre@gmail.com","cpf","Analista de T.I.",21,"Arthur",1)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario)
        funcionario2 = FuncionarioDTO.FuncionarioDto("12345678","12345678910111213","tutu.andre@gmail.com","cpf","Analista de T.I.",22,"Tutu",2)
        FuncionarioService.FuncionarioService.funcionarios.append(funcionario2)

    def test_consultarFuncionario_existente(self):
        
        resultado = FuncionarioService.FuncionarioService.consultarFuncionario(1)

        self.assertIsNotNone(resultado)

        
        self.assertEqual(resultado.id, 1)

    def test_consultarFuncionario_inexistente(self):
        
        resultado = FuncionarioService.FuncionarioService.consultarFuncionario(999)

       
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()