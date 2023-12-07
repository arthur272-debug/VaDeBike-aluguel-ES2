import unittest
from services import CiclistaService
from unittest.mock import MagicMock


class TestCiclistaServiceCadastro(unittest.TestCase):

    @unittest.skip("")
    def test_cadastrarCiclista(self):
        # Chame a função cadastrarCiclista com um objeto MagicMock simulando um DTO
        ciclista_mock = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None,
                                  nacionalidade="Brasileiro", email="arthur.andre", urlFotoDocumento="https", id=0, senha="12356", cadastro=None)
        resultado = CiclistaService.CiclistaService.cadastrar_ciclista(
            ciclista_mock)

        # Verifique se o resultado está na lista de ciclistas
        self.assertIn(resultado, CiclistaService.CiclistaService.Ciclista)

        # Verifique se o ID do resultado corresponde ao esperado
        self.assertEqual(resultado.id, len(
            CiclistaService.CiclistaService.Ciclista))


if __name__ == '__main__':
    unittest.main()
