from flask import Blueprint, request, jsonify
from dto import CiclistaDTO
from dto import CartaoDTO
from services import CiclistaService
from models.Ciclista import Nacionalidade
from models.Ciclista import RespostaCadastro
from models import Ciclista
import requests

invalido = "Dados Inválidos"
nao_econtrado = "Não encontrado"

ciclistaBp = Blueprint('ciclistaBp', __name__)


@ciclistaBp.route('/ciclista', methods=['POST'])
def realizar_cadastro():  # feito  a integração
    ciclista_dados = request.json

    # validação dos dados
    nacionalidade = ciclista_dados["nacionalidade"]
    nacionalidade_lower = nacionalidade.lower()
    if (nacionalidade_lower == "brasileira"):
        nacionalidade_valida = Nacionalidade.BRASILEIRA
        if not ciclista_dados["cpf"] or not ciclista_dados["nome"] or not ciclista_dados["nascimento"] or not ciclista_dados["email"] or not ciclista_dados["senha"]:
            return "Dados inválidos(Dado(s) vazio(s))", 422
    elif (nacionalidade_lower == "estrangeira"):
        if not ciclista_dados["numero"] or not ciclista_dados["validade"] or not ciclista_dados["pais"] or not ciclista_dados["nome"] or not ciclista_dados["nascimento"] or not ciclista_dados["email"] or not ciclista_dados["senha"]:
            return "Dados inválidos(Dado(s) vazio(s))", 422
        nacionalidade_valida = Nacionalidade.ESTRANGEIRA
    else:
        return "Dados inválidos(passaporte não válido)", 422

    cartao = requests.post(
        url='https://microservice-externo-hbkxpua2za-uc.a.run.app/validaCartaoDeCredito', json={'nomeTitular': 'ciclista_dados[nomeTitular]', 'numero': 'ciclista_dados[numero]', 'validade': 'ciclista_dados[validade]', 'cvv': 'ciclista_dados[cvv]'})
    if cartao.status_code != 422:
        return "Dados inválidos(Cartão não válido)", 422

    passaporte = Ciclista.Passaporte(
        ciclista_dados["numero"], ciclista_dados["validade"], ciclista_dados["pais"])
    cartao = CartaoDTO.CartaoDto(ciclista_dados["nomeTitular"], ciclista_dados["numero_cartao"],
                                 ciclista_dados["validade_cartao"], ciclista_dados["cvv"], len(CiclistaService.CiclistaService.Ciclista)+1)
    ciclista_dto = CiclistaDTO.CiclistaDto(ciclista_dados["nome"], ciclista_dados["nascimento"], ciclista_dados["cpf"], passaporte, nacionalidade_valida,
                                           ciclista_dados["email"], ciclista_dados["urlFotoDocumento"], 0, ciclista_dados["senha"], RespostaCadastro.CONFIRMACAO, cartao, None)

    ciclista = CiclistaService.CiclistaService.cadastrar_ciclista(ciclista_dto)

    if ciclista == "EmailInvalido":
        return "Dados inválidos(Email não válido ou já cadastrado)", 422

    informacoesCiclista = {"id": ciclista.id,
                           "status": ciclista.cadastro.value}
    envio_email = requests.post(url='https://microservice-externo-hbkxpua2za-uc.a.run.app/enviarEmail', json={
                                'email': 'ciclista_dados[email]', 'assunto': 'Cadastro de ciclista', 'menssagem': 'Ciclista foi cadastrado no sistema com sucesso!! Mas o mesmo precisa ainda ativar seu cadastro.'})

    if envio_email.status_code == 422:
        return "Dados inválidos(E-mail não enviado)", 422

    return jsonify(informacoesCiclista), 201


@ciclistaBp.route('/ciclista/<int:ciclista_id>', methods=['GET'])
def realizar_busca_ciclista(ciclista_id):

    ciclista = CiclistaService.CiclistaService.consultar_ciclista(ciclista_id)
    if ciclista is not None:
        informacoesCiclista = {"id": ciclista.id,
                               "status": ciclista.cadastro.value}
        return jsonify(informacoesCiclista), 200
    else:
        return "Requisição mal formada", 404


@ciclistaBp.route('/ciclista/<int:ciclista_id>', methods=['PUT'])
# está de acordo com o caso de uso
def realizar_atualizacao_ciclista(ciclista_id):
    ciclistaDados = request.json
    nacionalidade = ciclistaDados["nacionalidade"]
    nacionalidade_lower = nacionalidade.lower()

    if (nacionalidade_lower == "brasileira"):
        nacionalidade_valida = Nacionalidade.BRASILEIRA
        if not ciclistaDados["cpf"] or not ciclistaDados["nome"] or not ciclistaDados["nascimento"] or not ciclistaDados["email"] or not ciclistaDados["senha"]:
            return "Dados inválidos(Dado(s) vazio(s))", 422

    elif (nacionalidade_lower == "estrangeira"):
        nacionalidade_valida = Nacionalidade.ESTRANGEIRA
        if not ciclistaDados["numero"] or not ciclistaDados["validade"] or not ciclistaDados["pais"] or not ciclistaDados["nome"] or not ciclistaDados["nascimento"] or not ciclistaDados["email"] or not ciclistaDados["senha"]:
            return "Dados inválidos(Dado(s) vazio(s))", 422
    else:
        return "Dados inválidos(passaporte não válido)", 422

    passaporte = Ciclista.Passaporte(
        ciclistaDados["numero"], ciclistaDados["validade"], ciclistaDados["pais"])
    ciclista_dto = CiclistaDTO.CiclistaDto(ciclistaDados["nome"], ciclistaDados["nascimento"], ciclistaDados["cpf"], passaporte, nacionalidade_valida,
                                           ciclistaDados["email"], ciclistaDados["urlFotoDocumento"], 0, ciclistaDados["senha"], RespostaCadastro.CONFIRMACAO, None, None)
    ciclista = CiclistaService.CiclistaService.atualizar_ciclista(
        ciclista_id, ciclista_dto)

    if ciclista == "ErroCartao":
        return "Dados inválidos(Cartão não válido)", 422
    if ciclista == "EmailInvalido":
        return "Dados inválidos(Email não válido ou já cadastrado)", 422

    if ciclista is not None:

        informacoesCiclista = {"id": ciclista.id,
                               "status": ciclista.cadastro.value}

        envio_email = requests.post(url='https://microservice-externo-hbkxpua2za-uc.a.run.app/enviarEmail', json={
            'email': 'ciclista_dados[email]', 'assunto': 'Atualização de ciclista', 'menssagem': 'Ciclista foi atualizado no sistema com sucesso!!'})

        if envio_email.status_code == 422:
            return "Dados inválidos(E-mail não enviado)", 422

        return jsonify(informacoesCiclista), 200
    else:
        return nao_econtrado, 404


@ciclistaBp.route('/ciclista/<int:ciclista_id>/ativar', methods=['POST'])
def realizar_ativacao_ciclista(ciclista_id):  # verificado com o caso de uso 02

    ciclista = CiclistaService.CiclistaService.consultar_ciclista(ciclista_id)
    if ciclista is None:
        return nao_econtrado, 404

    if (ciclista.cadastro == RespostaCadastro.CONFIRMACAO):
        ciclista.cadastro = RespostaCadastro.ATIVO
        informacoesCiclista = {"id": ciclista.id,
                               "status": ciclista.cadastro.value}
        CiclistaService.CiclistaService.Confirmacao.append(informacoesCiclista)
        return jsonify(informacoesCiclista), 200
    else:
        return "Dados Inválidos(Dados fornecidos não correspondem ao um registro existente)", 422


@ciclistaBp.route('/ciclista/existeEmail/<email>', methods=['GET'])
def realizar_verificao_email(email):

    if '@' not in email:
        return "Email não enviado como parâmetro", 400

    ExisteEmail = CiclistaService.CiclistaService.consultar_ciclista_email(
        email)

    if ExisteEmail:
        return "True", 200
    else:
        return "False", 200
