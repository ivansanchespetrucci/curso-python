def calculo(capital:float,taxa:float,meses:int)->float:
    """
    capital:
    valor inicial que sera corrigido
    
    taxa:
    taxa de rentabilidade

    meses:
    qt de meses a ser rentabilizado

    exemplo:
    capital = 500
    taxa    = 1.02 -> 2% 
    meses   = 6
    resultado = 
    """
    return capital * taxa ** meses


rend = calculo(5000,1.10,10)


print ("Rentabilidade = ", rend)