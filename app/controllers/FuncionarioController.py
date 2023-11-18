from flask import Blueprint, request, jsonify
from dto import FuncionarioDTO
from services import FuncionarioService

funcionarioBp = Blueprint('funcionarioBp',__name__)

invalido = "Dados Inválidos"
nao_econtrado= "Não encontrado"

@funcionarioBp.route('/funcionario',methods=['POST'])
def realizar_cadastro(): #Ok!
    funcionarioDados= request.json
    senha = funcionarioDados["senha"]
    confirmacaoSenha= funcionarioDados["confirmação_senha"]
    
    if (senha != confirmacaoSenha) or not isinstance(funcionarioDados.get("idade"),int) :
        return invalido,422 
    
    funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
    funcionario = FuncionarioService.FuncionarioService.cadastrarFuncionario(funcionarioDto)
    infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":confirmacaoSenha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
    return jsonify(infomacoesFuncionario),200 

@funcionarioBp.route('/funcionario',methods=['GET'])
def realizar_listagen_funcionarios(): 
    funcionarios= FuncionarioService.FuncionarioService.consultarListaFuncionario()
    if len(funcionarios) !=0 : 
       listagenFuncionarios =[{"senha": funcionario.senha, "cpf": funcionario.cpf, "email": funcionario.email, "documento": funcionario.documento,"funcao":funcionario.funcao, "idade": funcionario.idade, "nome": funcionario.nome,"id": funcionario.id} for funcionario in funcionarios]
       return jsonify(listagenFuncionarios), 200
    else:
        return nao_econtrado, 404

@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['GET'])
def realizar_busca_funcionario(funcionario_id): 
    if not isinstance(funcionario_id,int):
        return invalido,422
    
    funcionario =FuncionarioService.FuncionarioService.consultarFuncionario(funcionario_id)
    if funcionario is not None:
        infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":funcionario.senha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
        return jsonify(infomacoesFuncionario),200
    else:
        return nao_econtrado,404
    
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['PUT']) 
def realizar_atualizacao_funcionario(funcionario_id): 
        funcionarioDados = request.json
        confirmacaoSenha= funcionarioDados["confirmação_senha"]
        senha = funcionarioDados["senha"]

        if (senha != confirmacaoSenha) or not isinstance(funcionarioDados.get("idade"),int) :
         return invalido,422 

        funcionarioDto= FuncionarioDTO.FuncionarioDto(funcionarioDados["senha"],funcionarioDados["cpf"], funcionarioDados["email"],funcionarioDados["documento"],funcionarioDados["funcao"],funcionarioDados["idade"],funcionarioDados["nome"], 0)
        funcionario = FuncionarioService.FuncionarioService.atualizarFuncionario(funcionario_id,funcionarioDto)
        infomacoesFuncionario = {"senha": funcionario.senha, "confirmacaoSenha":funcionario.senha,"email": funcionario.email,"nome": funcionario.nome , "idade": funcionario.idade,"funcao":funcionario.funcao, "cpf": funcionario.cpf,"id": funcionario.id}
        return jsonify(infomacoesFuncionario),200
        
@funcionarioBp.route('/funcionario/<int:funcionarioId>',methods=['DELETE'])
def realizar_exclusao_funcionario(funcionario_id): 
     if not isinstance(funcionario_id,int):
        return invalido,422
     
     funcionario = FuncionarioService.FuncionarioService.deletarFuncionario(funcionario_id)
     if funcionario == True:
          return "Dados removidos",200
     else:
          return nao_econtrado,404