from models import Funcionario


class FuncionarioService:
    funcionarios = []

    @staticmethod
    def cadastrar_funcionario(funcionario_dto):
        idFuncionario = len(FuncionarioService.funcionarios)+1
        funcionario_dto.id = idFuncionario
        funcionario = Funcionario.Funcionario(funcionario_dto.senha, funcionario_dto.cpf, funcionario_dto.email,
                                              funcionario_dto.documento, funcionario_dto.funcao, funcionario_dto.idade, funcionario_dto.nome, funcionario_dto.id)
        FuncionarioService.funcionarios.append(funcionario)
        return funcionario

    @staticmethod
    def consultar_lista_funcionario():
        lista_funcionarios = FuncionarioService.funcionarios
        return lista_funcionarios

    @staticmethod
    def consultar_funcionario(idFuncionario):
        for funcionario in FuncionarioService.funcionarios:
            if funcionario.id == idFuncionario:
                return funcionario
        return None

    @staticmethod
    def atualizar_funcionario(idFuncionario, funcionario_dto):
        funcionario = FuncionarioService.consultar_funcionario(idFuncionario)
        if funcionario is not None:
            funcionario_novo = Funcionario.Funcionario(funcionario_dto.senha, funcionario_dto.cpf, funcionario_dto.email,
                                                       funcionario_dto.documento, funcionario_dto.funcao, funcionario_dto.idade, funcionario_dto.nome, 0)
            funcionario.senha = funcionario_novo.senha
            funcionario.cpf = funcionario_novo.cpf
            funcionario.email = funcionario_novo.email
            funcionario.documento = funcionario_novo.documento
            funcionario.funcao = funcionario_novo.funcao
            funcionario.idade = funcionario_novo.idade
            funcionario.nome = funcionario_novo.nome
        return Funcionario

    @staticmethod
    def deletar_funcionario(idFuncionario):
        funcionario = FuncionarioService.consultar_funcionario(idFuncionario)
        if funcionario is not None:
            FuncionarioService.funcionarios.remove(funcionario)
            return True
        return False
