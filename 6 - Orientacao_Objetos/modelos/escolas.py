from modelos.avaliacao import Avaliacao

class Escola:
    escolas = []

    def __init__(self,nome,endereco,telefone):
        self.nome = nome.upper()
        self.endereco =  endereco.title()
        self.telefone = telefone
        self._ativa = True
        self._avaliacao = []
        Escola.escolas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.endereco} | {self.telefone} | {self.ativa}'
    
    def listar_escolas():
        print (f'{'Nome da Escola'.ljust(20)} | {'Endereco'.ljust(20)} | {'Telefone'.ljust(20)} | {'Avaliacao'.ljust(20)} | {'Status'.ljust(20)} ')
        for escola in Escola.escolas:
            print (f'{escola.nome.ljust(20)} | {escola.endereco.ljust(20)} | {escola.telefone.ljust(20)} | {str(escola.media_avaliacoes).ljust(20)} | {escola.ativa}')

    def mudar_status(self,status):
        self._ativa = status

    @property
    def ativa(self):
        return 'Ativa' if self._ativa  else 'Inativa'
            
    def receber_avaliacao(self,aluno,nota):
        aval = Avaliacao(aluno,nota)
        self._avaliacao.append(aval)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Sem avaliacao"
        soma  = sum(avaliacao._nota for avaliacao in self._avaliacao )
        quant = len(self._avaliacao)
        return  soma / quant  


'''filial_1 = Escola("Unidade SP","Avenida Paulista","11 945856")
filial_2 = Escola("Unidade RJ","Avenida Rio Branco","21 123945856")
filial_3 = Escola("unidade BA","avenida central","71 567545856")

filial_2.mudar_status(False)

Escola.listar_escolas()
'''
