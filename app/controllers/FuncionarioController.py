from flask import Blueprint, request, jsonify
from dto import FuncionarioDTO
from services import FuncionarioService

funcionarioBp = Blueprint('funcionarioBp',__name__)

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizarCadastro():
    funcionarioDados= request.json
    