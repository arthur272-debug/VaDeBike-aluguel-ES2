class CartaoDto:

    def __init__(self,nomeTitular:str,numero:str,validade:str,cvv:str):
        self.nomeTitular=nomeTitular
        self.numero=numero
        self.validade=validade
        self.cvv=cvv