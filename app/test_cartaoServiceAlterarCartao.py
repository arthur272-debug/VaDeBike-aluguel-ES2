import unittest
from services import CartaoService,CiclistaService
from unittest.mock import MagicMock

class TestCartaoServiceAlterar(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        cartao_mock = MagicMock(nomeTitular="Titular Antigo", numero="1111222233334444", validade="12/25", cvv="123", id=1)
        ciclista_mock1 = MagicMock(nome="Arthur", nascimento="27/03/2002", cpf="122323", passaporte=None,nacionalidade="Brasileiro", email="arthur.andre@gmail.com", urlFotoDocumento="httpssssss",id=1, senha="12356", cadastro=None, cartao=cartao_mock, aluguel=None)
        CiclistaService.CiclistaService.Ciclista.append(ciclista_mock1)

    def test_alterar_cartao_sucesso(self):
        # Configurar dados fictícios para um teste bem-sucedido
        id_ciclista = 1
        cartao_dto = MagicMock(nomeTitular="Novo Titular", numero="4444333322221111", validade="06/24", cvv="456")

        # Chame a função alterar_cartao
        resultado = CartaoService.CartaoService.alterar_cartao(id_ciclista, cartao_dto)

        # Verifique se o resultado é Não-nulo
        self.assertIsNotNone(resultado)

        # Verifique se os atributos do cartão foram atualizados corretamente
        self.assertEqual(resultado.nomeTitular, cartao_dto.nomeTitular)
        self.assertEqual(resultado.numero, cartao_dto.numero)
        self.assertEqual(resultado.validade, cartao_dto.validade)
        self.assertEqual(resultado.cvv, cartao_dto.cvv)

    def test_alterar_cartao_ciclista_nao_encontrado(self):
        # Configurar dados fictícios para um teste de falha
        id_ciclista_invalido = 999
        cartao_dto = MagicMock(nomeTitular="Novo Titular", numero="4444333322221111", validade="06/24", cvv="456")

        # Chame a função alterar_cartao
        resultado = CartaoService.CartaoService.alterar_cartao(id_ciclista_invalido, cartao_dto)

        # Verifique se o resultado é None (ciclista não encontrado)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
