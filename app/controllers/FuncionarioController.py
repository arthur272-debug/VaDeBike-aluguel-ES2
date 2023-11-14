from flask import Blueprint, request, jsonify
from dto import FuncionarioDTO
from services import FuncionarioService

funcionarioBp = Blueprint('funcionarioBp',__name__)

#Verifcar as exceções em cada método com os casos de uso específicos

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizarCadastro(): 
    funcionarioDados= request.json
    funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
    funcionario = FuncionarioService.FuncionarioService.cadastrarFuncionario(funcionarioDto)
    if funcionario is not None:
       return "Dados Cadastrados com Sucesso!!",200
    else:
       return "Dados inválidos!!",422 

@funcionarioBp.route('/funcionario',methods=['GET'])
def realizarListagenFuncionarios(): 
    funcionarios= FuncionarioService.FuncionarioService.consultarListaFuncionario()
    if len(funcionarios) !=0 : 
       listagenFuncionarios =[{"senha": funcionario.senha, "cpf": funcionario.cpf, "email": funcionario.email, "documento": funcionario.documento,"funcao":funcionario.funcao, "idade": funcionario.idade, "nome": funcionario.nome,"id": funcionario.id} for funcionario in funcionarios]
       return jsonify(listagenFuncionarios), 200
    else:
         return "Lista de funcionários não encontrados",404

@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['GET'])
def realizarBuscaFuncionario(funcionarioId):
    funcionario =FuncionarioService.FuncionarioService.consultarFuncionario(funcionarioId)
    if funcionario is not None:
        infomacoesFuncionario = {"senha": funcionario.senha, "cpf": funcionario.cpf, "email": funcionario.email, "documento": funcionario.documento,"funcao":funcionario.funcao, "idade": funcionario.idade, "nome": funcionario.nome,"id": funcionario.id}
        return jsonify(infomacoesFuncionario),200
    else:
        return "Funcionário não encontrado",404
    
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['PUT']) 
def realizarAtualizacaoFuncionario(funcionarioId):
        funcionarioDados = request.json
        funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
        funcionario = FuncionarioService.FuncionarioService.atualizarFuncionario(funcionarioId,funcionarioDto)
        if funcionario is not None:
            infomacoesFuncionario = {"senha": funcionario.senha, "cpf": funcionario.cpf, "email": funcionario.email, "documento": funcionario.documento,"funcao":funcionario.funcao, "idade": funcionario.idade, "nome": funcionario.nome,"id": funcionario.id}
            return jsonify(infomacoesFuncionario),"Registro de funcionário atualizado!!",200
        else:
             return "Funcionário não encontrado", 404
        
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['DELETE'])
def realizarExclusaoFuncionario(funcionarioId):
     funcionario = FuncionarioService.FuncionarioService.deletarFuncionario(funcionarioId)
     if funcionario == True:
          return "Funcionário excluído com sucesso",200
     else:
          return "Funcionário não encontrado",404

