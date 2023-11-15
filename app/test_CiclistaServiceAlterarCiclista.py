import unittest
from services import CiclistaService 
from dto import CiclistaDTO

class TestCiclistaServiceAtualizar(unittest.TestCase):

    def setUp(self):
        
        ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre@gmail.com","httpssssss",1,"12356",None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista)
        

    def test_atualizarCiclista_existente(self):
        
        ciclista2 = CiclistaDTO.CiclistaDto("Tutu","23/02/2002","122345623",None,"Estrangeiro","Tutu@gmail.com","httpssss",2,"12356789",None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista2)

        
        resultado = CiclistaService.CiclistaService.atualizarCiclista(1, ciclista2)

        
        self.assertIsNotNone(resultado)

        self.assertEqual(resultado.nome, "Tutu")
        self.assertEqual(resultado.nascimento, "23/02/2002")
        self.assertEqual(resultado.cpf, "122345623")
        self.assertEqual(resultado.passaporte, None)
        self.assertEqual(resultado.nacionalidade, "Estrangeiro")
        self.assertEqual(resultado.email, "Tutu@gmail.com")
        self.assertEqual(resultado.urlFotoDocumento,"httpssss")
        self.assertEqual(resultado.senha, "12356789")

    def test_atualizarCiclista_inexistente(self):
        
         ciclista3 = CiclistaDTO.CiclistaDto("Tutu","23/05/2002","12234",None,"Estrangeiro","Tutu2345@gmail.com","httpssdgsg",3,"1235678910",None)
         CiclistaService.CiclistaService.Ciclista.append(ciclista3)
       
         resultado = CiclistaService.CiclistaService.atualizarCiclista(999, ciclista3)

         self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()