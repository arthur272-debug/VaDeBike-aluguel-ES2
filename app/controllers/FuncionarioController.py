from flask import Blueprint, request, jsonify
from dto import FuncionarioDTO
from services import FuncionarioService

funcionarioBp = Blueprint('funcionarioBp',__name__)

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizarCadastro(): 
    funcionarioDados= request.json
    funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"],funcionarioDados["id"])
    funcionario = FuncionarioService.FuncionarioService.cadastrarFuncionario(funcionarioDto)
    if funcionario is not None:
       return "Dados Cadastrados com Sucesso!!",200
    else:
       return "Dados inválidos!!",422 

@funcionarioBp.route('/funcionario',methods=['GET'])
def realizarListagenFuncionarios():
    funcionarios= FuncionarioService.FuncionarioService.consultarListaFuncionario()
    if funcionarios is not None:
       return jsonify(funcionarios), 200
    else:
         return "Lista de funcionários não encontrados",404

@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['GET'])
def realizarBuscaFuncionario(funcionarioId):# colocar a parte da exceção
    funcionario =FuncionarioService.FuncionarioService.consultarFuncionario(funcionarioId)
    if funcionario is not None:
        return jsonify(funcionario),200
    else:
        return "Funcionário não encontrado",404
    
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['PUT'])
def realizarAtualizacaoFuncionario(funcionarioId):# colocar a parte da exceção
        funcionario = FuncionarioService.FuncionarioService.consultarFuncionario(funcionarioId)
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
     funcionario = FuncionarioService.FuncionarioService.consultarFuncionario(funcionarioId)

     if funcionario is not None:
          FuncionarioService.FuncionarioService.deletarFuncionario(funcionarioId)
          return "Funcionário excluído com sucesso",200
     else:
          return "Funcionário não encontrado",404

