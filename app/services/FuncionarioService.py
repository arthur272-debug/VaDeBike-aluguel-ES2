from models import Funcionario

class FuncionarioService:
    funcionarios =[]

    @staticmethod
    def cadastrarFuncionario(funcionario_dto):
        idFuncionario = len(FuncionarioService.funcionarios)+1
        funcionario_dto.id=idFuncionario
        funcionario =Funcionario.Funcionario(funcionario_dto.senha,funcionario_dto.cpf,funcionario_dto.email,funcionario_dto.documento,funcionario_dto.funcao,funcionario_dto.idade,funcionario_dto.nome,funcionario_dto.id)
        FuncionarioService.funcionarios.append(funcionario)
        return funcionario
    
    @staticmethod
    def consultarListaFuncionario():
        return FuncionarioService.funcionarios
    
    @staticmethod
    def consultarFuncionario(idFuncionario):
        for funcionario in FuncionarioService.funcionarios:
            if funcionario.id ==idFuncionario:
                return funcionario
        return None
    
    @staticmethod
    def atualizarFuncionario(idFuncionario,funcionario_dto):
        funcionario=FuncionarioService.consultarFuncionario(idFuncionario)
        if funcionario is not None:
            funcionario.senha = funcionario_dto.senha
            funcionario.cpf = funcionario_dto.cpf
            funcionario.email = funcionario_dto.email
            funcionario.documento = funcionario_dto.documento
            funcionario.funcao = funcionario_dto.funcao
            funcionario.idade = funcionario_dto.idade
            funcionario.nome = funcionario_dto.nome
            return funcionario
        return None

    @staticmethod
    def deletarFuncionario(idFuncionario):
         funcionario=FuncionarioService.consultarFuncionario(idFuncionario)
         if funcionario:
             FuncionarioService.funcionarios.remove(funcionario)
             return True
         return False
            
