#%%
# -------------- Dicionarios
lista=['ivan','denise',12]  # lista
dicio  = {"Nome":"Ivan",
         "Idade":50,
          "Cidade":"SP",
          "Linguagens":["Python","Cobol","PHP","Java"],
          "Cargos":[
              {"empresa":"xpto","funcao":"Programador"},
              {"empresa":"abcd","funcao":"Analista"},
              {"empresa":"gpti","funcao":"Gerente"},
          ]
          }

print (dicio["Cargos"][0]["empresa"])







'''print (dicio)
dicio["nome"] = "Silva"
print (dicio)

for chave in dicio.keys():
    print (chave)
    
if "SP" in dicio.values():
    print("SP encontrado")
    '''

