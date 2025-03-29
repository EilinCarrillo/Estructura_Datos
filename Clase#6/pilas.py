class Pila:
    def __init__(self):
        self.lista = []

    def apilar(self, elemento):
        self.lista.append(elemento)

    def desapilar(self):
        if len(self.lista) == 0:
            print("La pila está vacía, no se puede desapilar.")
            return None  
        return self.lista.pop()  

    def ver_tope(self):
        if len(self.lista) == 0:
            print("La pila está vacía, no hay tope.")
            return None
        return self.lista[-1]

    def esta_vacia(self):
        return len(self.lista) == 0

    def tamaño(self):
        return len(self.lista)


pila = Pila()

print("Apilando 5, 10 y 15...")
pila.apilar(5)
pila.apilar(10)
pila.apilar(15)

print("Tope actual:", pila.ver_tope()) 
print("Desapilando:", pila.desapilar())  
print("Nuevo tope:", pila.ver_tope())  
print("Tamaño de la pila:", pila.tamaño())  
print("¿Está vacía?", pila.esta_vacia()) 

print("Desapilando todo...")
pila.desapilar()
pila.desapilar()
print("¿Está vacía ahora?", pila.esta_vacia()) 




