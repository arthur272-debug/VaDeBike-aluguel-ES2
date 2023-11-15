from flask import Blueprint, request, jsonify
from dto import CiclistaDTO
from services import CiclistaService
from models import Nacionalidade
from models import RespostaCadastro
from models import Ciclista

ciclistaBp = Blueprint('ciclistaBp',__name__)

@ciclistaBp.route('/ciclista',methods=['POST'])
def realizarCadastro():
   ciclistaDados = request.json
   nacionalidade = ciclistaDados["passaporte"]
   nacionalidade_lower = nacionalidade.lower

   if(nacionalidade_lower == "brasileira"):
      nacionalidade_valida = Nacionalidade.BRASILEIRA
   elif(nacionalidade_lower == "estrangeira"):
       nacionalidade_valida = Nacionalidade.ESTRANGEIRA
   else:
      return "Dados inválidos",422 
   
   if(
        not isinstance(ciclistaDados.get("numero"),str) or
        not isinstance(ciclistaDados.get("validade"),str) or
        not isinstance(ciclistaDados.get("pais"),str) or
        not isinstance(ciclistaDados.get("senha"),str) or
        not isinstance(ciclistaDados.get("nascimento"),str) or
        not isinstance(ciclistaDados.get("nome"),str) or
        not isinstance(ciclistaDados.get("cpf"),str) or
        not isinstance(ciclistaDados.get("email"),str) or
        not isinstance(ciclistaDados.get("urlFotoDocumento"),str)
    ):
        return "Dados inválidos",422 
     
   passaporte = Ciclista.Passaporte(ciclistaDados["numero"],ciclistaDados["validade"],ciclistaDados["pais"])
   ciclistaDto = CiclistaDTO.CiclistaDto(ciclistaDados["nome"],ciclistaDados["nascimento"],ciclistaDados["cpf"],passaporte,nacionalidade_valida,ciclistaDados["email"],ciclistaDados["urlFotoDocumento"],0,ciclistaDados["senha"],RespostaCadastro.CONFIRMACAO)
   ciclista = CiclistaService.CiclistaService.cadastrarCiclista(ciclistaDto)
   if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro}
      return jsonify(informacoesCiclista), 201
   else:
      return "Requisição mal formada",404
   
@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['GET'])
def realizarBuscaCiclista(ciclistaId):
   if not isinstance(ciclistaId,int):
        return "Dados Inválidos",422
   
   ciclista= CiclistaService.CiclistaService.consultarCiclista(ciclistaId)
   if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro}
      return jsonify(informacoesCiclista), 200
   else:
       return "Requisição mal formada",404

@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['PUT'])
def realizarAtualizacaoCiclista(ciclistaId):
    ciclistaDados = request.json
    nacionalidade = ciclistaDados["passaporte"]
    nacionalidade_lower = nacionalidade.lower

    if(nacionalidade_lower == "brasileira"):
      nacionalidade_valida = Nacionalidade.BRASILEIRA
    elif(nacionalidade_lower == "estrangeira"):
       nacionalidade_valida = Nacionalidade.ESTRANGEIRA
    else:
      return "Dados inválidos",422 
   
    if(
        not isinstance(ciclistaDados.get("numero"),str) or
        not isinstance(ciclistaDados.get("validade"),str) or
        not isinstance(ciclistaDados.get("pais"),str) or
        not isinstance(ciclistaDados.get("senha"),str) or
        not isinstance(ciclistaDados.get("nascimento"),str) or
        not isinstance(ciclistaDados.get("nome"),str) or
        not isinstance(ciclistaDados.get("cpf"),str) or
        not isinstance(ciclistaDados.get("email"),str) or
        not isinstance(ciclistaDados.get("urlFotoDocumento"),str)
    ):
        return "Dados inválidos",422 
    
    passaporte = Ciclista.Passaporte(ciclistaDados["numero"],ciclistaDados["validade"],ciclistaDados["pais"])
    ciclistaDto = CiclistaDTO.CiclistaDto(ciclistaDados["nome"],ciclistaDados["nascimento"],ciclistaDados["cpf"],passaporte,nacionalidade_valida,ciclistaDados["email"],ciclistaDados["urlFotoDocumento"],0,ciclistaDados["senha"],RespostaCadastro.CONFIRMACAO)
    ciclista = CiclistaService.CiclistaService.atualizarCiclista(ciclistaId,ciclistaDto)
    if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro}
      return jsonify(informacoesCiclista), 200
    else:
      return "Não encontrado",404
    
@ciclistaBp.route('/ciclista/<int:ciclistaId>/ativar',methods=['POST'])
def realizarAtivacaoCiclista(ciclistaId):
   if not isinstance(ciclistaId,int):
        return "Dados Inválidos",422
   ciclista = CiclistaService.CiclistaService.consultarCiclista(ciclistaId)
   if ciclista is None:
      return "Não encontrado",404
   
   if (ciclista.cadastro == RespostaCadastro.CONFIRMACAO):
      ciclista.cadastro = RespostaCadastro.ATIVO
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro}
      return jsonify(informacoesCiclista), 200
   else:
      return "Dados inválidos",422
   
@ciclistaBp.route('/ciclista/existeEmail/<email>',methods=['GET'])
def realizarVerificaoEmail(email):
   if not isinstance(email,str):
        return "Dados Inválidos",422
   
   if not email.strip():
      return "Email não enviado como parâmetro", 400
   
   ExisteEmail = CiclistaService.CiclistaService.consultarCiclistaEmail(email)
   return ExisteEmail,200
   
   