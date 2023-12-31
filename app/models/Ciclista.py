from enum import Enum


class Nacionalidade(Enum):

    BRASILEIRA = "BRASILEIRA"
    ESTRANGEIRA = "ESTRANGEIRA"


class RespostaCadastro(Enum):

    ATIVO = "ATIVO"
    INATIVO = "INATIVO"
    CONFIRMACAO = "AGUARDANDO_CONFIRMACAO"


class Passaporte:

    def __init__(self, numero: str, validade: str, pais: str):
        self.numero = numero
        self.validade = validade
        self.pais = pais


class Ciclista:

    def __init__(self, nome: str, nascimento: str, cpf: str, passaporte: object, nacionalidade, email: str, urlFotoDocumento: str, id: int, senha: str, cadastro, cartao: object, aluguel: object):

        self.senha = senha
        self.passaporte = passaporte
        self.nacionalidade = nacionalidade
        self.cadastro = cadastro
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.cartao = cartao
        self.aluguel = aluguel
        self.email = email
        self.urlFotoDocumento = urlFotoDocumento
        self.id = id
