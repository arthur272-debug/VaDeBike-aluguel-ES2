import unittest
from services import CiclistaService 
from dto import CiclistaDTO

class TestCiclistaServiceConsultarEmail(unittest.TestCase):

    def setUp(self):
        
        ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre@gmail.com","https",1,"12356",None)
        ciclista2 = CiclistaDTO.CiclistaDto("Arthur André","27/03/2002","122323",None,"Estrangeiro","arthurandre@gmail.com","https",2,"12356",None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista)
        CiclistaService.CiclistaService.Ciclista.append(ciclista2)

    def test_consultarCiclistaEmail_existente(self):
        
        resultado = CiclistaService.CiclistaService.consultarCiclistaEmail("arthur.andre@gmail.com")

       
        self.assertTrue(resultado)

    def test_consultarCiclistaEmail_inexistente(self):
        
        resultado = CiclistaService.CiclistaService.consultarCiclistaEmail("tutu@gmail.com")

        
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()