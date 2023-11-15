from flask import Blueprint, request, jsonify
from dto import FuncionarioDTO
from services import FuncionarioService

funcionarioBp = Blueprint('funcionarioBp',__name__)

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizarCadastro(): 
    funcionarioDados= request.json
    senha = funcionarioDados["senha"]
    confirmacaoSenha= funcionarioDados["confirmação_senha"]
    
    if (senha != confirmacaoSenha):
        return "Dados inválidos",422 
    
    if(
        not isinstance(funcionarioDados.get("senha"),str) or
        not isinstance(funcionarioDados.get("cpf"),str) or
        not isinstance(funcionarioDados.get("email"),str) or
        not isinstance(funcionarioDados.get("documento"),str) or
        not isinstance(funcionarioDados.get("funcao"),str) or
        not isinstance(funcionarioDados.get("idade"),int) or
        not isinstance(funcionarioDados.get("nome"),str)
    ):
        return "Dados inválidos",422  
    
    funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
    funcionario = FuncionarioService.FuncionarioService.cadastrarFuncionario(funcionarioDto)
    if funcionario is not None:
       infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":confirmacaoSenha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
       return jsonify(infomacoesFuncionario),200 
    else:
       return "Dados inválidos",422 

@funcionarioBp.route('/funcionario',methods=['GET'])
def realizarListagenFuncionarios(): 
    funcionarios= FuncionarioService.FuncionarioService.consultarListaFuncionario()
    if len(funcionarios) !=0 : 
       listagenFuncionarios =[{"senha": funcionario.senha, "cpf": funcionario.cpf, "email": funcionario.email, "documento": funcionario.documento,"funcao":funcionario.funcao, "idade": funcionario.idade, "nome": funcionario.nome,"id": funcionario.id} for funcionario in funcionarios]
       return jsonify(listagenFuncionarios), 200
    else:
        return "Não encontrado", 404

@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['GET'])
def realizarBuscaFuncionario(funcionarioId): 
    if not isinstance(funcionarioId,int):
        return "Dados Inválidos",422
    
    funcionario =FuncionarioService.FuncionarioService.consultarFuncionario(funcionarioId)
    if funcionario is not None:
        infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":funcionario.senha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
        return jsonify(infomacoesFuncionario),200
    else:
        return "Não encontrado",404
    
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['PUT']) 
def realizarAtualizacaoFuncionario(funcionarioId): 
        funcionarioDados = request.json
        confirmacaoSenha= funcionarioDados["confirmação_senha"]
        senha = funcionarioDados["senha"]

        if (senha != confirmacaoSenha):
           return "Dados inválidos",422 
    
        if(
             not isinstance(funcionarioDados.get("senha"),str) or
             not isinstance(funcionarioDados.get("cpf"),str) or
             not isinstance(funcionarioDados.get("email"),str) or
             not isinstance(funcionarioDados.get("documento"),str) or
             not isinstance(funcionarioDados.get("funcao"),str) or
             not isinstance(funcionarioDados.get("idade"),int) or
             not isinstance(funcionarioDados.get("nome"),str)
       ):
          return "Dados inválidos",422 

        funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
        funcionario = FuncionarioService.FuncionarioService.atualizarFuncionario(funcionarioId,funcionarioDto)
        if funcionario is not None:
            infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":funcionario.senha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
            return jsonify(infomacoesFuncionario),200
        else:
             return "Não encontrado", 404
        
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['DELETE'])
def realizarExclusaoFuncionario(funcionarioId): 
     if not isinstance(funcionarioId,int):
        return "Dados Inválidos",422
     
     funcionario = FuncionarioService.FuncionarioService.deletarFuncionario(funcionarioId)
     if funcionario == True:
          return "Dados removidos",200
     else:
          return "Não encontrado",404

