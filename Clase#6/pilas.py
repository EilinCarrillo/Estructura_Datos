class NodoPila:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None
        self._tamanio = 0

    def apilar(self, elemento):
        nuevo = NodoPila(elemento, self.cima)
        self.cima = nuevo
        self._tamanio += 1

    def desapilar(self):
        if self.cima is None:
            print("La pila está vacía, no se puede desapilar.")
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        self._tamanio -= 1
        return valor

    def ver_tope(self):
        if self.cima is None:
            print("La pila está vacía, no hay tope.")
            return None
        return self.cima.valor

    def esta_vacia(self):
        return self.cima is None

    def tamaño(self):
        return self._tamanio


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




