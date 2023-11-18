from flask import Blueprint, request, jsonify
from dto import CiclistaDTO
from services import CiclistaService
from models.Ciclista import Nacionalidade
from models.Ciclista import RespostaCadastro
from models import Ciclista

invalido = "Dados Inválidos"
nao_econtrado= "Não encontrado"

ciclistaBp = Blueprint('ciclistaBp',__name__)

@ciclistaBp.route('/ciclista',methods=['POST'])
def realizar_cadastro():
   ciclistaDados = request.json
   nacionalidade = ciclistaDados["nacionalidade"]
   nacionalidade_lower = nacionalidade.lower()
   if(nacionalidade_lower == "brasileira"):
      nacionalidade_valida = Nacionalidade.BRASILEIRA
   elif(nacionalidade_lower == "estrangeira"):
       nacionalidade_valida = Nacionalidade.ESTRANGEIRA
   else:
      return invalido,422 
        
   passaporte = Ciclista.Passaporte(ciclistaDados["numero"],ciclistaDados["validade"],ciclistaDados["pais"])
   ciclistaDto = CiclistaDTO.CiclistaDto(ciclistaDados["nome"],ciclistaDados["nascimento"],ciclistaDados["cpf"],passaporte,nacionalidade_valida,ciclistaDados["email"],ciclistaDados["urlFotoDocumento"],0,ciclistaDados["senha"],RespostaCadastro.CONFIRMACAO)
   ciclista = CiclistaService.CiclistaService.cadastrarCiclista(ciclistaDto)
   informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
   return jsonify(informacoesCiclista), 201
  
   
@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['GET'])
def realizar_buscaCiclista(ciclistaId):
   if not isinstance(ciclistaId,int):
        return invalido,422
   
   ciclista= CiclistaService.CiclistaService.consultarCiclista(ciclistaId)
   if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
   else:
       return "Requisição mal formada",404

@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['PUT'])
def realizar_atualizacaoCiclista(ciclistaId):
    ciclistaDados = request.json
    nacionalidade = ciclistaDados["nacionalidade"]
    nacionalidade_lower = nacionalidade.lower()

    if(nacionalidade_lower == "brasileira"):
      nacionalidade_valida = Nacionalidade.BRASILEIRA
    elif(nacionalidade_lower == "estrangeira"):
       nacionalidade_valida = Nacionalidade.ESTRANGEIRA
    else:
      return invalido,422 
    
    passaporte = Ciclista.Passaporte(ciclistaDados["numero"],ciclistaDados["validade"],ciclistaDados["pais"])
    ciclistaDto = CiclistaDTO.CiclistaDto(ciclistaDados["nome"],ciclistaDados["nascimento"],ciclistaDados["cpf"],passaporte,nacionalidade_valida,ciclistaDados["email"],ciclistaDados["urlFotoDocumento"],0,ciclistaDados["senha"],RespostaCadastro.CONFIRMACAO)
    ciclista = CiclistaService.CiclistaService.atualizarCiclista(ciclistaId,ciclistaDto)
    if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
    else:
      return nao_econtrado,404
    
@ciclistaBp.route('/ciclista/<int:ciclistaId>/ativar',methods=['POST'])
def realizar_ativacaoCiclista(ciclistaId):
   if not isinstance(ciclistaId,int):
        return invalido,422
   ciclista = CiclistaService.CiclistaService.consultarCiclista(ciclistaId)
   if ciclista is None:
      return nao_econtrado,404
   
   if (ciclista.cadastro == RespostaCadastro.CONFIRMACAO):
      ciclista.cadastro = RespostaCadastro.ATIVO
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
   else:
      return invalido,422
   
@ciclistaBp.route('/ciclista/existeEmail/<email>',methods=['GET'])
def realizar_verificaoEmail(email):
   
   if not isinstance(email,str):
        return invalido,422
   
   if not email.strip():
      return "Email não enviado como parâmetro", 400
   
   ExisteEmail = CiclistaService.CiclistaService.consultarCiclistaEmail(email)

   if ExisteEmail:
      return "True", 200
   else:
      return "False",200
   
   
   