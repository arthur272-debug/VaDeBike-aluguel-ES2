from flask import Blueprint, request, jsonify
from dto import CartaoDTO
from services import CartaoService

cartaoBp = Blueprint('cartaoBp',__name__)

#@cartaoBp.route('/cartaoDeCredito/<int: idCiclista>',methods=['PUT'])
#def rea