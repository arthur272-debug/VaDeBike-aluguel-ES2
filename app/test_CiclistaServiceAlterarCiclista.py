import unittest
from services import CiclistaService
from unittest.mock import MagicMock


class TestCiclistaServiceAtualizar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        ciclista_mock1 = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None, nacionalidade="Brasileiro",
                                   email="arthur.andre@gmail.com", urlFotoDocumento="httpssssss", id=1, senha="12356", cadastro=None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock1)

    @unittest.skip("")
    def test_atualizarCiclista_existente(self):
        # Chame a função atualizarCiclista para um ID existente
        ciclista_mock2 = MagicMock(nome="Tutu", nascimento="23/02/2002", cpf="122345623", passaporte=None, nacionalidade="Estrangeiro",
                                   email="Tutu@gmail.com", urlFotoDocumento="httpssss", id=2, senha="12356789", cadastro=None)
        resultado = CiclistaService.CiclistaService.atualizar_ciclista(
            1, ciclista_mock2)

        # Verifique se o resultado não é None
        self.assertIsNotNone(resultado)

        # Verifique se os atributos foram atualizados corretamente
        self.assertEqual(resultado.nome, "Tutu")
        self.assertEqual(resultado.nascimento, "23/02/2002")
        self.assertEqual(resultado.cpf, "122345623")
        self.assertEqual(resultado.passaporte, None)
        self.assertEqual(resultado.nacionalidade, "Estrangeiro")
        self.assertEqual(resultado.email, "Tutu@gmail.com")
        self.assertEqual(resultado.urlFotoDocumento, "httpssss")
        self.assertEqual(resultado.senha, "12356789")

    @unittest.skip("")
    def test_atualizar_ciclista_inexistente(self):
        # Chame a função atualizarCiclista para um ID que não existe
        ciclista_mock3 = MagicMock(nome="Tutu", nascimento="23/05/2002", cpf="12234", passaporte=None, nacionalidade="Estrangeiro",
                                   email="Tutu2345@gmail.com", urlFotoDocumento="httpssdgsg", id=3, senha="1235678910", cadastro=None)
        resultado = CiclistaService.CiclistaService.atualizar_ciclista(
            999, ciclista_mock3)

        # Verifique se o resultado é None
        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
