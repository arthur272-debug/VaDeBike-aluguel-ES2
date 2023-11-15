import unittest
from services import CiclistaService 
from dto import CiclistaDTO

class TestCiclistaServiceCadastro(unittest.TestCase):

    def test_cadastrarCiclista(self):
        
        ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre","https",0,"12356",None)
        resultado = CiclistaService.CiclistaService.cadastrarCiclista(ciclista)

        self.assertIn(resultado, CiclistaService.CiclistaService.Ciclista)

        self.assertEqual(resultado.id, len(CiclistaService.CiclistaService.Ciclista))

if __name__ == '__main__':
    unittest.main()

