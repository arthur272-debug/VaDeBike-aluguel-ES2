import unittest
from services import CartaoService
from unittest.mock import MagicMock

class TestCartaoServiceConsultar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        cartao_mock = MagicMock(nomeTitular="Titular Antigo", numero="1111222233334444", validade="12/25", cvv="123", id=1)
        ciclista_mock1 = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None,nacionalidade="Brasileiro", email="arthur.andre@gmail.com", urlFotoDocumento="httpssssss",id=1, senha="12356", cadastro=None, cartao=cartao_mock, aluguel=None)
        CartaoService.ciclista_lista.append(ciclista_mock1)

    def test_consultar_cartao_existente(self):
        # Configurar dados fictícios para um teste bem-sucedido
        id_ciclista = 1

        # Chame a função consultar_cartao
        resultado = CartaoService.CartaoService.consultar_cartao(id_ciclista)

        # Verifique se o resultado não é nulo
        self.assertIsNotNone(resultado)

    def test_consultar_cartao_ciclista_nao_encontrado(self):
        # Configurar dados fictícios para um teste de falha
        id_ciclista_invalido = 999

        # Chame a função consultar_cartao
        resultado = CartaoService.CartaoService.consultar_cartao(id_ciclista_invalido)

        # Verifique se o resultado é None (ciclista não encontrado)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
