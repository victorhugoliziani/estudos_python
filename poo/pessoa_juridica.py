from pessoa import Pessoa 

class PessoaJuridica(Pessoa):

    def __init__(self, razao_social, cnpj):
        self._razao_social = razao_social
        self._cnpj = cnpj

    def validar_cnpj(cnpj=None):
        if cnpj is not None:
            return True
        return False