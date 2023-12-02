import unittest
from services import CiclistaService
from unittest.mock import MagicMock

CiclistaService.CiclistaService.Ciclista = []


class TestCiclistaServiceConsultarEmail(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        ciclista_mock1 = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None, nacionalidade="Brasileiro",
                                   email="arthur.andre@gmail.com", urlFotoDocumento="https", id=1, senha="12356", cadastro=None, aluguel=None)
        ciclista_mock2 = MagicMock(nome="Arthur André", nascimento="27/03/2002", cpf="122323", passaporte=None,
                                   nacionalidade="Estrangeiro", email="arthurandre@gmail.com", urlFotoDocumento="https", id=2, senha="12356", cadastro=None, aluguel=None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock1)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock2)

    def test_consultar_ciclistaEmail_existente(self):
        # Chame a função para um email existente
        resultado = CiclistaService.CiclistaService.consultar_ciclista_email(
            "arthur.andre@gmail.com")

        # Verifique se o resultado é True
        self.assertTrue(resultado)

    def test_consultar_ciclistaEmail_inexistente(self):
        # Chame a função consultarCiclistaEmail para um email que não existe
        resultado = CiclistaService.CiclistaService.consultar_ciclista_email(
            "tutu@gmail.com")

        # Verifique se o resultado é False
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
