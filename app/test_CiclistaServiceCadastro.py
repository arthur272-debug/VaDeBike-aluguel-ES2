import unittest
from services import CiclistaService 
from dto import CiclistaDTO

#ciclista_dto = {
#    "nome": "João da Silva",
 #   "nascimento": "1990-01-01",
 #   "cpf": "123.456.789-00",
 #   "passaporte": "AB123456",
 #   "nacionalidade": "Brasileiro",
#  "email": "joao.silva@example.com",
  #  "urlFotoDocumento": "http://example.com/foto.jpg",
   # "senha": "senha123",
   # "cadastro": 
#}

class TestCiclistaServiceCadastro(unittest.TestCase):

    def test_cadastrarCiclista(self):
        
        ciclista = CiclistaDTO.CiclistaDto("Arthur","27/03/2002","122323",None,"Brasileiro","arthur.andre","https",0,"12356",None)
        resultado = CiclistaService.CiclistaService.cadastrarCiclista(ciclista)

        self.assertIn(resultado, CiclistaService.CiclistaService.Ciclista)

        self.assertEqual(resultado.id, len(CiclistaService.CiclistaService.Ciclista))

if __name__ == '__main__':
    unittest.main()

