class Vehiculo :
    marca:str
    color : str
    modelo : int
    cilindraje : int 
    numero_ruedas : int 
    combustible:int 
    tipo_Carro_Moto:str 


def __init__(self, marca:str, combustible:int ) -> None:
        self.marca=marca
        self.combustible=combustible 
 
def __str__(self) ->str:
     return f"La marca del vehiculo {self.marca} y el nivel de combustible es {self.combustible}"


def encender (self):
    pass

def acelerar (self):
    pass

def frenar (self):
    pass

def apagar (self):
    pass

class Moto (Vehiculo):
     pass

class Carro (Vehiculo):
     pass

Vehiculo1=Vehiculo('Mazda',80)
print (Vehiculo1)

Moto1=Moto('Duke', 100)
print (Moto1)

Carro1=Carro('Renault', 130)
print (Carro1)





