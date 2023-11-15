import unittest
from services import CiclistaService 
from dto import CiclistaDTO

class TestCiclistaServiceConsultar(unittest.TestCase):

    def setUp(self):
        
         ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre","https",1,"12356",None)
         ciclista2 = CiclistaDTO.CiclistaDto("Arthur André","27/03/2002","122323",None,"Estrangeiro","arthur.andre","https",2,"12356",None)
         CiclistaService.CiclistaService.Ciclista.append(ciclista)
         CiclistaService.CiclistaService.Ciclista.append(ciclista2)

    def test_consultarCiclista_existente(self):
        
        resultado = CiclistaService.CiclistaService.consultarCiclista(1)

        
        self.assertIsNotNone(resultado)

        
        self.assertEqual(resultado.id, 1)

    def test_consultarCiclista_inexistente(self):
        
        resultado = CiclistaService.CiclistaService.consultarCiclista(999)

        
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
