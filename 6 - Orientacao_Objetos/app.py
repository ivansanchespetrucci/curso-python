from modelos.escolas import Escola

filial_1 = Escola("Unidade SP","Avenida Paulista","11 945856")
filial_2 = Escola("Unidade RJ","Avenida Rio Branco","21 123945856")
filial_3 = Escola("unidade BA","avenida central","71 567545856")

filial_1.receber_avaliacao('Ivan',10)
filial_1.receber_avaliacao('Joao',5)

filial_2.receber_avaliacao('Joao',8)
filial_2.receber_avaliacao('Joao',0)

Escola.listar_escolas()