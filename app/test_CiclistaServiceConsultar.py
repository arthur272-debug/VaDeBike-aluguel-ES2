import unittest
from services import CiclistaService 
from dto import CiclistaDTO

class TestCiclistaServiceConsultar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
         ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre","https",1,"12356",None)
         ciclista2 = CiclistaDTO.CiclistaDto("Arthur André","27/03/2002","122323",None,"Estrangeiro","arthur.andre","https",2,"12356",None)
         CiclistaService.CiclistaService.Ciclista.append(ciclista)
         CiclistaService.CiclistaService.Ciclista.append(ciclista2)

    def test_consultarCiclista_existente(self):
        # Chame a função consultarCiclista para um ID existente
        resultado = CiclistaService.CiclistaService.consultarCiclista(1)

        # Verifique se o resultado não é nulo
        self.assertIsNotNone(resultado)

        # Verifique se o ID do resultado é o esperado
        self.assertEqual(resultado.id, 1)

    def test_consultarCiclista_inexistente(self):
        # Chame a função consultarCiclista para um ID que não existe
        resultado = CiclistaService.CiclistaService.consultarCiclista(999)

        # Verifique se o resultado é nulo
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
