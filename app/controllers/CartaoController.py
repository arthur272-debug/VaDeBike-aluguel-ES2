from flask import Blueprint, request, jsonify
from dto import CartaoDTO
from services import CartaoService

cartaoBp = Blueprint('cartaoBp',__name__)
invalido = "Dados Inválidos"

@cartaoBp.route('/cartaoDeCredito/<int:id_Ciclista>',methods=['PUT'])
def realizar_atulizacao(id_ciclista):
    cartao_dados = request.json
    if not '-' in cartao_dados["validade"]:
        return invalido,422

    cartao_Dto = CartaoDTO.CartaoDto(cartao_dados["nomeTitular"],cartao_dados["numero"],cartao_dados["validade"],cartao_dados["cvv"])
    cartao = CartaoService.CartaoService.alterar_cartao(id_ciclista,cartao_Dto)
    if cartao is not None:
        return "Dados atualizados",200
    else:
        return "Não encontrado",404
    
@cartaoBp.route('/cartaoDeCredito/<int:id_Ciclista>',methods=['GET'])
def realizar_consultaCartao(id_ciclista):
    cartao= CartaoService.CartaoService.consultar_cartao(id_ciclista)
    if cartao is not None:
        informacoes_cartao = {"id":cartao.id,"nomeTitular":cartao.nomeTitular,"numero":cartao.numero,"validade":cartao.validade,"cvv":cartao.cvv}
        return jsonify(informacoes_cartao),200
    else:
        return invalido,404