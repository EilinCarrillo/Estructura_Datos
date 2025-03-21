class Pila:
    def __init__(self):
        # Lista vacía para almacenar los elementos de la pila
        self.lista = []

    def apilar(self, elemento):
        # Agrega un elemento a la pila (al final de la lista)
        self.lista.append(elemento)

    def desapilar(self):
        # Verifica si la pila está vacía antes de intentar sacar un elemento
        if len(self.lista) == 0:
            print("La pila está vacía, no se puede desapilar.")
            return None  # Retorna None si no hay nada que quitar
        return self.lista.pop()  # Elimina y devuelve el último elemento

    def ver_tope(self):
        # Si la pila está vacía, no hay tope que mostrar
        if len(self.lista) == 0:
            print("La pila está vacía, no hay tope.")
            return None
        return self.lista[-1]  # Devuelve el último elemento sin eliminarlo

    def esta_vacia(self):
        # Devuelve True si la pila está vacía, de lo contrario False
        return len(self.lista) == 0

    def tamaño(self):
        # Devuelve cuántos elementos tiene la pila
        return len(self.lista)


# Pruebas básicas
pila = Pila()

print("Apilando 5, 10 y 15...")
pila.apilar(5)
pila.apilar(10)
pila.apilar(15)

print("Tope actual:", pila.ver_tope())  # Debería mostrar 15
print("Desapilando:", pila.desapilar())  # Debería sacar el 15
print("Nuevo tope:", pila.ver_tope())  # Debería mostrar 10
print("Tamaño de la pila:", pila.tamaño())  # Debería ser 2
print("¿Está vacía?", pila.esta_vacia())  # Debería ser False

print("Desapilando todo...")
pila.desapilar()
pila.desapilar()
print("¿Está vacía ahora?", pila.esta_vacia())  # Debería ser True




