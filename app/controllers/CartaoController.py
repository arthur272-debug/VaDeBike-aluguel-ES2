from flask import Blueprint, request, jsonify
from dto import CartaoDTO
from services import CartaoService
import requests

cartaoBp = Blueprint('cartaoBp', __name__)
invalido = "Dados Inválidos"


@cartaoBp.route('/cartaoDeCredito/<int:id_ciclista>', methods=['PUT'])
def realizar_atulizacao(id_ciclista):
    cartao_dados = request.json
    if '-' not in cartao_dados["validade"]:
        return "Dados Inválidos(Validade inválida)", 422

    cartao_dto = CartaoDTO.CartaoDto(
        cartao_dados["nomeTitular"], cartao_dados["numero"], cartao_dados["validade"], cartao_dados["cvv"], id_ciclista)
    cartao = CartaoService.CartaoService.alterar_cartao(
        id_ciclista, cartao_dto)

    if cartao == "ErroCartao":
        return "Dados inválidos(Cartão não válido)", 422

    if cartao is not None:
        envio_email = requests.post(url='https://microservice-externo-hbkxpua2za-uc.a.run.app/enviarEmail', json={
            'email': 'ciclista_dados[email]', 'assunto': 'Atualização de ciclista', 'menssagem': 'Ciclista foi atualizado no sistema com sucesso!!'})

        if envio_email.status_code == 422:
            return "Dados inválidos(E-mail não enviado)", 422

        return "Dados atualizados do cartão", 200
    else:
        return "Não encontrado(Ciclista)", 404


@cartaoBp.route('/cartaoDeCredito/<int:id_ciclista>', methods=['GET'])
def realizar_consulta_cartao(id_ciclista):
    cartao = CartaoService.CartaoService.consultar_cartao(id_ciclista)
    if cartao is not None:
        informacoes_cartao = {"id": cartao.id, "nomeTitular": cartao.nomeTitular,
                              "numero": cartao.numero, "validade": cartao.validade, "cvv": cartao.cvv}
        return jsonify(informacoes_cartao), 200
    else:
        return "Não encontrado", 404
