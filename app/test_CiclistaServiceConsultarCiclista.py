import unittest
from services import CiclistaService
from unittest.mock import MagicMock

class TestCiclistaServiceConsultar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        ciclista_mock1 = MagicMock(nome="Arthur",nascimento="27/03/2002",cpf="122323",passaporte=None,nacionalidade="Brasileiro",email="arthur.andre",urlFotoDocumento="https",id=1,senha="12356",cadastro=None)
        ciclista_mock2 = MagicMock(nome="Arthur André",nascimento="27/03/2002",cpf="122323",passaporte=None,nacionalidade="Estrangeiro",email="arthur.andre",urlFotoDocumento="https",id=2,senha="12356",cadastro=None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock1)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock2)

    def test_consultarCiclista_existente(self):
        # Chame a função consultarCiclista para um ID existente
        resultado = CiclistaService.CiclistaService.consultar_ciclista(1)

        # Verifique se o resultado não é None
        self.assertIsNotNone(resultado)

        # Verifique se o ID do resultado corresponde ao esperado
        self.assertEqual(resultado.id, 1)

    def test_consultarCiclista_inexistente(self):
        # Chame a função consultarCiclista para um ID que não existe
        resultado = CiclistaService.CiclistaService.consultar_ciclista(999)

        # Verifique se o resultado é None
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
