from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.next: Optional["Animal"] = None

    def get_nombre(self) -> str:
        return self.nombre

    def get_edad(self) -> int:
        return self.edad

    def get_tipo(self) -> str:
        return self.tipo

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional[Animal] = None

    def agregar(self, nombre: str, edad: int, tipo: str) -> None:
        if self.existe_animal(nombre, tipo):
            print(f"El animal {nombre} de tipo {tipo} ya está registrado.")
            return
        
        nuevo_animal = Animal(nombre, edad, tipo)
        if self.cabeza is None:
            self.cabeza = nuevo_animal
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_animal

    def existe_animal(self, nombre: str, tipo: str) -> bool:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.get_nombre() == nombre and nodo_actual.get_tipo() == tipo:
                return True
            nodo_actual = nodo_actual.next
        return False

    def mostrar_iterativo(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"Nombre: {nodo_actual.get_nombre()}, Edad: {nodo_actual.get_edad()}, Tipo: {nodo_actual.get_tipo()}")
            nodo_actual = nodo_actual.next

    def mostrar_recursivo(self, nodo: Optional[Animal] = None) -> None:
        if nodo is None:
            nodo = self.cabeza
        
        if nodo is not None:
            print(f"Nombre: {nodo.get_nombre()}, Edad: {nodo.get_edad()}, Tipo: {nodo.get_tipo()}")
            self.mostrar_recursivo(nodo.next)

lista_animales = ListaEnlazada()
lista_animales.agregar("Águila", 5, "Ave")
lista_animales.agregar("Pantera", 7, "Felino")
lista_animales.agregar("Vaca", 4, "Mamífero")
lista_animales.agregar("Águila", 5, "Ave")  

print("\nAnimales (Iterativo):")
lista_animales.mostrar_iterativo()

print("\nAnimales (Recursivo):")
lista_animales.mostrar_recursivo()
