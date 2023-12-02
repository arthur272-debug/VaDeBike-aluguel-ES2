from flask import Blueprint, request, jsonify
from dto import AluguelDTO
from services import AluguelService

aluguelBp = Blueprint('aluguelBp', __name__)
invalido = "Dados Inválidos"
nao_econtrado = "Não encontrado"


@aluguelBp.route('/ciclista/<int:id_ciclista>/permiteAluguel', methods=['GET'])
def consulta_permite_aluguel(id_ciclista):
    aluguel = AluguelService.AluguelService.verificar_ciclista_aluguel(
        id_ciclista)

    if aluguel == False:
        return nao_econtrado, 404

    if aluguel is not None:
        return "False", 200
    else:
        return "True", 200


@aluguelBp.route('/ciclista/<int:id_ciclista>/bicicletaAlugada', methods=['GET'])
def consulta_bicicleta_alugada(id_ciclista):
    bicicleta = AluguelService.AluguelService.verificar_bicicleta_alugada(
        id_ciclista)

    if bicicleta == False:
        return nao_econtrado, 404

    if bicicleta is not None:
        informacoes_bicicleta = {"id": bicicleta.id, "marca": bicicleta.marca,
                                 "modelo": bicicleta.modelo, "ano": bicicleta.ano, "status": bicicleta.status}
        return jsonify(informacoes_bicicleta), 200
    else:
        return "Vazio", 200


@aluguelBp.route('/aluguel', methods=['POST'])
def realizar_aluguel():
    aluguel_dados = request.json
    aluguel_dto = AluguelDTO.AluguelDto(
        aluguel_dados["ciclista"], aluguel_dados["trancaInicio"], 0, 0, 0, 0, 0,None)
    aluguel = AluguelService.AluguelService.alugar_bicicleta(aluguel_dto)

    if aluguel == "ErroTranca":
        return "Dados Inválidos(Tranca Inválida)", 422
    elif aluguel == "BicicletaNaoExiste":
        return "Dados Inválidos(Bicicleta Não existe)", 422
    elif aluguel == "BicicletaReparo":
        return "Dados Inválidos(Bicicleta não está em condições de uso)"
    elif aluguel == "PagamentoNaoFeito":
        return "Dados Inválidos(Pagamento não realizado)"

    if aluguel is not None:
        informacoes_aluguel = {"bicicleta": aluguel.bicicleta, "horaInicio": aluguel.horaInicio, "trancaFim": aluguel.trancaFim,
                               "horaFim": aluguel.horaFim, "cobranca": aluguel.cobranca, "ciclista": aluguel.ciclista, "trancaInicio": aluguel.trancaInicio}
        return jsonify(informacoes_aluguel), 200
    else:
        return invalido, 422


@aluguelBp.route('/devolucao', methods=['POST'])
def realizar_devolucao():
    devolucao_dados = request.json
    devolucao = AluguelService.AluguelService.devolver_bicicleta(
        devolucao_dados['idBicicleta'], devolucao_dados['idTranca'])

    if devolucao is not None:
        informacoes_devolucao = {"bicicleta": devolucao.bicicleta, "horaInicio": devolucao.horaInicio, "trancaFim": devolucao.trancaFim,
                                 "horaFim": devolucao.horaFim, "cobranca": devolucao.cobranca, "ciclista": devolucao.ciclista, "trancaInicio": devolucao.trancaInicio}
        return jsonify(informacoes_devolucao), 200
    else:
        return invalido, 422
