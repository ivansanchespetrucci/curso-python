varArquivo = 'arquivo.txt'

conteudo = open(varArquivo,'rb')
linhas=conteudo.read() 
#linhas=conteudo.write('\nLinha adicionada')
print(linhas)





'''
r  = read       -> leitura
w  = write      -> gravacao
a  = append     -> inclui dados ao final do arquivo
b = binario     ->

r+ = read+write -> leitura + gravacao no inicio do arquivo
w+ = read+write -> leitura + gravacao no final  do arquivo

'''
