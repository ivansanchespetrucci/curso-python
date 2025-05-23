def soma(nome:str,*argu):
    print ("Quem me chamou ",)
    return sum(*argu)

def media(ptotal:float, pqt:int):
    return ptotal / pqt

valores= [10,20,30,30]

print ( soma("Jonas", valores)) 


#print ( media(soma(valores),len(valores)) )