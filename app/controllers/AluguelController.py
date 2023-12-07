from flask import Blueprint, request, jsonify
from dto import AluguelDTO
from services import AluguelService
import requests

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
        dados_bicicleta = {
            "id": dados_bicicleta.get('id'),
            "marca": dados_bicicleta.get('marca'),
            "modelo": dados_bicicleta.get('modelo'),
            "ano": dados_bicicleta.get('ano'),
            "status": dados_bicicleta.get('status')
        }
        return jsonify(dados_bicicleta), 200
    else:
        return "Vazio", 200


@aluguelBp.route('/aluguel', methods=['POST'])
def realizar_aluguel():
    aluguel_dados = request.json

    # validação dos dados
    tranca = aluguel_dados["trancaInicio"]
    tranca_valida = requests.get(
        url=f'https://va-de-bike-equipamentos-hbkxpua2za-uc.a.run.app/tranca/{tranca}')
    if tranca_valida.status_code == 404:
        return "Dados inválidos (Tranca inválida)", 422

    bicicleta_tranca = requests.get(
        url=f'https://va-de-bike-equipamentos-hbkxpua2za-uc.a.run.app/tranca/{tranca_valida}/bicicleta')

    if bicicleta_tranca.status_code == 404:
        return "Dados inválidos(Bicicleta não encontrada)", 422
    
    aluguel_dto = AluguelDTO.AluguelDto(
        aluguel_dados["ciclista"], tranca_valida, bicicleta_tranca, 0, 0, 0, 0, None)
    aluguel = AluguelService.AluguelService.alugar_bicicleta(aluguel_dto)

    if aluguel == "BicicletaNaoExiste":
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
