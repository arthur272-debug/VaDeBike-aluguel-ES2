from flask import Blueprint, request, jsonify
from dto import *
from services import *

funcionarioBp = Blueprint('funcionarioBp',__name__)

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizarCadastro(): # colocar a parte da exceção
    funcionarioDados= request.json
    funcionarioDto= FuncionarioDTO(funcionarioDados['senha'],funcionarioDados['cpf'], funcionarioDados['email'],funcionarioDados['documento'],funcionarioDados['funcao'],funcionarioDados['idade'],funcionarioDados['nome'])
    funcionario = FuncionarioService.cadastrarFuncionario(funcionarioDto)
    return jsonify(funcionario.__dict__), 200

@funcionarioBp.route('/funcionario',methods=['GET'])
def realizarListagenFuncionarios():# colocar a parte da exceção
    funcionarios= FuncionarioService.consultarListaFuncionario()
    funcionariosDto= [FuncionarioDTO(funcionario.senha, funcionario.cpf, funcionario.email, funcionario.documento, funcionario.funcao,funcionario.idade,funcionario.nome) for funcionario in funcionarios]
    return jsonify([funcionario.__dict__ for funcionario in funcionariosDto]),200

@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['GET'])
def realizarBuscaFuncionario(funcionarioId):# colocar a parte da exceção
    funcionario =FuncionarioService.consultarFuncionario(funcionarioId)
    if funcionario is not None:
        funcionarioDto= FuncionarioDTO(funcionario.senha,funcionario.cpf, funcionario.email, funcionario.documento, funcionario.funcao,funcionario.idade,funcionario.nome)
        return jsonify(funcionarioDto.__dict__),200
    else:
        return "Funcionário não encontrado",404
    
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['PUT'])
def realizarAtualizacaoFuncionario(funcionarioId):# colocar a parte da exceção
        funcionario = FuncionarioService.consultarFuncionario(funcionarioId)
        if funcionario is not None:
            funcionarioData = request.json
            funcionario.senha= funcionarioData.get('senha',funcionario.senha)
            funcionario.cpf= funcionarioData.get('cpf',funcionario.cpf)
            funcionario.email=funcionarioData.get('email',funcionario.email)
            funcionario.documento=funcionarioData.get('documento',funcionario.documento)
            funcionario.funcao=funcionarioData.get('funcao',funcionario.funcao)
            funcionario.idade=funcionarioData.get('idade',funcionario.idade)
            funcionario.nome=funcionarioData.get('nome',funcionario.nome)
            
            return jsonify(funcionario.__dict__),200    
        else:
             return "Funcionário não encontrado", 404
        
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['DELETE'])
def realizarExclusaoFuncionario(funcionarioId):# colocar a parte da exceção
     funcionario = FuncionarioService.consultarFuncionario(funcionarioId)

     if funcionario is not None:
          FuncionarioService.deletarFuncionario(funcionarioId)
          return "Funcionário excluído com sucesso",200
     else:
          return "Funcionário não encontrado",404

