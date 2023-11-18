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
   ciclista_dados = request.json
   nacionalidade = ciclista_dados["nacionalidade"]
   nacionalidade_lower = nacionalidade.lower()
   if(nacionalidade_lower == "brasileira"):
      nacionalidade_valida = Nacionalidade.BRASILEIRA
   elif(nacionalidade_lower == "estrangeira"):
       nacionalidade_valida = Nacionalidade.ESTRANGEIRA
   else:
      return invalido,422 
        
   passaporte = Ciclista.Passaporte(ciclista_dados["numero"],ciclista_dados["validade"],ciclista_dados["pais"])
   ciclista_dto = CiclistaDTO.CiclistaDto(ciclista_dados["nome"],ciclista_dados["nascimento"],ciclista_dados["cpf"],passaporte,nacionalidade_valida,ciclista_dados["email"],ciclista_dados["urlFotoDocumento"],0,ciclista_dados["senha"],RespostaCadastro.CONFIRMACAO)
   ciclista = CiclistaService.CiclistaService.cadastrarCiclista(ciclista_dto)
   informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
   return jsonify(informacoesCiclista), 201
  
   
@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['GET'])
def realizar_busca_ciclista(ciclista_id):
   if not isinstance(ciclista_id,int):
        return invalido,422
   
   ciclista= CiclistaService.CiclistaService.consultarCiclista(ciclista_id)
   if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
   else:
       return "Requisição mal formada",404

@ciclistaBp.route('/ciclista/<int:ciclistaId>',methods=['PUT'])
def realizar_atualizacao_ciclista(ciclista_id):
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
    ciclista = CiclistaService.CiclistaService.atualizarCiclista(ciclista_id,ciclistaDto)
    if ciclista is not None:
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
    else:
      return nao_econtrado,404
    
@ciclistaBp.route('/ciclista/<int:ciclistaId>/ativar',methods=['POST'])
def realizar_ativacao_ciclista(ciclista_id):
   if not isinstance(ciclista_id,int):
        return invalido,422
   ciclista = CiclistaService.CiclistaService.consultarCiclista(ciclista_id)
   if ciclista is None:
      return nao_econtrado,404
   
   if (ciclista.cadastro == RespostaCadastro.CONFIRMACAO):
      ciclista.cadastro = RespostaCadastro.ATIVO
      informacoesCiclista = {"id":ciclista.id,"status":ciclista.cadastro.value}
      return jsonify(informacoesCiclista), 200
   else:
      return invalido,422
   
@ciclistaBp.route('/ciclista/existeEmail/<email>',methods=['GET'])
def realizar_verificao_email(email):
   
   if not isinstance(email,str):
        return invalido,422
   
   if not email.strip():
      return "Email não enviado como parâmetro", 400
   
   ExisteEmail = CiclistaService.CiclistaService.consultarCiclistaEmail(email)

   if ExisteEmail:
      return "True", 200
   else:
      return "False",200
   
   
   