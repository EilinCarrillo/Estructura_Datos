numeros=list()
def agregar(numero:int):
    numeros.append(numero)


persona=dict()
def agregar_valor(clave:str,valor:str):
    persona.update({clave:valor})
agregar_valor ('nombre','juan')
print (persona)