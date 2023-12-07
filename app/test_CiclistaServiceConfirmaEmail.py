import unittest
from services import CiclistaService
from unittest.mock import MagicMock


class TestCiclistaServiceConfirmarEmail(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        ciclista_mock1 = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None, nacionalidade="Brasileiro",
                                   email="arthur.andre@gmail.com", urlFotoDocumento="https", id=1, senha="12356", cadastro=None)
        ciclista_mock2 = MagicMock(nome="Arthur André", nascimento="27/03/2002", cpf="122323", passaporte=None,
                                   nacionalidade="Estrangeiro", email="tutu@gmail.com", urlFotoDocumento="https", id=2, senha="12356", cadastro=None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock1)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock2)

    def test_confirmarEmail_existente(self):
        # Chame a função confirmarEmail para um email existente
        resultado = CiclistaService.CiclistaService.confirmar_email(
            "arthur.andre@gmail.com")

        # Verifique se o resultado é True
        self.assertTrue(resultado)

    def test_confirmarEmail_inexistente(self):
        # Chame a função confirmarEmail para um email que não existe
        resultado = CiclistaService.CiclistaService.confirmar_email(
            "nao_existe@example.com")

        # Verifique se o resultado é False
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
